from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .functionsPy import saveDB, sendEmail, updateDB, formsDate
from .models import *


def formsInfo(request):
    formsObject = formsDate.FormDate
    forms = formsObject.defineForms(formsObject)
    request.session["forms"] = forms
    contexto = {
        "forms": forms,
    }
    request.session["contexto"] = contexto


def select_city(request):
    if request.GET:
        print(request.GET.get("dados"), Estado.objects.all())
        estadoUf = request.GET.get("dados", None)
        estadoId = Estado.objects.get(uf=estadoUf)
        municipios = Municipio.objects.all().filter(idEstado=estadoId)
        listaMunicipios = []
        for item in municipios:
            listaMunicipios.append([item.id, item.nome])
        data = {"municipios": listaMunicipios, "nome": "municipios"}
        return JsonResponse(data)
    return HttpResponseRedirect("/")


def index(request):
    contextoTemp = {"estados": Estado.objects.all()}
    return render(request, "index.html", contextoTemp)


def cadastro(request):
    if request.method == "POST":
        print(request.POST)
        if request.POST["senha"] == request.POST["confirmeSenha"]:
            saveBase = saveDB.SaveDataBase()
            endereco = saveBase.CreateEndereco(request=request)
            usuario = saveBase.CreateUsuario(request=request)
            if endereco[0] == "Success" and usuario[0] == "Success":
                endereco[1].save()
                usuario[1].save()
                usuario[2].save()
                if request.POST["tipoPessoa"] == "1":
                    empresa = saveBase.CreateEmpresa(
                        request=request, id_endereco=endereco[1].id
                    )
                    empresa[1].save()
                elif request.POST["tipoPessoa"] == "2":
                    caminhoneiro = saveBase.CreateCaminhoneiro(
                        request=request, id_endereco=endereco[1].id
                    )
                    if caminhoneiro[0] == "Success":
                        caminhoneiro[1].save()
    return HttpResponseRedirect("/")


def logar(request):
    formsInfo(request)
    if request.method == "POST":
        user = authenticate(
            username=request.POST["usuario"], password=request.POST["senha"]
        )
        if user is not None:
            login(request, user)
            usuarioId = User.objects.get(username=request.POST["usuario"])
            usuarioObeject = Usuario.objects.get(usuario_chave=usuarioId)
            request.session["dados"] = {
                "descricao": usuarioObeject.descricao,
                "usuarioId": usuarioObeject.id,
            }
            return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")


def suporte(request):
    if request.method == "POST":
        dados = {
            "titulo": request.POST["motivo"],
            "mensagem": request.POST["mensagem"],
            "emailsList": [request.POST["email"]],
        }
        if request.POST["outroMotivo"]:
            dados["titulo"] = request.POST["outroMotivo"]
        emailObj = sendEmail.EnviarEmail()
        emailObj.enviarEmail(dados)
        return render(request, "suporte.html", {"emailEnviado": "true"})
    return render(request, "suporte.html", {"emailEnviado": "false"})


@login_required(redirect_field_name=None)
def fretes(request):
    return render(request, "fretes.html", request.session["contexto"])


@login_required(redirect_field_name=None)
def network(request):
    filialCriada = "None"
    funcionarioCriado = "None"
    if request.method == "POST":
        saveBase = saveDB.SaveDataBase()
        if request.POST["inputForm"] == "filial":
            if request.POST["senha"] == request.POST["confirmeSenha"]:
                if saveBase.CreateUsuario(request=request) == "Success":
                    endereco = saveBase.CreateEndereco(request=request)
                    empresa = saveBase.CreateEmpresa(request=request)
                    if endereco[0] == "Success" and empresa[0] == "Success":
                        endereco[1].save()
                        empresa[1].save()
                        values = {
                            "id_empresa": empresa[1].id,
                            "usuario": request.POST["usuario"],
                            "id_endereco": endereco[1].id,
                        }
                        filial = saveBase.CreateFilial(values=values)
                        if filial[0] == "Success":
                            filial[1].save()
                            filialCriada = "Success"
        elif request.POST["inputForm"] == "funcionario":
            funcionarioCriado = "Success"

    request.session["contexto"]["estados"] = Estado.objects.all()
    request.session["contexto"]["empresas"] = Empresa.objects.all()
    return render(request, "network.html", request.session["contexto"])


@login_required(redirect_field_name=None)
def caminhoes(request):
    caminhaoCriado = "None"
    carretaCriado = "None"
    if request.method == "POST":
        saveBase = saveDB.SaveDataBase()
        if request.POST["inputForm"] == "caminhao":
            if saveBase.CreateCaminhao(request=request) == "Success":
                caminhaoCriado = "Success"
                return HttpResponseRedirect(reverse("caminhoes"))
        elif request.POST["inputForm"] == "carreta":
            if saveBase.CreateCarreta(request=request) == "Success":
                carretaCriado = "Success"
                return HttpResponseRedirect(reverse("caminhoes"))
    caminhoesObject = Caminhao.objects.all().filter(
        idUsuario=request.session["dados"]["usuarioId"]
    )
    carretaObject = Carreta.objects.all().filter(
        idUsuario=request.session["dados"]["usuarioId"]
    )
    caminhoesList = []
    carretasList = []
    for item in caminhoesObject:
        marca = Marca.objects.get(nome=item.idMarca)
        caminhoesList.append(
            {
                "id": item.id,
                "nome": item.nome,
                "eixos": item.eixos,
                "marca": marca.nome,
                "id_marca": marca.id,
            }
        )
    for item in carretaObject:
        tipoCarreta = TipoCarreta.objects.get(id=item.idTipoCarreta.id)
        tipoReboque = TipoReboque.objects.get(id=item.idTipoReboque.id)
        carretasList.append(
            {
                "id": item.id,
                "peso_maximo": item.pesoMaximo,
                "tipoCarreta": tipoCarreta.id,
                "tipoReboque": tipoReboque.id,
            }
        )
    contexto = {
        "caminhoes": caminhoesList,
        "carretas": carretasList,
        "marcas": Marca.objects.all(),
        "tipoReboque": TipoReboque.objects.all(),
        "tipoCarreta": TipoCarreta.objects.all(),
        "caminhaoCriado": caminhaoCriado,
        "carretaCriado": carretaCriado,
        "forms": request.session["forms"],
    }
    return render(request, "caminhoes.html", contexto)


@login_required(redirect_field_name=None)
def perfis(request):
    return render(request, "perfis.html", request.session["contexto"])


@login_required(redirect_field_name=None)
def atividade(request):
    return render(request, "atividade.html")


@login_required(redirect_field_name=None)
def usuario(request):
    contexto = {
        "estados": Estado.objects.all(),
        "sesssionDados": request.session["dados"],
    }
    return render(request, "usuario.html", contexto)


@login_required(redirect_field_name=None)
def logout_view(request):
    if User.is_authenticated or User.is_staff:
        logout(request)
        return HttpResponseRedirect("/")


@login_required(redirect_field_name=None)
def delCaminhoes(request):
    if request.GET:
        caminhaoId = request.GET.get("dados", None)
        Caminhao.objects.get(id=caminhaoId).delete()
        data = {"nome": "delCaminhoes", "id": "caminhaoId" + str(caminhaoId)}
        return JsonResponse(data)
    return HttpResponseRedirect("/")


@login_required(redirect_field_name=None)
def delCarreta(request):
    if request.GET:
        carretaId = request.GET.get("dados", None)
        Carreta.objects.get(id=carretaId).delete()
        data = {"nome": "delCarreta", "id": "carretaId" + str(carretaId)}
        return JsonResponse(data)
    return HttpResponseRedirect("/")


@login_required(redirect_field_name=None)
def updateCaminhoes(request):
    if request.method == "POST":
        updateBase = updateDB.UpdateDataBase
        updateBase.updateCaminhoes(updateBase, request)
    return HttpResponseRedirect("/caminhoes/")


@login_required(redirect_field_name=None)
def updateCarreta(request):
    if request.method == "POST":
        updateBase = updateDB.UpdateDataBase
        updateBase.updateCarreta(updateBase, request)
    return HttpResponseRedirect("/caminhoes/")

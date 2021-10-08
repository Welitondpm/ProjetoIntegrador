from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .functionsPy import saveDB, sendEmail, updateDB, formsDate
from .models import *


def formsInfo(request, nome):
	formsObject = formsDate.FormDate
	if nome == "formLogin":
		forms = formsObject.defineFormsLogin(formsObject)
	else:
		forms = formsObject.defineForms(formsObject)
	request.session["forms"] = forms
	contexto = {
		"forms": forms,
	}
	request.session["contexto"] = contexto


def index(request):
	if not request.user.is_authenticated:
		formsInfo(request, "formLogin")
	return render(request, "index.html", request.session["contexto"])


def cadastro(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	formsInfo(request, "formLogin")
	if request.method == 'POST':
		if request.POST['senha'] == request.POST['confirmeSenha']:
			saveBase = saveDB.SaveDataBase()
			if saveBase.CreateUsuario(request=request) == "Success":
				return HttpResponseRedirect('/')
	return render(request, "cadastro.html", request.session["contexto"])


def logar(request):
	formsInfo(request, "")
	if request.method == 'POST':
		user = authenticate(username=request.POST['usuario'], password=request.POST["senha"])
		if user is not None:
			login(request, user)
			usuarioId = User.objects.get(username=request.POST['usuario'])
			usuarioObeject = Usuario.objects.get(usuario_chave=usuarioId)
			request.session['dados'] = {
				'descricao': usuarioObeject.descricao,
				"usuarioId": usuarioObeject.id,
			}
			return HttpResponseRedirect('/')


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
		elif request.POST["inputForm"] == "carreta":
			if saveBase.CreateCarreta(request=request) == "Success":
				carretaCriado = "Success"	
	caminhoesObject = Caminhao.objects.all().filter(idUsuario = request.session["dados"]["usuarioId"])
	carretaObject = Carreta.objects.all().filter(idUsuario = request.session["dados"]["usuarioId"])
	caminhoesList = []
	carretasList = []
	for item in caminhoesObject:
		marca = Marca.objects.get(nome=item.idMarca)
		caminhoesList.append({
			"id": item.id, 
			"nome": item.nome,
			"eixos": item.eixos,
			"marca": marca.nome,
			"id_marca": marca.id,
		})
	for item in carretaObject:
		tipoCarreta = TipoCarreta.objects.get(id=item.idTipoCarreta.id)
		tipoReboque = TipoReboque.objects.get(id=item.idTipoReboque.id)
		carretasList.append({
			"id": item.id, 
			"peso_maximo": item.pesoMaximo,
			"tipoCarreta": tipoCarreta.id,
			"tipoReboque": tipoReboque.id,
		})
	contexto = {
		"caminhoes": caminhoesList,
		"carretas": carretasList,
		'marcas': Marca.objects.all(),
		'tipoReboque': TipoReboque.objects.all(),
		'tipoCarreta': TipoCarreta.objects.all(),
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
		'estados': Estado.objects.all(),
		'sesssionDados': request.session['dados'],
	}
	return render(request, "usuario.html", contexto)


@login_required(redirect_field_name=None)
def logout_view(request):
	if User.is_authenticated or User.is_staff:
		logout(request)
		return HttpResponseRedirect('/')


@login_required(redirect_field_name=None)
def select_city(request):
	if request.GET:
		estadoUf = request.GET.get('dados', None)
		estadoId = Estado.objects.get(uf = estadoUf)
		municipios = Municipio.objects.all().filter(idEstado = estadoId)
		listaMunicipios = []
		for item in municipios:
			listaMunicipios.append([item.id ,item.nome])
		data = {'municipios': listaMunicipios, 'nome': 'municipios'}
		return JsonResponse(data)
	return HttpResponseRedirect('/')


@login_required(redirect_field_name=None)
def delCaminhoes(request):
	if request.GET:
		caminhaoId = request.GET.get('dados', None)
		Caminhao.objects.get(id = caminhaoId).delete()
		data = {'nome': 'delCaminhoes', "id": "caminhaoId" + str(caminhaoId)}
		return JsonResponse(data)
	return HttpResponseRedirect('/')


@login_required(redirect_field_name=None)
def delCarreta(request):
	if request.GET:
		carretaId = request.GET.get('dados', None)
		Carreta.objects.get(id = carretaId).delete()
		data = {'nome': 'delCarreta', "id": "carretaId" + str(carretaId)}
		return JsonResponse(data)
	return HttpResponseRedirect('/')


@login_required(redirect_field_name=None)
def updateCaminhoes(request):
	if request.method == 'POST':
		updateBase = updateDB.UpdateDataBase
		updateBase.updateCaminhoes(updateBase, request)
	return HttpResponseRedirect('/caminhoes/')


@login_required(redirect_field_name=None)
def updateCarreta(request):
	if request.method == 'POST':
		updateBase = updateDB.UpdateDataBase
		updateBase.updateCarreta(updateBase, request)
	return HttpResponseRedirect('/caminhoes/')
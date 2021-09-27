from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect, JsonResponse
from .templates.assets import saveDB, sendEmail
from .models import *


def index(request):
	return render(request, "index.html")


def select_city(request):
	estadoUf = request.GET.get('dados', None)
	estadoId = Estado.objects.get(uf = estadoUf)
	municipios = Municipio.objects.all().filter(idEstado = estadoId)
	listaMunicipios = []
	for item in municipios:
		listaMunicipios.append([item.id ,item.nome])
	data = {'municipios': listaMunicipios, 'nome': 'municipios'}
	return JsonResponse(data)


def delCaminhoes(request):
	caminhaoId = request.GET.get('dados', None)
	caminhaoObj = Caminhao.objects.get(id = caminhaoId).delete()
	data = {'nome': 'delCaminhoes', "id": "caminhaoId" + str(caminhaoId)}
	return JsonResponse(data)
	

def cadastro(request):
	if request.method == 'POST':
		if request.POST['senha'] == request.POST['confirmeSenha']:
			saveBase = saveDB.SaveDataBase()
			if saveBase.CreateUsuario(request=request) == "Success":
				return HttpResponseRedirect('/login/')
	return render(request, "cadastro.html")


def logar(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['usuario'], password=request.POST["senha"])
		if user is not None:
			login(request, user)
			usuarioId = User.objects.get(username=request.POST['usuario'])
			usuarioObeject = Usuario.objects.get(usuario_chave=usuarioId)
			request.session['dados'] = {
				'descricao': usuarioObeject.descricao,
				"usuarioId": usuarioId.id,
			}
			return HttpResponseRedirect('/')
	return render(request, "login.html")


def logout_view(request):
	if User.is_authenticated or User.is_staff:
		logout(request)
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


def fretes(request):
	return render(request, "fretes.html")


def caminhoes(request):
	caminhaoCriado = "None"
	if request.method == "POST":
		if request.POST["inputForm"] == "caminhao":
			saveBase = saveDB.SaveDataBase()
			if saveBase.CreateCaminhao(request=request) == "Success":
				caminhaoCriado = "Success"
	caminhoesObject = Caminhao.objects.all().filter(idUsuario = request.session["dados"]["usuarioId"])
	caminhoesList = []
	for item in caminhoesObject:
		marca = Marca.objects.get(nome=item.idMarca)
		caminhoesList.append({
			"id": item.id, 
			"nome": item.nome,
			"eixos": item.eixos,
			"marca": marca.nome,
		})
	contexto = {
		"caminhoes": caminhoesList,
		'marcas': Marca.objects.all(),
		"caminhaoCriado": caminhaoCriado,
	}
	return render(request, "caminhoes.html", contexto)


def perfis(request):
	return render(request, "perfis.html")


def network(request):
	return render(request, "network.html")


def usuario(request):
	contexto = {
		'estados': Estado.objects.all(),
		'carretas': TipoCarreta.objects.all(),
		'carrocerias': TipoReboque.objects.all(),
		'sesssionDados': request.session['dados'],
	}
	return render(request, "usuario.html", contexto)


def atividade(request):
	return render(request, "atividade.html")

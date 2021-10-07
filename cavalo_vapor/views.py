from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect, JsonResponse
from .templates.assets import saveDB, sendEmail
from .models import *


def index(request):
	forms = {
		'formLogin': {
			"Name": 'Login',
			"Url": "templates-form/formLogin.html",
			"ButtonText": "Logar",
			"ActionUrl": "/login/",
			"modalId": "formularioLogin",
		},
		'formCadastro': {
			"Name": 'Cadastro',
			"Url": "templates-form/formCadastro.html",
			"ButtonText": "Cadastrar",
			"ActionUrl": "/cadastro/",
			"modalId": "formularioCadastro",
		},
	}
	contexto = {
		"forms": forms,
	}
	return render(request, "index.html", contexto)


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


def delCarreta(request):
	carretaId = request.GET.get('dados', None)
	carretaObj = Carreta.objects.get(id = carretaId).delete()
	data = {'nome': 'delCarreta', "id": "carretaId" + str(carretaId)}
	return JsonResponse(data)


def updateCaminhoes(request):
	print(request.POST)
	if request.method == 'POST':
		caminhaoObj = Caminhao.objects.get(id = request.POST['idCaminhao'])
		caminhaoObj.nome = request.POST['nome']
		caminhaoObj.eixos = request.POST['eixos']
		caminhaoObj.idMarca = Marca.objects.get(id=request.POST['id_marca'])
		caminhaoObj.save()
	return HttpResponseRedirect('/caminhoes/')


def updateCarreta(request):
	print(request.POST)
	if request.method == 'POST':
		carretaObj = Carreta.objects.get(id = request.POST['idCarreta'])
		carretaObj.pesoMaximo = request.POST['pesoMaximo']
		carretaObj.idTipoReboque = TipoReboque.objects.get(id=request.POST['id_TipoReboque'])
		carretaObj.idTipoCarreta = TipoCarreta.objects.get(id=request.POST['id_TipoCarreta'])
		carretaObj.save()
	return HttpResponseRedirect('/caminhoes/')
	

def cadastro(request):
	if request.method == 'POST':
		if request.POST['senha'] == request.POST['confirmeSenha']:
			saveBase = saveDB.SaveDataBase()
			if saveBase.CreateUsuario(request=request) == "Success":
				return HttpResponseRedirect('/')
	forms = {
		'formLogin': {
			"Name": 'Login',
			"Url": "templates-form/formLogin.html",
			"ButtonText": "Logar",
			"ActionUrl": "/login/",
			"modalId": "formularioLogin",
		},
	}
	contexto = {
		"forms": forms,
	}
	return render(request, "cadastro.html", contexto)


def logar(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['usuario'], password=request.POST["senha"])
		if user is not None:
			login(request, user)
			formsInfo(request)
			usuarioId = User.objects.get(username=request.POST['usuario'])
			usuarioObeject = Usuario.objects.get(usuario_chave=usuarioId)
			request.session['dados'] = {
				'descricao': usuarioObeject.descricao,
				"usuarioId": usuarioObeject.id,
			}
			return HttpResponseRedirect('/')


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
	contexto = {
		"forms": request.session["forms"],
	}
	return render(request, "fretes.html", contexto)


def caminhoes(request):
	caminhaoCriado = "None"
	if request.method == "POST":
		if request.POST["inputForm"] == "caminhao":
			saveBase = saveDB.SaveDataBase()
			if saveBase.CreateCaminhao(request=request) == "Success":
				caminhaoCriado = "Success"
	carretaCriado = "None"
	if request.method == "POST":
		if request.POST["inputForm"] == "carreta":
			saveBase = saveDB.SaveDataBase()
			if saveBase.CreateCarreta(request=request) == "Success":
				carretaCriado = "Success"	
	
	caminhoesObject = Caminhao.objects.all().filter(idUsuario = request.session["dados"]["usuarioId"])
	caminhoesList = []
	for item in caminhoesObject:
		marca = Marca.objects.get(nome=item.idMarca)
		caminhoesList.append({
			"id": item.id, 
			"nome": item.nome,
			"eixos": item.eixos,
			"marca": marca.nome,
			"id_marca": marca.id,
		})
	carretaObject = Carreta.objects.all().filter(idUsuario = request.session["dados"]["usuarioId"])
	carretasList = []
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


def perfis(request):
	contexto = {
		"forms": request.session["forms"],
	}
	return render(request, "perfis.html", contexto)


def network(request):
	contexto = {
		"forms": request.session["forms"],
	}
	return render(request, "network.html", contexto)


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


def formsInfo(request):
	forms = {
		'formUpdateCaminhao': {
			"Name": "Atualize seu Caminhão",
			"Url": "templates-form/formCaminhao.html",
			"ButtonText": "Salvar Alterações",
			"ActionUrl": "/update/updateCaminhao/",
			"modalId": "formularioUpdateCaminhao",
		},
		'formCadastroCaminhao': {
			"Name": "Cadastre um Caminhão",
			"Url": "templates-form/formCaminhao.html",
			"ButtonText": "Cadastrar Caminhão",
			"ActionUrl": "",
			"modalId": "formularioCadastroCaminhao",
		},
		'formUpdateCarreta': {
			"Name": "Atualize sua Carreta",
			"Url": "templates-form/formCarreta.html",
			"ButtonText": "Salvar Alterações",
			"ActionUrl": "/update/updateCarreta/",
			"modalId": "formularioUpdateCarreta",
		},
		'formCadastroCarreta': {
			"Name": "Cadastre uma Carreta",
			"Url": "templates-form/formCarreta.html",
			"ButtonText": "Cadastrar Carreta",
			"ActionUrl": "",
			"modalId": "formularioCadastroCarreta",
		},
		'formPesquisaFretes': {
			"Placeholder": "Buscar Frete",
			"FiltrosTemplate": "templates-filtros/filtrosFretes.html",
		},
		'formPesquisaNetwork': {
			"Placeholder": "Buscar Filial/Funcionário",
			"FiltrosTemplate": "templates-filtros/filtrosNetwork.html",
		},
		'formPesquisaCaminhao': {
			"Placeholder": "Buscar Caminhões/Carretas",
			"FiltrosTemplate": "templates-filtros/filtrosCaminhao.html",
		},
		'formPesquisaPerfis': {
			"Placeholder": "Buscar Perfil por Nome, CPF/CNPJ",
			"FiltrosTemplate": "templates-filtros/filtrosPerfis.html",
		},
	}
	request.session["forms"] = forms
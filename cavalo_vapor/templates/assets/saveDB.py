from django.contrib.auth.models import User
from django.db import models
from cavalo_vapor.models import *
from .vereficadores import *

class SaveDataBase():
  
  def CreateUsuario(self, request):
    descricao = "Agora isso foi automatico"
    if verificaTamanho(descricao, 200):
      user = User.objects.create_user(
        username = request.POST['usuario'],
        email = request.POST['email'],
        password = request.POST['senha'],
        first_name = request.POST['firstName'],
        last_name = request.POST['lastName'],
      )
      usuarioExtend = Usuario(
        descricao = descricao,
        usuario_chave = User.objects.get(username=request.POST['usuario']),
      )
      user.save()
      usuarioExtend.save()
      return "Success"
    return "Failed"


  def EnderecoSave(self, request):
    rua = request.POST['rua'],
    cep = request.POST['cep'],
    bairro = request.POST['bairro'],
    numero = request.POST['numero'],
    ruaBool = verificaTamanho(rua, 200)
    cepBool, cep = verificaReorganizeCep(cep)
    bairroBool = verificaTamanho(bairro, 200)
    if ruaBool and cepBool and bairroBool and type(numero) == int:
      endereco = Endereco(
        rua = rua,
        cep = cep,
        bairro = bairro,
        numero = numero,
        idMunicipio = Municipio.objects.get(id=request.POST['municipio']),
        idEstado = Estado.objects.get(uf=request.POST['estado']),
      )
      endereco.save()
      return "Success"
    return "Failed"


  def CreateEmail(self, request):
    email = request.POST['email'],
    if verificaEmail(email):
      email = Email(
        email = email,
        idUsuario = User.objects.get(username=request.POST['usuario']),
      )
      email.save()
      return "Success"
    return "Failed"
  

  def CreateTelefone(self, request):
    telefone = request.POST['telefone']
    if verificaTelefone(telefone):
      telefone = Telefone(
        telefone = telefone,
        idUsuario = User.objects.get(username=request.POST['usuario']),
      )
      telefone.save()
      return "Success"
    return "Failed"


  def CreateEmpresa(self, request):
    cnpj = request.POST['cnpj']
    if verificaCNPJ(cnpj):
      empresa = Empresa(
        cnpj = OrganizaCpfCnpj(cnpj),
        anoFundacao = request.POST['anoFundacao'],
        idUsuario = User.objects.get(username=request.POST['usuario']),
      )
      empresa.save()
      return "Success"
    return "Failed"


  def CreateFuncionario(self, request):
    matricula = request.POST['matricula']
    cpf = request.POST['cpf']
    if verificaTamanho(matricula, 50) and verificaCPF(cpf):
      funcionario = Funcionario(
        matricula = matricula,
        cpf = OrganizaCpfCnpj(cpf),
        idUsuario = User.objects.get(username=request.POST['usuario']),
      )
      funcionario.save()
      return "Success"
    return "Failed"
  

  def CreateFilial(self, request):
    filial = Filial(
      idEmpresa = Empresa.objects.get(username=request.POST['id_empresa']),
      idUsuario = User.objects.get(id=request.POST['usuario']),
      idEndereco = Endereco.objects.get(id=request.POST['id_endereco']),
    )
    filial.save()


  def CreateFuncionarioFilial(self, request):
    funcionarioFilial = FuncionarioFilial(
      idFuncionario = Funcionario.objects.get(id=request.POST['id_funcionario']),
      idFilial = Filial.objects.get(id=request.POST['id_filial']),
    )
    funcionarioFilial.save()
  

  def CreateMarca(self, request):
    nome = request.POST['nome']
    if verificaTamanho(nome, 150):
      marca = Marca(
        nome = nome,
      )
      marca.save()
      return "Success"
    return "Failed"
  

  def CreateCaminhao(self, request):
    nome = request.POST['nome']
    eixos = request.POST['eixos']
    if verificaTamanho(nome, 200) and verificaTamanho(eixos, 2):
      caminhao = Caminhao(
        nome = nome,
        eixos = eixos,
        idUsuario = User.objects.get(username=request.POST['username']),
        idMarca = Marca.objects.get(id=request.POST['id_marca']),
      )
      caminhao.save()
      return "Success"
    return "Failed"

  
  def CreateCaminhoneiro(self, request):
    cpf = request.POST['cpf']
    if verificaCPF(cpf):
      caminhoneiro = Caminhoneiro(
        cpf = OrganizaCpfCnpj(cpf),
        idUsuario = User.objects.get(id=request.POST['username']),
        idEndereco = Endereco.objects.get(id=request.POST['id_endereco']),
      )
      caminhoneiro.save()
      return "Success"
    return "Failed"

  
  def CreateTipoCarreta(self, request):
    nome = request.POST['nome']
    eixos = request.POST['eixos']
    if verificaTamanho(nome, 100) and verificaTamanho(eixos, 2):
      tipoCarreta = TipoCarreta(
        nome = nome,
        eixos = eixos,
      )
      tipoCarreta.save()
      return "Success"
    return "Failed"
  

  def CreateTipoReboque(self, request):
    nome = request.POST['nome']
    if verificaTamanho(nome, 100):
      tipoReboque = TipoReboque(
        nome = nome,
      )
      tipoReboque.save()
      return "Success"
    return "Failed"

  
  def CreateCarreta(self, request):
    pesoMaximo = request.POST['pesoMaximo']
    if verificaTamanho(pesoMaximo, 2):
      carreta = Carreta(
        pesoMaximo = pesoMaximo,
        idUser = User.objects.get(username=request.POST['username']),
        idTipoCarreta = TipoCarreta.objects.get(id=request.POST['id_TipoCarreta']),
        idTipoReboque = TipoReboque.objects.get(id=request.POST['id_TipoReboque']),
      )
      carreta.save()
      return "Success"
    return "Failed"
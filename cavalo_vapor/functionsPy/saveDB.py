from django.contrib.auth.models import User
from ..models import *
from .vereficadores import *

class SaveDataBase():
  def CreateUsuario(self, request):
    user = User.objects.create_user(
      username = request.POST['usuario'],
      email = request.POST['email'],
      password = request.POST['senha'],
      first_name = request.POST['firstName'],
    )
    usuarioExtend = Usuario(
      # descricao = request.POST['descricao'],
      usuario_chave = User.objects.get(username=request.POST['usuario']),
    )
    return ("Success", user, usuarioExtend)


  def CreateEndereco(self, request):
    rua = request.POST['rua']
    cep = request.POST['cep']
    bairro = request.POST['bairro']
    numero = int(request.POST['numero'])
    ruaBool = verificaTamanho(rua, 200)
    cepBool, cep = verificaReorganizeCep(cep)
    bairroBool = verificaTamanho(bairro, 200)
    if ruaBool and cepBool and bairroBool:
      endereco = Endereco(
        rua = rua,
        cep = cep,
        bairro = bairro,
        numero = numero,
        idMunicipio = Municipio.objects.get(id=request.POST['municipio']),
        idEstado = Estado.objects.get(uf=request.POST['estado']),
      )
      return ("Success", endereco)
    return ("Failed", "")


  def CreateEmail(self, request):
    email = request.POST['email']
    if verificaEmail(email):
      email = Email(
        email = email,
        idUsuario = Usuario.objects.get(id=request.session["dados"]['usuarioId']),
      )
      email.save()
      return "Success"
    return "Failed"


  def CreateEmpresa(self, request, id_endereco):
    cnpj = request.POST['CNPJ']
    idUsuario = User.objects.get(username=request.POST['usuario'])
    if verificaCNPJ(cnpj):
      empresa = Empresa(
        cnpj = OrganizaCpfCnpj(cnpj),
        anoFundacao = request.POST['dataFundacao'],
        idUsuario = Usuario.objects.get(usuario_chave=idUsuario),
        idEndereco = Endereco.objects.get(id=id_endereco),
      )
      return ("Success", empresa)
    return ("Failed")


  def CreateFuncionario(self, request):
    matricula = request.POST['matricula']
    cpf = request.POST['cpf']
    idUsuario = User.objects.get(username=request.POST['usuario'])
    if verificaTamanho(matricula, 50) and verificaCPF(cpf):
      funcionario = Funcionario(
        matricula = matricula,
        cpf = OrganizaCpfCnpj(cpf),
        idUsuario = Usuario.objects.get(usuario_chave=idUsuario),
      )
      return ("Success", funcionario)
    return "Failed"


  def CreateFuncionarioFilial(self, values):
    funcionarioEmpresa = FuncionarioEmpresa(
      idFuncionario = Funcionario.objects.get(id=values['id_funcionario']),
      idEmpresa = Empresa.objects.get(id=values['id_empresa']),
    )
    return ("Success", funcionarioEmpresa)
  

  def CreateCaminhao(self, request):
    nome = request.POST['nome']
    eixos = request.POST['eixos']
    if verificaTamanho(nome, 200) and verificaTamanho(eixos, 2):
      caminhao = Caminhao(
        nome = nome,
        eixos = eixos,
        idUsuario = Usuario.objects.get(id=request.session['dados']['usuarioId']),
        idMarca = Marca.objects.get(id=request.POST['id_marca']),
      )
      caminhao.save()
      return "Success"
    return "Failed"

  
  def CreateCaminhoneiro(self, request, id_endereco):
    cpf = request.POST['CPF']
    idUsuario = User.objects.get(username=request.POST['usuario'])
    if verificaCPF(cpf):
      caminhoneiro = Caminhoneiro(
        cpf = OrganizaCpfCnpj(cpf),
        idUsuario = Usuario.objects.get(usuario_chave=idUsuario),
        idEndereco = Endereco.objects.get(id=id_endereco),
      )
      return ("Success", caminhoneiro)
    return ("Failed", "")

  
  def CreateCarreta(self, request):
    pesoMaximo = request.POST['pesoMaximo']
    if verificaTamanho(pesoMaximo, 2):
      carreta = Carreta(
        pesoMaximo = pesoMaximo,
        idUsuario = Usuario.objects.get(id=request.session['dados']['usuarioId']),
        idTipoCarreta = TipoCarreta.objects.get(id=request.POST['id_TipoCarreta']),
        idTipoReboque = TipoReboque.objects.get(id=request.POST['id_TipoReboque']),
      )
      carreta.save()
      return "Success"
    return "Failed"
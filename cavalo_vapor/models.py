from django.db import models
from django.contrib.auth.models import User #, AbstractBaseUser


class Estado(models.Model):
  nome = models.CharField(max_length=200, unique=True)
  uf = models.CharField(max_length=2, unique=True)

  def __str__(self):
    return self.nome

class Municipio(models.Model):
  nome = models.CharField(max_length=200)
  idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)

  def __str__(self):
    return self.nome

class Marca(models.Model):
  nome = models.CharField(max_length=150, unique=True)

  def __str__(self):
    return self.nome

class TipoCarreta(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome

class TipoReboque(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome


class Endereco(models.Model):
  rua = models.CharField(max_length=200)
  cep = models.CharField(max_length=9)
  bairro = models.CharField(max_length=150)
  numero = models.SmallIntegerField()
  idMunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
  idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
  
  def __str__(self):
    return "Endereço: " + str(self.id)

class Usuario(models.Model):
  usuario_chave = models.ForeignKey(User, on_delete=models.CASCADE)
  descricao = models.CharField(max_length=200)

  def __str__(self):
    return str(self.id)

class Email(models.Model):
  email = models.CharField(max_length=200)
  idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

  def __str__(self):
    return self.email

class Empresa(models.Model):
  cnpj = models.CharField(max_length=18, unique=True)
  anoFundacao = models.DateField()
  idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

  def __str__(self):
    return self.cnpj

class Funcionario(models.Model):
  matricula = models.CharField(max_length=50, unique=True)
  cpf = models.CharField(max_length=14, unique=True)
  idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

  def __str__(self):
    return self.cpf

class FuncionarioEmpresa(models.Model):
  idFuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
  idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id)

class Caminhao(models.Model):
  nome = models.CharField(max_length=200)
  eixos = models.CharField(max_length=2)
  idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  idMarca = models.ForeignKey(Marca, on_delete=models.CASCADE)

  def __str__(self):
    return self.nome

class Caminhoneiro(models.Model):
  cpf = models.CharField(max_length=14, unique=True)
  idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

  def __str__(self):
    return self.cpf

class Carreta(models.Model):
  pesoMaximo = models.CharField(max_length=2)
  idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  idTipoCarreta = models.ForeignKey(TipoCarreta, on_delete=models.CASCADE)
  idTipoReboque = models.ForeignKey(TipoReboque, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.idUsuario)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Estado(models.Model):
    nome = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)


class Municipio(models.Model):
    nome = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


class Adress(models.Model):
    rua = models.CharField(max_length=200)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=150)
    number = models.SmallIntegerField()
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


class Usuario(models.Model):
    soma_avaliacoes = models.IntegerField(default=0)
    foto_capa = models.CharField(max_length=200, blank=True)
    logo = models.CharField(max_length=200, blank=True)
    qtd_avaliacoes = models.IntegerField(default=0)
    descricao = models.TextField(blank=True)
    modo_preferencia = models.CharField(max_length=1, default=0)
    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=64)
    usuario = models.OneToOneField(User, on_delete=CASCADE)
    login = models.CharField(max_length=200)
    admin = models.BooleanField(max_length=1, default=False)
    imagem = models.ImageField(default="default.jpeg", upload_to="img_perfil")

    def __str__(self):
        return f"{self.usuario.username} Perfil"

    def save(self, *args, **kwargs):
        super(Perfil, self).save(*args, **kwargs)

        img = Image.open(self.imagem.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.imagem.path)
# class Suporte(models.Model):
#     motivo_contato = models.CharField(max_length=40)
#     mensagem = models.TextField()
#     data_hora = models.DateTimeField()
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Email(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    email_de_recuperacao = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Telefone(models.Model):
    numero = models.CharField(max_length=15)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Empresa(models.Model):
    cnpj = models.CharField(max_length=18, primary_key=True)
    ano_fundacao = models.CharField(max_length=4, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Filial(models.Model):
    cnpj = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)


class Funcionario(models.Model):
    matricula = models.IntegerField()
    genero = models.CharField(max_length=1, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Funcionario_Filial(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)


class Notificacao(models.Model):
    data_hora = models.DateTimeField()
    texto = models.TextField()
    titulo = models.CharField(max_length=150)
    cnpj = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Destinatarios(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    notificacao = models.ForeignKey(Notificacao, on_delete=models.CASCADE)


class Sala(models.Model):
    data_hora = models.DateTimeField()
    open_close = models.CharField(max_length=1, default=1)
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Integrante(models.Model):
    permissao = models.CharField(max_length=40)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Post(models.Model):
    data_hora = models.DateTimeField()
    texto = models.TextField()
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)


class Sala_favorita(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Caminhoneiro(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    data_nascimento = models.DateField(blank=True)
    genero = models.CharField(max_length=1, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    adrees = models.ForeignKey(Adress, on_delete=models.CASCADE)


class Marca(models.Model):
    marca = models.CharField(max_length=150, primary_key=True)


class Caminhao(models.Model):
    potencia = models.SmallIntegerField()
    eixos = models.SmallIntegerField()
    litros = models.SmallIntegerField(blank=True)
    autonomia = models.SmallIntegerField(blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)


class Tipo_Carreta(models.Model):
    tipo_de_carreta = models.CharField(max_length=100)
    eixos = models.SmallIntegerField()


class Tipo_Reboque(models.Model):
    tipo_de_reboque = models.CharField(max_length=100)


class Carreta(models.Model):
    peso_max = models.SmallIntegerField()
    eixos = models.SmallIntegerField()
    volume_max = models.SmallIntegerField()
    comprimento = models.FloatField(blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_de_carreta = models.ForeignKey(Tipo_Carreta, on_delete=models.CASCADE)
    tipo_de_reboque = models.ForeignKey(Tipo_Reboque, on_delete=models.CASCADE)


class Frete(models.Model):
    descricao = models.TextField()
    avaliacao_empresa = models.SmallIntegerField(default=0)
    tipo_de_carga = models.CharField(max_length=150)
    data_hora_carga = models.DateTimeField()
    carga = models.CharField(max_length=150)
    avaliacao_caminhoneiro = models.SmallIntegerField(default=0)
    valor = models.CharField(max_length=20)
    tipo_reboque = models.TextField()
    status_fretes = models.CharField(max_length=50)
    data_hora_prazo = models.DateTimeField()
    distancia = models.SmallIntegerField()
    data_hora_descarga = models.DateTimeField(blank=True)
    descricao_status = models.TextField()
    peso_incial = models.SmallIntegerField()
    tempo_de_candidato = models.SmallIntegerField(default=168)


class Adress_Frete(models.Model):
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    frete = models.ForeignKey(Frete, on_delete=models.CASCADE)
    carga_descarga = models.CharField(max_length=1)


class Frete_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    frete = models.ForeignKey(Frete, on_delete=models.CASCADE)
    cliente_prestador = models.CharField(max_length=40)


class Candidato(models.Model):
    carreta = models.ForeignKey(Carreta, on_delete=models.CASCADE)
    caminhao = models.ForeignKey(Caminhao, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    frete = models.ForeignKey(Frete, on_delete=models.CASCADE)

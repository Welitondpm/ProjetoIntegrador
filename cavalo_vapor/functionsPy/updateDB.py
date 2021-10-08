from ..models import *


class UpdateDataBase():
  def updateCaminhoes(self, request):
    caminhaoObj = Caminhao.objects.get(id = request.POST['idCaminhao'])
    caminhaoObj.nome = request.POST['nome']
    caminhaoObj.eixos = request.POST['eixos']
    caminhaoObj.idMarca = Marca.objects.get(id=request.POST['id_marca'])
    caminhaoObj.save()


  def updateCarreta(self, request):
    carretaObj = Carreta.objects.get(id = request.POST['idCarreta'])
    carretaObj.pesoMaximo = request.POST['pesoMaximo']
    carretaObj.idTipoReboque = TipoReboque.objects.get(id=request.POST['id_TipoReboque'])
    carretaObj.idTipoCarreta = TipoCarreta.objects.get(id=request.POST['id_TipoCarreta'])
    carretaObj.save()

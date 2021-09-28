function mostrarInputMotivo (elemento){
  inputMotivo = document.getElementById("formGroupInputMotivo")
  if (elemento == "outro"){
    inputMotivo.classList.remove("d-none")
  } else {
    inputMotivo.classList.add("d-none")
  }
}


function login(){
  $('#formularioLogin').modal({backdrop:"static"})
}


function ajaxConection(dados){
  $.ajax({
    url: dados["url"],
    data: {
      'dados': dados["dados"],
    },
    success: function(data) {
      conectionSuccess(data)
    }
  })
}


function conectionSuccess(data){
  if (data["nome"] == "municipios"){
    PreencheMunicipios(data)
  } else if (data["nome"] == "delCaminhoes"){
    removeCaminhaoDeletado(data["id"])
  } else if (data["nome"] == "delCarreta"){
    removeCarretaDeletada(data["id"])
  }
}


function PreencheMunicipios(dados) {
  var municipios = dados["municipios"]
  document.getElementById("inputCidade").innerHTML = ""
  var htmlInner = ""
  for (item of municipios) {
    htmlInner += "<option value=" + item[0] + ">" + item[1] + "</option>"
  }
  document.getElementById("inputCidade").innerHTML = htmlInner
}


function removeCaminhaoDeletado(id){
  document.getElementById(id).remove();
  verificaCaminhoesExistente()
}


function removeCarretaDeletada(id){
  document.getElementById(id).remove();
  verificaCarretasExistente()
}


function verificaCaminhoesExistente(){
  if (document.getElementsByClassName("caminhoes").length == 0){
    document.getElementById("mensagemSemCaminhao").classList.remove("d-none")
  }
}


function verificaCarretasExistente(){
  if (document.getElementsByClassName("carretas").length == 0){
    document.getElementById("mensagemSemCarreta").classList.remove("d-none")
  }
}


function alertDel(id, elementoNome){
  Swal.fire({
    title: 'Tem certeza?',
    text: "Você não poderá reverter isso!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sim, tenho!',
  }).then((result) => {
    if (result.isConfirmed) {
      ajaxDeleteDados(id, elementoNome)
    }
  })
}


function ajaxDeleteDados(id, elementoNome){
  if (elementoNome == "caminhao"){
    dados = {
      url: "/ajax/delCaminhoes",
      "dados": id,
      "nome": "delCaminhoes",
    }
    ajaxConection(dados)
    Swal.fire(
      'Excluído!',
      'Seu Caminhão foi deletado.',
      'success',
    )
  } else if (elementoNome == "carreta") {
    dados = {
      url: "/ajax/delCarreta",
      "dados": id,
      "nome": "delCarreta",
    }
    ajaxConection(dados)
    Swal.fire(
      'Excluído!',
      'Sua Carreta foi deletada.',
      'success',
    )
  }
}


function updateCaminhao(dados){
  $('#formularioUpdateCaminhao').modal({backdrop:"static"})
  document.getElementById("idCaminhao").value = dados["id"]
  document.getElementById("inputNomeCaminhao").value = dados["nome"]
  document.getElementById("inputEixosCaminhao").value = dados["eixos"]
  document.getElementById("selectMarca").value = dados["id_marca"]
}


function updateCarreta(dados){
  $('#formularioUpdateCarreta').modal({backdrop:"static"})
  document.getElementById("idCarreta").value = dados["id"]
  document.getElementById("inputPesoMaximo").value = dados["peso_maximo"]
  document.getElementById("selectTipoCarreta").value = dados["tipoCarreta"]
  document.getElementById("selectTipoReboque").value = dados["tipoReboque"]
}


function cadastrarCaminhao(){
  $('#formularioCadastroCaminhao').modal({backdrop:"static"})
}


function cadastrarCarreta(){
  $('#formularioCadastroCarreta').modal({backdrop:"static"})
}
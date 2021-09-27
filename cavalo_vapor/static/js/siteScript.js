function mostrarInputMotivo (elemento){
  inputMotivo = document.getElementById("formGroupInputMotivo")
  if (elemento == "outro"){
    inputMotivo.classList.remove("d-none")
  } else {
    inputMotivo.classList.add("d-none")
  }
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


function deletarCaminhao(id){
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
    } else {
      Swal.fire(
        'Cancelado',
        'Operação abortada!',
        'error',
      )
    }
  })
}


function cadastrarCaminhao(){
  Swal.fire({
    title: 'Cadastre seu Caminhão',
    template: "#cadastroCaminhaoTemplate",
    showConfirmButton: false,
    showCloseButton: true,
  })
}
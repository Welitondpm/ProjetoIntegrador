function mostrarInputMotivo (elemento){
  inputMotivo = document.getElementById("formGroupInputMotivo")
  if (elemento == "outro"){
    inputMotivo.classList.remove("d-none")
  } else {
    inputMotivo.classList.add("d-none")
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


function ajaxConection(dados){
  $.ajax({
    url: dados["url"],
    data: {
      'dados': dados["dados"]
    },
    success: function(data) {
      PreencheMunicipios(data)
    }
  })
}
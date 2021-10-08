class FormDate():
  def defineForms(self):
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
      'formUpdateFilial': {
        "Name": "Atualize sua Filial",
        "Url": "templates-form/formFilial.html",
        "ButtonText": "Salvar Alterações",
        "ActionUrl": "/update/updateFilial/",
        "modalId": "formularioUpdateFilial",
        "inputId": "UpdateFilial",
      },
      'formCadastroFilial': {
        "Name": "Cadastre uma Filial",
        "Url": "templates-form/formFilial.html",
        "ButtonText": "Cadastrar Filial",
        "ActionUrl": "",
        "modalId": "formularioCadastroFilial",
        "inputId": "CadastroFilial",
      },
      'formUpdateFuncionario': {
        "Name": "Atualize sue Funcionário",
        "Url": "templates-form/formFuncionario.html",
        "ButtonText": "Salvar Alterações",
        "ActionUrl": "/update/updateFuncionario/",
        "modalId": "formularioUpdateFuncionario",
        "inputId": "UpdateFilial",
      },
      'formCadastroFuncionario': {
        "Name": "Cadastre um Funcionário",
        "Url": "templates-form/formFuncionario.html",
        "ButtonText": "Cadastrar Funcionário",
        "ActionUrl": "",
        "modalId": "formularioCadastroFuncionario",
        "inputId": "CadastroFilial",
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
    return forms

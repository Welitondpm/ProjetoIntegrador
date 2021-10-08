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


  def defineFormsLogin(self):
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
    return forms

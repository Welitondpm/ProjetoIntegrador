def verificaTamanho(text, size):
  if type(text) != str:
    return False
  return not len(text) > size


def verificaEmail(email):
  return True


def verificaTelefone(telefone):
  return True


def verificaReorganizeCep(cep):
  if len(cep) > 9 or len(cep) <= 7:
    return False, cep
  cepClean = ""
  for item in cep:
    if item in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
      cepClean += item
  if len(cepClean) != 8:
    return False, cep
  cepClean = cepClean[:5] + "-" + cepClean[5:]
  return len(cepClean) == 9, cepClean
    

def CleanStrings(cpf):
  stringClean = ""
  for item in cpf:
    if item.isdigit():
      stringClean += item
  return stringClean  


def DigitosIguais(string):
  digito = string[0]
  for item in string:
    if item != digito:
      return True
  return False


def MultiplicaDigitos(multiplicador, digitos, cpfCnpj):
  valor = 0
  for item in digitos:
    valor += int(item) * multiplicador
    multiplicador -= 1
    if multiplicador == 1:
      multiplicador = 9
  return digitos + str(CalculaDigitoVerificador(valor, cpfCnpj))


def CalculaDigitoVerificador(valor, cpfCnpj):
  if cpfCnpj == "cpf":
    valor = valor * 10 % 11
    if valor == 10:
      valor = 0
  else:
    valor = valor % 11
    if valor < 2:
      valor = 0
    else:
      valor = 11 - valor
  return int(valor)


def verificaCPF(cpf):
  cpf = CleanStrings(cpf)
  if not len(cpf) == 11:
    return False
  if not DigitosIguais(cpf):
    return False
  newCpf = cpf[:9]
  newCpf = MultiplicaDigitos(10, newCpf, cpf)
  newCpf = MultiplicaDigitos(11, newCpf, cpf)
  return newCpf == cpf


def verificaCNPJ(cnpj):
  cnpj = CleanStrings(cnpj)
  if not len(cnpj) == 14:
    return False
  if not DigitosIguais(cnpj):
    return False
  newCnpj = cnpj[:12]
  newCnpj = MultiplicaDigitos(5, newCnpj, "cnpj")
  newCnpj = MultiplicaDigitos(6, newCnpj, "cnpj")
  return newCnpj == cnpj


def OrganizaCpfCnpj(string):
  string = CleanStrings(string)
  if len(string) == 11:
    return string[:3] + "." + string[3:6] + "." + string[6:9] + "-" + string[9:]
  return string[:2] + "." + string[2:5] + "." + string[5:8] + "/" + string[8:12] + "-" + string[12:] 
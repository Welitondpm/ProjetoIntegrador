class Verificador_CPF:
    def verifica_cpf(cpf):
        cpf_clean = []
        for item in cpf:
            if item.isdigit():
                cpf_clean.append(item)
        if len(cpf_clean) != 11:
            return False

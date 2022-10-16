from validate_docbr import CPF

def cpf_valido(cpf):
    new_cpf = CPF()
    return new_cpf.validate(cpf)

def rg_valido(rg):
    return len(rg) == 9
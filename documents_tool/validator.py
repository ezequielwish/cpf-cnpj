def cpf(cpf_digits):
    try:
        raw_cpf = str(cpf_digits).replace('.', '').replace('-', '')
        if raw_cpf == 11 * raw_cpf[0]:
            return False
        new_cpf = raw_cpf[:-2]
        contador = 10
        tot = 0  # Guarda o total de cada loop
        # Loop para multiplicar cada digito do documents por 10-2
        for index, value in enumerate(new_cpf):
            temp = int(value) * contador  # Armazena dados temporáriamente
            tot += temp
            contador -= 1
        contador = 11  # redefinindo para 11 pois o proximo calculo tera 11 digitos
        dig1 = 11 - (tot % 11)
        tot = 0  # Preparando o tot para o novo loop
        if dig1 > 9:  # O dígito deve ser 0 caso o resultado seja 10 ou superior
            dig1 = 0
        new_cpf += str(dig1)  # Criando novo cpf para comparar depois
        # Loop para multiplicar os dígitos ja com o 10° dígito incluso por 11-2
        for index, value in enumerate(new_cpf):
            temp = int(value) * contador
            tot += temp
            contador -= 1
        dig2 = 11 - (tot % 11)
        if dig2 > 9:  # O dígito deve ser 0 caso o resultado seja 10 ou superior
            dig2 = 0
        new_cpf += str(dig2)
        if new_cpf == raw_cpf:
            return True
        else:
            return False
    except:
        return False


def cnpj(cnpj_digits):
    try:
        raw_cnpj = ''
        tot = 0
        for value in str(cnpj_digits):
            if value.isnumeric():
                raw_cnpj += value
        if raw_cnpj[8:12] != '0001':
            return False
        raw_cnpj = list(raw_cnpj)
        new_cnpj = raw_cnpj[:-2]
        keys_cnpj = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        new_cnpj = list(new_cnpj)
        for k, v in enumerate(new_cnpj):
            tot += int(v) * keys_cnpj[k]
        dig1 = 11 - (tot % 11)
        tot = 0
        if dig1 > 9:
            new_cnpj.append(str(0))
        else:
            new_cnpj.append(str(dig1))
        keys_cnpj.insert(0, 6)
        for k, v in enumerate(new_cnpj):
            tot += int(v) * keys_cnpj[k]
        dig2 = 11 - (tot % 11)
        if dig2 > 9:
            new_cnpj.append(str(0))
        else:
            new_cnpj.append(str(dig2))
        if new_cnpj == raw_cnpj:
            return True
        else:
            return False
    except IndexError:
        return False


def val(number):
    if len(number) == 11:
        return cpf(number)
    elif len(number) == 14:
        return cnpj(number)
    else:
        return False
        

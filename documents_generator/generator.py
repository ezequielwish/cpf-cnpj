def cpf():
    from random import randint

    while True:
        raw_cpf = str(randint(100000000, 999999999))
        contador = 10
        tot = 0
        for index, value in enumerate(raw_cpf):
            temp = int(value) * contador
            tot += temp
            contador -= 1
        contador = 11
        dig1 = 11 - (tot % 11)
        tot = 0
        if dig1 > 9:
            dig1 = 0
        raw_cpf += str(dig1)
        for index, value in enumerate(raw_cpf):
            temp = int(value) * contador
            tot += temp
            contador -= 1
        dig2 = 11 - (tot % 11)
        if dig2 > 9:
            dig2 = 0
        raw_cpf += str(dig2)
        if raw_cpf != 11 * raw_cpf[0]:
            break
    new_cpf = f'{raw_cpf[0:3]}.{raw_cpf[3:6]}.{raw_cpf[6:9]}-{raw_cpf[9:]}'
    return new_cpf


def cnpj():
    from random import randint
    while True:
        raw_cnpj = str(randint(10000000, 99999999)) + '0001'
        tot = 0
        new_cnpj = list(raw_cnpj)
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
        if raw_cnpj != len(raw_cnpj) * raw_cnpj[0]:
            break
    new_cnpj = ''.join(new_cnpj)
    new_cnpj = f'{new_cnpj[0:2]}.{new_cnpj[2:5]}.{new_cnpj[5:8]}/{new_cnpj[8:12]}-{new_cnpj[12:]}'
    return new_cnpj

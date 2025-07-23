from random import randint


def generate_cpf():
    while True:
        base = str(randint(100000000, 999999999))
        if base == base[0] * 9:
            continue

        total = sum(int(d) * w for d, w in zip(base, range(10, 1, -1)))
        digit1 = 11 - (total % 11)
        digit1 = "0" if digit1 > 9 else str(digit1)

        base += digit1
        total = sum(int(d) * w for d, w in zip(base, range(11, 1, -1)))
        digit2 = 11 - (total % 11)
        digit2 = "0" if digit2 > 9 else str(digit2)

        cpf_number = base + digit2
        if cpf_number != cpf_number[0] * 11:
            return (
                f"{cpf_number[:3]}.{cpf_number[3:6]}.{cpf_number[6:9]}-{cpf_number[9:]}"
            )


def generate_cnpj():
    while True:
        base = str(randint(10000000, 99999999)) + "0001"
        if base == base[0] * 12:
            continue

        weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        digit1 = 11 - (sum(int(d) * w for d, w in zip(base, weights1)) % 11)
        digit1 = "0" if digit1 > 9 else str(digit1)

        base += digit1
        weights2 = [6] + weights1
        digit2 = 11 - (sum(int(d) * w for d, w in zip(base, weights2)) % 11)
        digit2 = "0" if digit2 > 9 else str(digit2)

        cnpj_number = base + digit2
        return f"{cnpj_number[:2]}.{cnpj_number[2:5]}.{cnpj_number[5:8]}/{cnpj_number[8:12]}-{cnpj_number[12:]}"


def generate_document(doc_type):
    doc_type = doc_type.lower()
    if doc_type == "cpf":
        return generate_cpf()
    elif doc_type == "cnpj":
        return generate_cnpj()
    return "Only CPF or CNPJ are accepted."

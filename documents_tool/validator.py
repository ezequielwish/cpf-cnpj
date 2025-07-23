def validate_cpf(cpf_digits):
    try:
        digits = str(cpf_digits).replace(".", "").replace("-", "")
        if digits == digits[0] * 11:
            return False

        base = digits[:-2]
        total = sum(int(d) * w for d, w in zip(base, range(10, 1, -1)))
        digit1 = 11 - (total % 11)
        digit1 = "0" if digit1 > 9 else str(digit1)

        base += digit1
        total = sum(int(d) * w for d, w in zip(base, range(11, 1, -1)))
        digit2 = 11 - (total % 11)
        digit2 = "0" if digit2 > 9 else str(digit2)

        return base + digit2 == digits
    except:
        return False


def validate_cnpj(cnpj_digits):
    try:
        digits = "".join(filter(str.isdigit, str(cnpj_digits)))
        if len(digits) != 14 or digits[8:12] != "0001":
            return False

        base = digits[:-2]
        weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        total = sum(int(d) * w for d, w in zip(base, weights1))
        digit1 = 11 - (total % 11)
        digit1 = "0" if digit1 > 9 else str(digit1)

        base += digit1
        weights2 = [6] + weights1
        total = sum(int(d) * w for d, w in zip(base, weights2))
        digit2 = 11 - (total % 11)
        digit2 = "0" if digit2 > 9 else str(digit2)

        return base + digit2 == digits
    except:
        return False


def validate_document(doc_number):
    digits = "".join(filter(str.isdigit, str(doc_number)))
    if len(digits) == 11:
        return validate_cpf(digits)
    elif len(digits) == 14:
        return validate_cnpj(digits)
    return False

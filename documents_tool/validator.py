def validate_cpf(cpf_digits):
    """
    Valida um número de CPF (Cadastro de Pessoa Física) com base nos dígitos verificadores.

    O CPF possui 11 dígitos, sendo os dois últimos calculados a partir dos nove primeiros.
    A validação segue o algoritmo oficial de cálculo dos dígitos verificadores.

    Args:
        cpf_digits (str): CPF com ou sem formatação (ex: "123.456.789-09" ou "12345678909").

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """
    try:
        # Remove pontos e traços
        digits = str(cpf_digits).replace(".", "").replace("-", "")

        # Verifica se todos os dígitos são iguais (ex: "11111111111" não é válido)
        if digits == digits[0] * 11:
            return False

        # Primeiro dígito verificador
        base = digits[:-2]  # primeiros 9 dígitos
        total = sum(int(d) * w for d, w in zip(base, range(10, 1, -1)))
        digit1 = 11 - (total % 11)
        digit1 = "0" if digit1 > 9 else str(digit1)

        # Segundo dígito verificador
        base += digit1
        total = sum(int(d) * w for d, w in zip(base, range(11, 1, -1)))
        digit2 = 11 - (total % 11)
        digit2 = "0" if digit2 > 9 else str(digit2)

        # Compara os dígitos calculados com os fornecidos
        return base + digit2 == digits
    except:
        return False


def validate_cnpj(cnpj_digits):
    """
    Valida um número de CNPJ (Cadastro Nacional de Pessoa Jurídica) com base nos dígitos verificadores.

    O CNPJ possui 14 dígitos, sendo os dois últimos calculados com base nos doze primeiros.
    A validação segue o algoritmo oficial definido pela Receita Federal.

    Args:
        cnpj_digits (str): CNPJ com ou sem formatação (ex: "12.345.678/0001-95" ou "12345678000195").

    Returns:
        bool: True se o CNPJ for válido, False caso contrário.
    """
    try:
        digits = "".join(filter(str.isdigit, str(cnpj_digits)))

        # Verifica tamanho e se o CNPJ está no formato de matriz (filial 0001)
        if len(digits) != 14 or digits[8:12] != "0001":
            return False

        base = digits[:-2]  # primeiros 12 dígitos

        # Primeiro dígito verificador
        weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        total = sum(int(d) * w for d, w in zip(base, weights1))
        digit1 = 11 - (total % 11)
        digit1 = "0" if digit1 > 9 else str(digit1)

        # Segundo dígito verificador
        base += digit1
        weights2 = [6] + weights1
        total = sum(int(d) * w for d, w in zip(base, weights2))
        digit2 = 11 - (total % 11)
        digit2 = "0" if digit2 > 9 else str(digit2)

        return base + digit2 == digits
    except:
        return False


def validate_document(doc_number):
    """
    Detecta automaticamente se o documento é CPF ou CNPJ e executa a validação correspondente.

    Args:
        doc_number (str): Número do documento com ou sem formatação.

    Returns:
        bool: True se o documento for válido, False caso contrário.
    """
    digits = "".join(filter(str.isdigit, str(doc_number)))

    if len(digits) == 11:
        return validate_cpf(digits)
    elif len(digits) == 14:
        return validate_cnpj(digits)
    return False

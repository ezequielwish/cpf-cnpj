/**
 * Requisição para gerar um novo documento (CPF ou CNPJ) do tipo especificado.
 * Atualiza o campo de input e exibe o resultado.
 *
 * @param {string} type - Tipo de documento a ser gerado ("cpf" ou "cnpj").
 */
async function generateDoc(type) {
    try {
        const res = await fetch(`${baseURL}/generate/${type}`);
        const data = await res.json();
        document.getElementById("inputValue").value = data.value || "";
        showResult(`Novo ${type.toUpperCase()} gerado: ${data.value}`, "green");
    } catch (err) {
        showResult("Erro ao gerar " + type.toUpperCase(), "red");
    }
}

/**
 * Valida o conteúdo do campo de input como CPF ou CNPJ.
 * Envia a requisição para o backend e exibe se o documento é válido.
 */
async function validateDoc() {
    const rawValue = document.getElementById("inputValue").value;
    const value = rawValue.replace(/\D/g, ""); // Remove caracteres não numéricos

    if (!value) return showResult("Digite um CPF ou CNPJ", "red");

    try {
        const res = await fetch(`${baseURL}/validate`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ value }),
        });
        const data = await res.json();

        if (data.valid) {
            showResult(`${value} é válido ✅`, "green");
        } else {
            showResult(`${value} é inválido ❌`, "red");
        }
    } catch (err) {
        showResult("Erro na validação", "red");
    }
}

/**
 * Remove todos os caracteres que não são dígitos do input.
 *
 * @param {HTMLInputElement} el - Elemento input a ser sanitizado.
 */
function sanitizeInput(el) {
    el.value = el.value.replace(/\D/g, "");
}

/**
 * Exibe uma mensagem de feedback na tela com a cor correspondente.
 *
 * @param {string} msg - Mensagem a ser exibida.
 * @param {string} color - Cor do texto (ex: "green", "red").
 */
function showResult(msg, color) {
    const result = document.getElementById("result");
    result.textContent = msg;
    result.className = `text-center mt-4 font-semibold text-${color}-600`;
}

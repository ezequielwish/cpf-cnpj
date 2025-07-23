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

async function validateDoc() {
    const rawValue = document.getElementById("inputValue").value;
    const value = rawValue.replace(/\D/g, "");

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

function sanitizeInput(el) {
    el.value = el.value.replace(/\D/g, "");
}

function showResult(msg, color) {
    const result = document.getElementById("result");
    result.textContent = msg;
    result.className = `text-center mt-4 font-semibold text-${color}-600`;
}

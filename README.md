# 📄 Documents Tool API

API simples em Flask para geração e validação de documentos brasileiros (como CPF e CNPJ).

---

## 🚀 Endpoints

### `GET /`

Renderiza a página inicial da aplicação (index.html).

---

## 📷 Screenshots 

![screenshot 1](URL)

### `GET /generate/<tipo>`

Gera um novo número de documento com base no tipo informado.

- **Parâmetros de URL**:
  - `tipo` (string): Tipo do documento (ex: `cpf`, `cnpj`).

- **Exemplo de Requisição**:
  ```
  GET /generate/cpf
  ```

- **Resposta**:
  ```json
  {
    "value": "documento_gerado"
  }
  ```

---

### `POST /validate`

Valida um número de documento enviado via JSON.

- **Corpo da Requisição** (`application/json`):
  ```json
  {
    "value": "numero_do_documento"
  }
  ```

- **Exemplo de Requisição**:
  ```bash
  curl -X POST http://localhost:5000/validate        -H "Content-Type: application/json"        -d '{"value": "12345678900"}'
  ```

- **Resposta**:
  ```json
  {
    "valid": true
  }
  ```

---

## ⚙️ Requisitos

- Python 3.x
- Flask
- Módulo interno `documents_tool` contendo:
  - `generator.generate_document(tipo)`
  - `validator.validate_document(document_number)`

---

## 💡 Exemplo de uso com `curl`

### Gerar documento (CPF)

```bash
curl http://localhost:5000/generate/cpf
```

### Validar documento

```bash
curl -X POST http://localhost:5000/validate      -H "Content-Type: application/json"      -d '{"value": "12345678900"}'
```

---

## 🖥️ Execução

Para iniciar o servidor:

```bash
python app.py
```

O servidor será executado em `http://0.0.0.0:5000/`.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais ou internos.
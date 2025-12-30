from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="XGEN Mock API", version="1.0")

# -------------------------------
# API CLIENTES
# -------------------------------
@app.post("/api/clientes")
def clientes(payload: dict):
    req = payload.get("Request", {})

    if req.get("id_sap") == "0000001234":
        return {
            "Response": {
                "id_sap": "0000001234",
                "nome": "João Silva Pereira",
                "cpf": "12345678900",
                "cnpj": "",
                "uf": "SP",
                "cidade": "São Paulo"
            }
        }

    if req.get("cpf") == "98765432100":
        return {
            "Response": {
                "id_sap": "0000005678",
                "nome": "Carlos Alberto Mendes",
                "cpf": "98765432100",
                "uf": "RJ",
                "cidade": "Rio de Janeiro"
            }
        }

    if req.get("cnpj") == "12345678000195":
        return {
            "Response": {
                "id_sap": "0000009012",
                "nome": "Empresa Tecnológica Brasil LTDA",
                "cnpj": "12345678000195",
                "uf": "MG",
                "cidade": "Belo Horizonte"
            }
        }

    return JSONResponse(status_code=404, content={"error": "Cliente não encontrado"})


# -------------------------------
# API TITULOS
# -------------------------------
@app.post("/api/titulos")
def titulos(payload: dict):
    req = payload.get("Request", {})

    if req.get("id_sap") == "0000001234" and req.get("call_type") == "ABERTOS":
        return {
            "Response": {
                "docnum": "000001234567",
                "exercicio": "2024",
                "vencimento": "2024-12-31",
                "mont_ml": "15000.00",
                "dias_atraso": "0"
            }
        }

    return JSONResponse(status_code=404, content={"error": "Título não encontrado"})


# -------------------------------
# API NFSE
# -------------------------------
@app.post("/api/titulos/nfse")
def nfse(payload: dict):
    req = payload.get("Request", {})

    if req.get("docnum") == "000001234567":
        return {
            "Response": {
                "pdf_base64": "JVBERi0xLjQKJ...MOCKPDF"
            }
        }

    return JSONResponse(status_code=404, content={"error": "NFSe não encontrada"})


# -------------------------------
# API RPS
# -------------------------------
@app.post("/api/titulos/rps")
def rps(payload: dict):
    req = payload.get("Request", {})

    if req.get("docnum") == "000001234567" and req.get("item") == "001":
        return {
            "Response": {
                "pdf_base64": "JVBERi0xLjQKJ...MOCKRPS"
            }
        }

    return JSONResponse(status_code=404, content={"error": "RPS não encontrado"})

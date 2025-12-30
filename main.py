from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="XGEN Mock API",
    version="2.0",
    description="Mock completo baseado em todos os exemplos da documentação XGEN"
)

# =====================================================
# CLIENTES
# =====================================================
@app.post("/api/clientes")
def clientes(payload: dict):
    req = payload.get("Request", {})

    # ===== EXEMPLO 01 – ID SAP =====
    if req.get("id_sap") == "0000001234" and not req.get("cpf") and not req.get("cnpj"):
        return {
            "Response": {
                "id_sap": "0000001234",
                "nome": "João Silva Pereira",
                "cpf": "12345678900",
                "cnpj": "",
                "insc_est": "123.456.789.012",
                "insc_mun": "98765432",
                "uf": "SP",
                "logr": "Avenida Paulista",
                "nrp": "1500",
                "compl": "Apto 2801",
                "cidade": "São Paulo",
                "bairro": "Bela Vista",
                "cep": "01311100",
                "country": "BR",
                "fisc_dom": "N",
                "ind_sec": "C",
                "ind_sec_desc": "Comércio",
                "tdt": "01",
                "decreg": "2022-01-15",
                "Pag_metd": "TED",
                "classe_risco": "A",
                "contatos": {
                    "cont_obs": "Executivo de Contas",
                    "cont_nome": "Maria",
                    "cont_snome": "Santos",
                    "func": "Gerente",
                    "dept": "Financeiro",
                    "cont_fone": "11987654321",
                    "cont_mail": "maria.santos@empresa.com",
                    "cont_func": "Gestora de Contas"
                },
                "contatos_boleto": {
                    "contb_mail1": "cobranca@empresa.com",
                    "contb_mail2": "financeiro@empresa.com",
                    "contb_mail3": "tesouraria@empresa.com",
                    "contb_fone": "1133334444",
                    "contb_foneext": "1500",
                    "contb_ddd": "11",
                    "contb_celddd": "11",
                    "contb_cel": "987654321",
                    "data_cad": "2020-06-10",
                    "data_alt": "2024-11-20"
                }
            }
        }

    # ===== EXEMPLO 02 – CPF =====
    if req.get("cpf") == "98765432100":
        return {
            "Response": {
                "id_sap": "0000005678",
                "nome": "Carlos Alberto Mendes",
                "cpf": "98765432100",
                "cnpj": "",
                "insc_est": "456.789.123.456",
                "insc_mun": "12345678",
                "uf": "RJ",
                "logr": "Rua das Flores",
                "nrp": "250",
                "compl": "Sala 405",
                "cidade": "Rio de Janeiro",
                "bairro": "Centro",
                "cep": "20040020",
                "country": "BR",
                "fisc_dom": "S",
                "ind_sec": "S",
                "ind_sec_desc": "Serviços",
                "tdt": "02",
                "decreg": "2019-03-22",
                "Pag_metd": "BOLETO",
                "classe_risco": "B",
                "contatos": {
                    "cont_obs": "Responsável Fiscal",
                    "cont_nome": "Roberto",
                    "cont_snome": "Costa",
                    "func": "Diretor",
                    "dept": "Administrativo",
                    "cont_fone": "2198765432",
                    "cont_mail": "roberto.costa@servicos.com",
                    "cont_func": "Diretor Administrativo"
                },
                "contatos_boleto": {
                    "contb_mail1": "boletos@servicos.com",
                    "contb_mail2": "admin@servicos.com",
                    "contb_mail3": "",
                    "contb_fone": "2133334444",
                    "contb_foneext": "2000",
                    "contb_ddd": "21",
                    "contb_celddd": "21",
                    "contb_cel": "998765432",
                    "data_cad": "2018-09-05",
                    "data_alt": "2024-12-01"
                }
            }
        }

    # ===== EXEMPLO 03 – CNPJ =====
    if req.get("cnpj") == "12345678000195":
        return {
            "Response": {
                "id_sap": "0000009012",
                "nome": "Empresa Tecnológica Brasil LTDA",
                "cpf": "",
                "cnpj": "12345678000195",
                "insc_est": "789.012.345.678",
                "insc_mun": "87654321",
                "uf": "MG",
                "logr": "Avenida Getúlio Vargas",
                "nrp": "3000",
                "compl": "Bloco A - Sala 1200",
                "cidade": "Belo Horizonte",
                "bairro": "Funcionários",
                "cep": "30140071",
                "country": "BR",
                "fisc_dom": "N",
                "ind_sec": "I",
                "ind_sec_desc": "Indústria",
                "tdt": "03",
                "decreg": "2015-08-18",
                "Pag_metd": "TED",
                "classe_risco": "A",
                "contatos": {
                    "cont_obs": "Gerente Financeiro",
                    "cont_nome": "Patricia",
                    "cont_snome": "Oliveira",
                    "func": "Superintendente",
                    "dept": "Financeiro",
                    "cont_fone": "31987654321",
                    "cont_mail": "patricia.oliveira@tecbrasil.com.br",
                    "cont_func": "Superintendente Financeiro"
                },
                "contatos_boleto": {
                    "contb_mail1": "cobranca@tecbrasil.com.br",
                    "contb_mail2": "tesouraria@tecbrasil.com.br",
                    "contb_mail3": "controller@tecbrasil.com.br",
                    "contb_fone": "3133334444",
                    "contb_foneext": "5000",
                    "contb_ddd": "31",
                    "contb_celddd": "31",
                    "contb_cel": "999876543",
                    "data_cad": "2015-08-18",
                    "data_alt": "2024-10-15"
                }
            }
        }

    # ===== EXEMPLO 04 – DADOS INCOMPLETOS =====
    if req.get("id_sap") == "0000003456" and not req.get("cpf") and not req.get("cnpj"):
        return {
            "Response": {
                "id_sap": "0000003456",
                "nome": "Fernando Lima Consultoria",
                "cpf": "11122233344",
                "cnpj": "",
                "insc_est": "",
                "insc_mun": "45678901",
                "uf": "BA",
                "logr": "Rua Marques de Leão",
                "nrp": "800",
                "compl": "",
                "cidade": "Salvador",
                "bairro": "Barra",
                "cep": "42810500",
                "country": "BR",
                "fisc_dom": "N",
                "ind_sec": "S",
                "ind_sec_desc": "Serviços",
                "tdt": "01",
                "decreg": "2021-05-30",
                "Pag_metd": "BOLETO",
                "classe_risco": "C",
                "contatos": {
                    "cont_obs": "",
                    "cont_nome": "Fernando",
                    "cont_snome": "Lima",
                    "func": "Consultor",
                    "dept": "Consultoria",
                    "cont_fone": "71987654321",
                    "cont_mail": "fernando@consultoria.com.br",
                    "cont_func": "Sócio-Consultor"
                },
                "contatos_boleto": {
                    "contb_mail1": "financeiro@consultoria.com.br",
                    "contb_mail2": "",
                    "contb_mail3": "",
                    "contb_fone": "7133334444",
                    "contb_foneext": "",
                    "contb_ddd": "71",
                    "contb_celddd": "71",
                    "contb_cel": "987654321",
                    "data_cad": "2021-05-30",
                    "data_alt": "2024-09-10"
                }
            }
        }

    # ===== EXEMPLO 05 – PJ MULTINACIONAL =====
    if req.get("id_sap") == "0000008765" and not req.get("cpf") and not req.get("cnpj"):
        return {
            "Response": {
                "id_sap": "0000008765",
                "nome": "Global Solutions Corporation Brasil S/A",
                "cpf": "",
                "cnpj": "98765432000154",
                "insc_est": "234.567.890.123",
                "insc_mun": "56789012",
                "uf": "SP",
                "logr": "Avenida Brigadeiro Faria Lima",
                "nrp": "4000",
                "compl": "22º Andar",
                "cidade": "São Paulo",
                "bairro": "Itaim Bibi",
                "cep": "01451902",
                "country": "BR",
                "fisc_dom": "N",
                "ind_sec": "I",
                "ind_sec_desc": "Indústria",
                "tdt": "05",
                "decreg": "2012-02-14",
                "Pag_metd": "TED",
                "classe_risco": "A",
                "contatos": {
                    "cont_obs": "Diretor de Relações Comerciais",
                    "cont_nome": "Gustavo",
                    "cont_snome": "Barbosa",
                    "func": "Director",
                    "dept": "Financial",
                    "cont_fone": "11987654321",
                    "cont_mail": "gustavo.barbosa@globalsolutions.com.br",
                    "cont_func": "Director Financial Relations"
                },
                "contatos_boleto": {
                    "contb_mail1": "receivables@globalsolutions.com.br",
                    "contb_mail2": "treasury@globalsolutions.com.br",
                    "contb_mail3": "operations@globalsolutions.com.br",
                    "contb_fone": "1133334444",
                    "contb_foneext": "8500",
                    "contb_ddd": "11",
                    "contb_celddd": "11",
                    "contb_cel": "998765432",
                    "data_cad": "2012-02-14",
                    "data_alt": "2024-11-25"
                }
            }
        }

    # ===== EXEMPLO 06 – MÚLTIPLOS CONTATOS =====
    if req.get("id_sap") == "0000002891" and not req.get("cpf") and not req.get("cnpj"):
        return {
            "Response": {
                "id_sap": "0000002891",
                "nome": "Distribuidora de Alimentos Premium LTDA",
                "cpf": "",
                "cnpj": "45678901000123",
                "insc_est": "567.890.123.456",
                "insc_mun": "34567890",
                "uf": "SC",
                "logr": "Rua Industrial",
                "nrp": "1200",
                "compl": "Galpão 5",
                "cidade": "Blumenau",
                "bairro": "Industrial",
                "cep": "89010200",
                "country": "BR",
                "fisc_dom": "N",
                "ind_sec": "C",
                "ind_sec_desc": "Comércio",
                "tdt": "02",
                "decreg": "2018-07-20",
                "Pag_metd": "BOLETO",
                "classe_risco": "B",
                "contatos": {
                    "cont_obs": "Analista de Contas a Receber",
                    "cont_nome": "Adriana",
                    "cont_snome": "Machado",
                    "func": "Analista",
                    "dept": "Cobrança",
                    "cont_fone": "47987654321",
                    "cont_mail": "adriana.machado@alimentospremium.com.br",
                    "cont_func": "Analista Senior de Cobrança"
                },
                "contatos_boleto": {
                    "contb_mail1": "nfe@alimentospremium.com.br",
                    "contb_mail2": "boletos@alimentospremium.com.br",
                    "contb_mail3": "financeiro@alimentospremium.com.br",
                    "contb_fone": "4733334444",
                    "contb_foneext": "3000",
                    "contb_ddd": "47",
                    "contb_celddd": "47",
                    "contb_cel": "988765432",
                    "data_cad": "2018-07-20",
                    "data_alt": "2024-12-10"
                }
            }
        }

    return JSONResponse(status_code=404, content={"error": "Cliente não encontrado"})


# =====================================================
# TITULOS
# =====================================================
@app.post("/api/titulos")
def titulos(payload: dict):
    req = payload.get("Request", {})

    # ===== EXEMPLO 01 – TÍTULOS ABERTOS =====
    if req.get("id_sap") == "0000001234" and req.get("call_type") == "ABERTOS":
        return {
            "Response": {
                "lneg": "0001",
                "docnum": "000001234567",
                "exercicio": "2024",
                "contrato": "0000567890",
                "item": "001",
                "ref_num": "REF20241215001",
                "vencimento": "2024-12-31",
                "des_base": "Prestação de Serviços - Consultoria",
                "mont_ml": "15000.00",
                "docdat": "2024-12-01",
                "mot": "A",
                "desc": "Factura Normal",
                "dias_atraso": "0",
                "nfse_codver": "4.00",
                "nfse_num": "000001234",
                "rps_num": "000567",
                "docnum_sap": "0000001234",
                "nosso_num": "12345678901234567890123456",
                "xnfse": "https://sistema.com/nfse/000001234",
                "xboleto": "https://sistema.com/boleto/12345678901234567890123456",
                "sl_comercial": "João Silva",
                "rep_desc": "Gerente Regional",
                "docnum_baixa": "",
                "docdat_baixa": ""
            }
        }

    # ===== EXEMPLO 02 – TÍTULOS FECHADOS/PAGOS =====
    if req.get("id_sap") == "0000005678" and req.get("call_type") == "FECHADOS":
        return {
            "Response": {
                "lneg": "0002",
                "docnum": "000005678901",
                "exercicio": "2024",
                "contrato": "0000234567",
                "item": "001",
                "ref_num": "REF20241110002",
                "vencimento": "2024-11-25",
                "des_base": "Fornecimento de Produtos",
                "mont_ml": "8500.50",
                "docdat": "2024-11-10",
                "mot": "A",
                "desc": "Factura Normal",
                "dias_atraso": "-5",
                "nfse_codver": "4.00",
                "nfse_num": "000005678",
                "rps_num": "000234",
                "docnum_sap": "0000005678",
                "nosso_num": "98765432109876543210987654",
                "xnfse": "https://sistema.com/nfse/000005678",
                "xboleto": "https://sistema.com/boleto/98765432109876543210987654",
                "sl_comercial": "Maria Costa",
                "rep_desc": "Executiva de Contas",
                "docnum_baixa": "000005679001",
                "docdat_baixa": "2024-11-20"
            }
        }

    # ===== EXEMPLO 03 – TÍTULO COM ATRASO =====
    if req.get("id_sap") == "0000009012" and req.get("call_type") == "ABERTOS":
        return {
            "Response": {
                "lneg": "0003",
                "docnum": "000009012345",
                "exercicio": "2024",
                "contrato": "0000890123",
                "item": "002",
                "ref_num": "REF20240915003",
                "vencimento": "2024-09-30",
                "des_base": "Prestação de Serviços - Manutenção",
                "mont_ml": "22500.00",
                "docdat": "2024-09-15",
                "mot": "A",
                "desc": "Factura Normal",
                "dias_atraso": "90",
                "nfse_codver": "4.00",
                "nfse_num": "000009012",
                "rps_num": "000890",
                "docnum_sap": "0000009012",
                "nosso_num": "56789012345678901234567890",
                "xnfse": "https://sistema.com/nfse/000009012",
                "xboleto": "https://sistema.com/boleto/56789012345678901234567890",
                "sl_comercial": "Patricia Silva",
                "rep_desc": "Supervisora de Vendas",
                "docnum_baixa": "",
                "docdat_baixa": ""
            }
        }

    # ===== EXEMPLO 04 – MÚLTIPLOS TÍTULOS =====
    if req.get("id_sap") == "0000003456" and req.get("call_type") == "TODOS":
        return {
            "Response": [
                {
                    "lneg": "0001",
                    "docnum": "000003456789",
                    "exercicio": "2024",
                    "contrato": "0000345678",
                    "item": "001",
                    "ref_num": "REF20241120004",
                    "vencimento": "2024-12-10",
                    "des_base": "Consultoria Estratégica",
                    "mont_ml": "5000.00",
                    "docdat": "2024-11-20",
                    "mot": "A",
                    "desc": "Factura Normal",
                    "dias_atraso": "0",
                    "nfse_codver": "4.00",
                    "nfse_num": "000003456",
                    "rps_num": "000345",
                    "docnum_sap": "0000003456",
                    "nosso_num": "34567890123456789012345678",
                    "xnfse": "https://sistema.com/nfse/000003456",
                    "xboleto": "https://sistema.com/boleto/34567890123456789012345678",
                    "sl_comercial": "Fernando Lima",
                    "rep_desc": "Gerente de Desenvolvimento",
                    "docnum_baixa": "",
                    "docdat_baixa": ""
                },
                {
                    "lneg": "0001",
                    "docnum": "000003456790",
                    "exercicio": "2024",
                    "contrato": "0000345679",
                    "item": "002",
                    "ref_num": "REF20241105005",
                    "vencimento": "2024-11-30",
                    "des_base": "Auditoria e Assessoria",
                    "mont_ml": "3500.00",
                    "docdat": "2024-11-05",
                    "mot": "A",
                    "desc": "Factura Normal",
                    "dias_atraso": "0",
                    "nfse_codver": "4.00",
                    "nfse_num": "000003457",
                    "rps_num": "000346",
                    "docnum_sap": "0000003456",
                    "nosso_num": "45678901234567890123456789",
                    "xnfse": "https://sistema.com/nfse/000003457",
                    "xboleto": "https://sistema.com/boleto/45678901234567890123456789",
                    "sl_comercial": "Fernando Lima",
                    "rep_desc": "Gerente de Desenvolvimento",
                    "docnum_baixa": "",
                    "docdat_baixa": ""
                }
            ]
        }

    # ===== EXEMPLO 05 – TÍTULO CANCELADO =====
    if req.get("id_sap") == "0000002891" and req.get("call_type") == "ABERTOS":
        return {
            "Response": {
                "lneg": "0005",
                "docnum": "000002891567",
                "exercicio": "2024",
                "contrato": "0000289156",
                "item": "001",
                "ref_num": "REF20241001006",
                "vencimento": "2024-10-30",
                "des_base": "Fornecimento de Materiais",
                "mont_ml": "12000.00",
                "docdat": "2024-10-01",
                "mot": "C",
                "desc": "Cancelado",
                "dias_atraso": "0",
                "nfse_codver": "4.00",
                "nfse_num": "000002891",
                "rps_num": "000289",
                "docnum_sap": "0000002891",
                "nosso_num": "78901234567890123456789012",
                "xnfse": "https://sistema.com/nfse/000002891",
                "xboleto": "https://sistema.com/boleto/78901234567890123456789012",
                "sl_comercial": "Adriana Machado",
                "rep_desc": "Coordenadora de Vendas",
                "docnum_baixa": "000002891001",
                "docdat_baixa": "2024-10-05"
            }
        }

    # ===== EXEMPLO 06 – TÍTULO COM JUROS E MULTA =====
    if req.get("id_sap") == "0000008765" and req.get("call_type") == "ABERTOS":
        return {
            "Response": {
                "lneg": "0006",
                "docnum": "000008765432",
                "exercicio": "2024",
                "contrato": "0000876543",
                "item": "001",
                "ref_num": "REF20240820007",
                "vencimento": "2024-08-31",
                "des_base": "Serviços Especializados",
                "mont_ml": "35000.00",
                "docdat": "2024-08-20",
                "mot": "A",
                "desc": "Factura Normal - Com Juros e Multa",
                "dias_atraso": "120",
                "nfse_codver": "4.00",
                "nfse_num": "000008765",
                "rps_num": "000876",
                "docnum_sap": "0000008765",
                "nosso_num": "23456789012345678901234567",
                "xnfse": "https://sistema.com/nfse/000008765",
                "xboleto": "https://sistema.com/boleto/23456789012345678901234567",
                "sl_comercial": "Gustavo Barbosa",
                "rep_desc": "Diretor Executivo",
                "docnum_baixa": "",
                "docdat_baixa": ""
            }
        }

    # ===== EXEMPLO 07 – TÍTULO COM PARCELA =====
    if req.get("id_sap") == "0000001234" and req.get("call_type") == "ABERTOS" and req.get("item") == "001":
        return {
            "Response": {
                "lneg": "0007",
                "docnum": "000001234568",
                "exercicio": "2024",
                "contrato": "0000567891",
                "item": "001",
                "ref_num": "REF20241201001-P1",
                "vencimento": "2025-01-10",
                "des_base": "Prestação de Serviços em Parcelas",
                "mont_ml": "5000.00",
                "docdat": "2024-12-01",
                "mot": "A",
                "desc": "Factura Parcelada 1/3",
                "dias_atraso": "0",
                "nfse_codver": "4.00",
                "nfse_num": "000001235",
                "rps_num": "000568",
                "docnum_sap": "0000001234",
                "nosso_num": "12345678901234567890123456",
                "xnfse": "https://sistema.com/nfse/000001235",
                "xboleto": "https://sistema.com/boleto/12345678901234567890123456",
                "sl_comercial": "João Silva",
                "rep_desc": "Gerente Regional",
                "docnum_baixa": "",
                "docdat_baixa": ""
            }
        }

    return JSONResponse(status_code=404, content={"error": "Título não encontrado"})


# =====================================================
# NFSE
# =====================================================
@app.post("/api/titulos/nfse")
def nfse(payload: dict):
    req = payload.get("Request", {})

    # ===== EXEMPLO 01 – NFSE BÁSICA =====
    if req.get("docnum") == "000001234567" and exercicio == "2024":
        return {
            "Response": {
                "docnum": "000001234567",
                "exercicio": "2024",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDQ0Nj4+CnN0cmVhbQpCVAowIDAgVGQKL0YxIDEyIFRmCjI1IDcyNSBUZAooTm90YSBGaXNjYWwgZGUgU2Vydmnfv28gRWxldHLDtG5pY2EpIFRqCkVUCmVuZHN0cmVhbQpFbmRvYgoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzQgMDAwMDAgbiAKMDAwMDAwMDE3MiAwMDAwMCBuIAowMDAwMDAwMzM1IDAwMDAwIG4gCjAwMDAwMDA0MTEgMDAwMDAgbiAKdHJhaWxlcgo8PC9TaXplIDYgL1Jvb3QgMSAwIFI+PgpzdGFydHhyZWYKOTA4CiUlRU9G"
            }
        }

    # ===== EXEMPLO 02 – NFSE COM DESCRIÇÃO DETALHADA =====
    if req.get("docnum") == "000005678901" and exercicio == "2024":
        return {
            "Response": {
                "docnum": "000005678901",
                "exercicio": "2024",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDU1MD4zPj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTIgVGYKMjUgNzI1IFRkCihGb3JuZWNpbWVudG8gZGUgUHJvZHV0b3MgRmluYWxpemFkb3MpIFRqCihQcmVzdGHDp8OjbyBkZSBTZXJ2acOnb3MgRXNwZWNpYWxpemFkb3MpIFRqCihEZXNjcmnDp8OjbyBEZXRhbGhhZGEgZGEgUHJlc3Rhw6fDo28pIFRqCkVUCmVuZHN0cmVhbQpFbmRvYgoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzQgMDAwMDAgbiAKMDAwMDAwMDE3MiAwMDAwMCBuIAowMDAwMDAwMzM1IDAwMDAwIG4gCjAwMDAwMDA0MTEgMDAwMDAgbiAKdHJhaWxlcgo8PC9TaXplIDYgL1Jvb3QgMSAwIFI+PgpzdGFydHhyZWYKNTU1ODAKJSVFT0Y="
            }
        }

    # ===== EXEMPLO 03 – NFSE EMITIDA COM SUCESSO =====
    if req.get("docnum") == "000009012345" and exercicio == "2024":
        return {
            "Response": {
                "docnum": "000009012345",
                "exercicio": "2024",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDU5OTg4Pj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTQgVGYKMjAgNzIwIFRkCihOb3RhIEZpc2NhbCBkZSBTZXJ2acOnbyBFbGV0csO0bmljYSkgVGoKKFByZXN0YcOnw6NvIGRlIFNlcnbDrcMs)IFRqCihTdHJ1dHVyYSBDb21wbGV0YSBkYSBORlNlIENvbSBUb2RvcyBvcyBEYWRvcyBQcmVlbmNoaWRvcykgVGoKRVQKZW5kc3RyZWFtCkVuZG9iCnhyZWYKMCA2CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxMCAwMDAwMCBuIAowMDAwMDAwMDc0IDAwMDAwIG4gCjAwMDAwMDAxNzIgMDAwMDAgbiAKMDAwMDAwMDMzNSAwMDAwMCBuIAowMDAwMDAwNDExIDAwMDAwIG4gCnRyYWlsZXIKPDwvU2l6ZSA2IC9Sb290IDEgMCBSPj4Kc3RhcnR4cmVmCjU5OTk0CiUlRU9G"
            }
        }

    # ===== EXEMPLO 04 – NFSE COM RETENÇÃO =====
    if req.get("docnum") == "000003456789" and exercicio == "2024":
        return {
            "Response": {
                "docnum": "000003456789",
                "exercicio": "2024",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDQyMzQ1Pj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTIgVGYKMjUgNzI1IFRkCihDb25zdWx0b3JpYSBFc3RyYXTDqmdpY2EpIFRqCihDb20gRGVzY29udG8gZSBSZXRlbsOnw6NvKSBUagooUmV0ZW7Dg28gSVIgUlM6IDE1MCkgVGoKRVQKZW5kc3RyZWFtCkVuZG9iCnhyZWYKMCA2CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxMCAwMDAwMCBuIAowMDAwMDAwMDc0IDAwMDAwIG4gCjAwMDAwMDAxNzIgMDAwMDAgbiAKMDAwMDAwMDMzNSAwMDAwMCBuIAowMDAwMDAwNDExIDAwMDAwIG4gCnRyYWlsZXIKPDwvU2l6ZSA2IC9Sb290IDEgMCBSPj4Kc3RhcnR4cmVmCjQyMzQ3CiUlRU9G"
            }
        }

    # ===== EXEMPLO 05 – NFSE CANCELADA =====
    if req.get("docnum") == "000002891567" and exercicio == "2024":
        return {
            "Response": {
                "docnum": "000002891567",
                "exercicio": "2024",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDQ0NTEyPj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTYgVGYKMjAgNzIwIFRkCihOb3RhIEZpc2NhbCBkZSBTZXJ2acOnbyBFbGV0csO0bmljYSAtIENBTkNFTEFEQSkgVGoKKERvY3VtZW50byBDYW5jZWxhZG8gZW0gMDUvMTAvMjAyNCkgVGoKRVQKZW5kc3RyZWFtCkVuZG9iCnhyZWYKMCA2CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxMCAwMDAwMCBuIAowMDAwMDAwMDc0IDAwMDAwIG4gCjAwMDAwMDAxNzIgMDAwMDAgbiAKMDAwMDAwMDMzNSAwMDAwMCBuIAowMDAwMDAwNDExIDAwMDAwIG4gCnRyYWlsZXIKPDwvU2l6ZSA2IC9Sb290IDEgMCBSPj4Kc3RhcnR4cmVmCjQ0NTE0CiUlRU9G"
            }
        }

    # ===== EXEMPLO 06 – NFSE COMPLEMENTAR =====
    if req.get("docnum") == "000008765432" and exercicio == "2024":
        return {
            "Response": {
                "docnum": "000008765432",
                "exercicio": "2024",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDUzMjE0Pj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTQgVGYKMjAgNzIwIFRkCihOb3RhIEZpc2NhbCBkZSBTZXJ2acOnbyBFbGV0csO0bmljYSAtIENPTVBMRU1FTlRBUikgVGoKKEF1bWVudGEgbyB2YWxvciogZGEgc2VydmnDp28pIFRqCihSZWYgQ0JPOiBSZWYyMDI0MDUwMzEwMDcpIFRqCkVUCmVuZHN0cmVhbQpFbmRvYgoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzQgMDAwMDAgbiAKMDAwMDAwMDE3MiAwMDAwMCBuIAowMDAwMDAwMzM1IDAwMDAwIG4gCjAwMDAwMDA0MTEgMDAwMDAgbiAKdHJhaWxlcgo8PC9TaXplIDYgL1Jvb3QgMSAwIFI+PgpzdGFydHhyZWYKNTMyMTYKJSVFT0Y="
            }
        }

    # ===== EXEMPLO 07 – NFSE DE GRANDE VOLUME =====
    if req.get("docnum") == "000001234568" and exercicio == "2024":
        return {
            "Response": {
                "docnum": "000001234568",
                "exercicio": "2024",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDEwNDUzMjI+Pg0Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTIgVGYKMjUgNzI1IFRkCihQcmVzdGHDp8OjbyBkZSBTZXJ2acOnbyBFc3BlY2lhbGl6YWRvIEVtQWx0YSBWb2x1bWUpIFRqCihQb3J0YXJpYSBkZSBQcmVzdGHDp8OjbyBkaXNwb25pw410ZWwpIFRqCihTZXJ2acOnb3MgRW0gUGVyw410ZWwoIFRqCkVUCmVuZHN0cmVhbQpFbmRvYgoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzQgMDAwMDAgbiAKMDAwMDAwMDE3MiAwMDAwMCBuIAowMDAwMDAwMzM1IDAwMDAwIG4gCjAwMDAwMDA0MTEgMDAwMDAgbiAKdHJhaWxlcgo8PC9TaXplIDYgL1Jvb3QgMSAwIFI+PgpzdGFydHhyZWYKMTA0NTMyNCUlRU9G"
            }
        }

    return JSONResponse(status_code=404, content={"error": "NFSe não encontrada"})


# =====================================================
# RPS
# =====================================================
@app.post("/api/titulos/rps")
def rps(payload: dict):
    req = payload.get("Request", {})

    # ===== EXEMPLO 01 – RPS SIMPLES =====
    if req.get("docnum") == "000001234567" and req.get("item") == "001" and req.get("exercicio") == "2024":
        return {
            "Response": {
                "docnum": "000001234567",
                "exercicio": "2024",
                "item": "001",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDM0NTI+Pg0Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTQgVGYKMjAgNzIwIFRkCihSRUNJQk8gUFJPVklTw5NPIERFIFNFUVYK0kIKKERvY3VtZW50byBQcm92acOzcsKvbyBQYXJhIEVtaXNzw6NvIGRlIE5Gc2UpIFRqCkVUCmVuZHN0cmVhbQpFbmRvYgoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzQgMDAwMDAgbiAKMDAwMDAwMDE3MiAwMDAwMCBuIAowMDAwMDAwMzM1IDAwMDAwIG4gCjAwMDAwMDA0MTEgMDAwMDAgbiAKdHJhaWxlcgo8PC9TaXplIDYgL1Jvb3QgMSAwIFI+PgpzdGFydHhyZWYKMzQ1NAolJUVPRg=="
            }
        }

    # ===== EXEMPLO 02 – RPS COM VALOR ALTO =====
    if req.get("docnum") == "000005678901" and req.get("item") == "001" and req.get("exercicio") == "2024":
        return {
            "Response": {
                "docnum": "000005678901",
                "exercicio": "2024",
                "item": "001",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDQwMTIyPj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTQgVGYKMjAgNzIwIFRkCihSRUNJQk8gUFJPVklTw5NPIERFIFNFUVYK0kIKKFZhbG9yIEFsdG8gUGFyYSBFbWlzc8OjbyBkZSBORlNlIikgVGoKKFRvdGFsIFIkIDguNTAwLDUwKSBUagooQWxPv2Zvcm5lY2ltZW50byBkZSBQcm9kdXRvcykgVGoKRVQKZW5kc3RyZWFtCkVuZG9iCnhyZWYKMCA2CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxMCAwMDAwMCBuIAowMDAwMDAwMDc0IDAwMDAwIG4gCjAwMDAwMDAxNzIgMDAwMDAgbiAKMDAwMDAwMDMzNSAwMDAwMCBuIAowMDAwMDAwNDExIDAwMDAwIG4gCnRyYWlsZXIKPDwvU2l6ZSA2IC9Sb290IDEgMCBSPj4Kc3RhcnR4cmVmCjQwMTI0CiUlRU9G"
            }
        }

    # ===== EXEMPLO 03 – RPS COM MÚLTIPLOS ITENS =====
    if req.get("docnum") == "000009012345" and req.get("item") == "001" and req.get("exercicio") == "2024":
        return {
            "Response": {
                "docnum": "000009012345",
                "exercicio": "2024",
                "item": "001",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDU0MzIxPj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTIgVGYKMjUgNzI1IFRkCihSUFMgQ29tIE3DAXRpcGxvcyBJdGVucykgVGoKKEl0ZW0gMDAxIC0gU2VydmnDp28gQSkgVGoKKEl0ZW0gMDAyIC0gU2VydmnDp28gQikgVGoKKEl0ZW0gMDAzIC0gU2VydmnDp28gQykgVGoKRVQKZW5kc3RyZWFtCkVuZG9iCnhyZWYKMCA2CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxMCAwMDAwMCBuIAowMDAwMDAwMDc0IDAwMDAwIG4gCjAwMDAwMDAxNzIgMDAwMDAgbiAKMDAwMDAwMDMzNSAwMDAwMCBuIAowMDAwMDAwNDExIDAwMDAwIG4gCnRyYWlsZXIKPDwvU2l6ZSA2IC9Sb290IDEgMCBSPj4Kc3RhcnR4cmVmCjU0MzIzCiUlRU9G"
            }
        }

    # ===== EXEMPLO 04 – RPS PARA SERVIÇO NÃO TRIBUTÁVEL =====
    if req.get("docnum") == "000003456789" and req.get("item") == "001" and req.get("exercicio") == "2024":
        return {
            "Response": {
                "docnum": "000003456789",
                "exercicio": "2024",
                "item": "001",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDMyNTQyPj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTQgVGYKMjAgNzIwIFRkCihSRUNJQk8gUFJPVklTw5NPIERFIFNFUVYK0kIKKFNlcnbDrcOs8qBvIE7Dg28gVHJpYnV0w6F2ZWwpIFRqCihDb25zdWx0b3JpYSBFc3RyYXTDqmdpY2EpIFRqCihOYW8gSW1wb3N0YSBJUiBlIENzdCBDb21lY2lhbCkgVGoKRVQKZW5kc3RyZWFtCkVuZG9iCnhyZWYKMCA2CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxMCAwMDAwMCBuIAowMDAwMDAwMDc0IDAwMDAwIG4gCjAwMDAwMDAxNzIgMDAwMDAgbiAKMDAwMDAwMDMzNSAwMDAwMCBuIAowMDAwMDAwNDExIDAwMDAwIG4gCnRyYWlsZXIKPDwvU2l6ZSA2IC9Sb290IDEgMCBSPj4Kc3RhcnR4cmVmCjMyNTQ0CiUlRU9G"
            }
        }

    # ===== EXEMPLO 05 – RPS COM DESCONTO =====
    if req.get("docnum") == "000002891567" and req.get("item") == "001" and req.get("exercicio") == "2024":
        return {
            "Response": {
                "docnum": "000002891567",
                "exercicio": "2024",
                "item": "001",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDM1NjEyPj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTIgVGYKMjUgNzI1IFRkCihSUFMgQ29tIERlc2NvbnRvIEFwbGljYWRvKSBUagooQ8OkbGN1bG8gZGUgRGVzY29udG8gUHJvZ3Jlc3NpdG8pIFRqCihEZXNjb250bzogUiQgMS4yMDAsMDApIFRqCihUb3RhbCBDb20gRGVzY29udG8gUiQgMTAuODAwLDAwKSBUago pFVQKZW5kc3RyZWFtCkVuZG9iCnhyZWYKMCA2CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxMCAwMDAwMCBuIAowMDAwMDAwMDc0IDAwMDAwIG4gCjAwMDAwMDAxNzIgMDAwMDAgbiAKMDAwMDAwMDMzNSAwMDAwMCBuIAowMDAwMDAwNDExIDAwMDAwIG4gCnRyYWlsZXIKPDwvU2l6ZSA2IC9Sb290IDEgMCBSPj4Kc3RhcnR4cmVmCjM1NjE0CiUlRU9G"
            }
        }

    # ===== EXEMPLO 06 – RPS RETIFICADO =====
    if req.get("docnum") == "000008765432" and req.get("item") == "001" and req.get("exercicio") == "2024":
        return {
            "Response": {
                "docnum": "000008765432",
                "exercicio": "2024",
                "item": "001",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDQ4MzIxPj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTQgVGYKMjAgNzIwIFRkCihSRUNJQk8gUFJPVklTw5NPIERFIFNFUVYK0kIKKFJFVElGSUNBRE8pIFRqCihSUFMgQ29ycmlnaWRvIGUgUmVBanVzdGFkbykgVGoKKFJQUyBPcmlnaW5hbDogUlA0LzIwMjQpIFRqCihSUFMgUmV0aWZpY2FkYTogUlA2LzIwMjQpIFRqCkVUCmVuZHN0cmVhbQpFbmRvYgoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzQgMDAwMDAgbiAKMDAwMDAwMDE3MiAwMDAwMCBuIAowMDAwMDAwMzM1IDAwMDAwIG4gCjAwMDAwMDA0MTEgMDAwMDAgbiAKdHJhaWxlcgo8PC9TaXplIDYgL1Jvb3QgMSAwIFI+PgpzdGFydHhyZWYKNDgzMjMKJSVFT0Y="
            }
        }

    # ===== EXEMPLO 07 – RPS COM RETENÇÃO =====
    if req.get("docnum") == "000001234568" and req.get("item") == "001" and req.get("exercicio") == "2024":
        return {
            "Response": {
                "docnum": "000001234568",
                "exercicio": "2024",
                "item": "001",
                "pdf_base64": "JVBERi0xLjQKJeLjz9MNCjEgMCBvYmoKPDwvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFI+PgplbmRvYgoKMiAwIG9iago8PC9UeXBlIC9QYWdlcyAvS2lkcyBbMyAwIFJdIC9Db3VudCAxPj4KZW5kb2IKCjMgMCBvYmoKPDwvVHlwZSAvUGFnZSAvUGFyZW50IDIgMCBSIC9SZXNvdXJjZXMgPDwvRm9udCA8PC9GMSA0IDAgUj4+Pj4gL01lZGlhQm94IFswIDAgNjEyIDc5Ml0gL0NvbnRlbnRzIDUgMCBSPj4KZW5kb2IKCjQgMCBvYmoKPDwvVHlwZSAvRm9udCAvU3VidHlwZSAvVHlwZTEgL0Jhc2VGb250IC9IZWxtdmV0aWNhPj4KZW5kb2IKCjUgMCBvYmoKPDwvTGVuZ3RoIDUzMjEyPj4Kc3RyZWFtCkJUCjAgMCBUZAovRjEgMTIgVGYKMjUgNzI1IFRkCihSUFMgQ29tIFJldGVuw6fDo28gRmlzY2FsKSBUagooSVIgUmV0aWRvIFZhbG9yOiBSJCAzLjAwMCkgVGoKKENTVCBSZXRpZG8gVmFsb3I6IFIkIDQ1MCkgVGoKKElRVEYgUmV0aWRvOiBSJCAxMDApIFRqCkVUCmVuZHN0cmVhbQpFbmRvYgoKeHJlZgowIDYKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDEwIDAwMDAwIG4gCjAwMDAwMDAwNzQgMDAwMDAgbiAKMDAwMDAwMDE3MiAwMDAwMCBuIAowMDAwMDAwMzM1IDAwMDAwIG4gCjAwMDAwMDA0MTEgMDAwMDAgbiAKdHJhaWxlcgo8PC9TaXplIDYgL1Jvb3QgMSAwIFI+PgpzdGFydHhyZWYKNTMyMTQKJSVFT0Y="
            }
        }

    return JSONResponse(status_code=404, content={"error": "RPS não encontrado"})


# =====================================================
# HEALTH CHECK
# =====================================================
@app.get("/health")
def health():
    return {"status": "OK", "message": "API XGEN Mock v2.0 em funcionamento"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

def get_header():
    return{
        'Authorization': 'Bearer ' + get_token_sts()['access_token'],
        'credenciais': 'Teste'
    }

def consultar_cliente_eq3(cpf_cnpj):
    try:
        params={
            "tipo_consulta": "exata",
            "tipo_pessoa": "pj",
            "numero_documento": cpf_cnpj
        }
        url = os.getenv("URL_EQ3")
        header = get_header()
        response = requests.get(url, headers=header, params=params, verify='./ca_bundle.crt')

        return response.json()
    except Exception as e:
        logger.error("LOG ERRO")
        raise BusinessException(str(e))

def consultar_cliente_id_eq3(id_cliente):
    try:
        url = os.getenv("URL_EQ3_ID").replace("{id_cliente}", id_cliente)
        header = get_header()
        response = request.get(url, headers=header, verify='./ca_bundle.crt')

        return response.json()
    except Exception as e:
        logger.error("LOG ERRO")
        raise BusinessException(str(e))
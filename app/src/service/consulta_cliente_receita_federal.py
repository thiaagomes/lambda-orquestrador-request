def get_header():
    return{
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': 'Bearer ' + get_token_sts()['access_token'],
        'credenciais': 'Teste'
    }


def consulta_cliente_receita_federal_hw(cpf_cnpj):
    try:
        url = os.getenv("URL_HW").replace("{cpf_cnpj}", cpf_cnpj)

        header = get_header()
        response = request.get(url, headers=header, verify='./ca_bundle.crt')

        return response.json()
    except Exception as e:
        logger.error("LOG ERRO")
        raise BusinessException(str(e))
def get_header():
    return{
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': 'Bearer ' + get_token_sts()['access_token'],
        'credenciais': 'Teste'
    }

def consulta_contas_cc(id_cliente):
    try:
        url = os.getenv("URL_CC").replace("{id_cliente}", id_cliente)

        header = get_header()
        response = request.get(url, headers=header, verify='./ca_bundle.crt')

        return response.json()
    except Exception as e:
        logger.error("LOG ERRO")
        raise BusinessException(str(e))


def consulta_agencia_conta_cc(id_conta):
    try:
        url = os.getenv("URL_CONTA").replace("{id_conta}", id_conta)

        header = get_header()
        response = request.get(url, headers=header, verify='./ca_bundle.crt')

        return response.json()
    except Exception as e:
        logger.error("LOG ERRO")
        raise BusinessException(str(e))
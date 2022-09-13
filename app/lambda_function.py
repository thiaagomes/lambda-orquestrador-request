def lambda_handler(event, context):
    try:
        if 'queryStringParameters' in event:
            query = event['queryStringParameters']
        else:
            raise BusinessException("Erro! Chamada sem queryStringParameters")
        
        orquestrador = OrquestradorChamada()

        if 'cpf_cnpj' in query and query['cpf_cnpj'] != "" and query['cpf_cnpj'] is not None:
            return orquestrador.consulta_cpf_cnpj(query['cpf_cnpj'])
        
        if 'id_conta' in query and query['id_conta'] != "" and query['id_conta'] is not None:
            return orquestrador.consulta_cpf_cnpj(query['id_conta'])
        
        if 'id_cliente' in query and query['id_cliente'] != "" and query['id_cliente'] is not None:
            return orquestrador.consulta_cpf_cnpj(query['id_cliente'])
        
        raise BusinessException("Error na validacao de atributos")

    except Exception as e:
        logger.error("Ocorreu um erro ao receber os valores do Gateway")
        raise BusinessException(str(e))


# if __name__=="__main__":
#     lambda_handler(get_payload_gateway(), None)
        
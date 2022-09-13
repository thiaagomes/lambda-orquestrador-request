class OrquestradorChamadas():

    def consulta_cpf_cnpj(self, cpf_cnpj):
        try:
            response = consultar_cliente_eq3(cpf_cnpj)
            id_cliente = response['data']['id_cliente']
            response_cc = consulta_contas_cc(id_cliente)
            response['consulta_cc'] = response_cc
            response_hw = consulta_cliente_receita_federal_hw(cpf_cnpj)
            response['consulta_hw'] = response_hw

            return {
                "statusCode": 200,
                "body": json.dumps(response)
            }
        except Exception as e:
            logger.error("Ocorreu um erro ao executar a orquestracao")


    def consulta_conta_id_conta(self, id_conta):
        try:
            response = consulta_agencia_conta_cc(id_conta)
            id_cliente = response['data'][0]['numero_unico_cliente']
            response_eq3 = consultar_cliente_id_eq3(id_cliente)
            response['consulta_eq3'] = response_eq3
            response_hw = consulta_cliente_receita_federal_hw(cpf_cnpj)
            response['consulta_hw'] = response_hw

            return {
                "statusCode": 200,
                "body": json.dumps(response)
            }
        except Exception as e:
            logger.error("Ocorreu um erro ao executar a orquestracao")

    
    def consulta_id_cliente(self, id_conta):
        try:
            response = consulta_cliente_id_eq3(id_cliente)
            cpf_cnpj = response['data']['cpf_cnpj']
            response_cc = consultar_contas_cc(id_cliente)
            response['consulta_cc'] = response_cc
            response_hw = consulta_cliente_receita_federal_hw(cpf_cnpj)
            response['consulta_hw'] = response_hw

            return {
                "statusCode": 200,
                "body": json.dumps(response)
            }
        except Exception as e:
            logger.error("Ocorreu um erro ao executar a orquestracao")
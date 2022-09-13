from unittest import TestCase, mock
from urllib import response


@mock.patch.dict(os.environ, {
    'STS_CLIENT_ID':'teste',
    'STS_CLIENT_SECRET': 'teste',
    'URL_EQ3': 'https:xpto'
})

class ConsultaClienteEQ3Test(TestCase):

    @response.activate
    def test_busca_eq3_sucesso(self):
        response.add(responses.POST, 'http://sts.test.br',
        json={
            'access_token': 'meu_token',
            'token_type': 'Bearer '
        }, status=200)

        response.add(response.GET, "https:xpto", json={'content': None}, status=200)

        response = consultar_cliente_eq3(cpf_cnpj='12345678910')
        assert response == {'content': None}

    @reponse.activate
    def test_busca_eq3_falha(self):
        response.add(responses.POST, 'http://sts.test.br',
        json={
            'access_token': 'meu_token',
            'token_type': 'Bearer '
        }, status=200)

        responses.add(responses.GET, "https:xpto", json={'content': None}, status=400)

        with pytest.raises(BusinessException):
            consultar_cliente_eq3(cpf_cnpj='12345678910')
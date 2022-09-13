@mock.patch.dict(os.environ, {
    'STS_CLIENT_ID':'teste',
    'STS_CLIENT_SECRET': 'teste',
    'URL_EQ3': 'https:xpto'
})

class TestToken:

    @responses.activate
    def test_token_fail(self):
        responses.add(responses.POST, 'http://sts.test.br', json={'content': 'Erro ao gerar token'}, status=400)

        with pytest.raises(Exception, match='Chamada ao STS retornou 400'):
            get_token_sts()

    
    @responses.activate
    def test_get_token_fail_json(self):
        responses.add(responses.POST, 'http://sts.test.br', json=None, status=200)

        with pytest.raises(Exception, match='JSON retornado invalido: b'' '):
            get_token_sts()


    @responses.activate
    def test_get_token_sucess(self):
        responses.add(responses.POST, 'http://sts.test.br',json={'access_token': 'meu_token','token_type':''}, status=200)

        assert get_token_sts()['access_token']=='meu_token'

    def test_get_secret_sucess(self):
        assert get_secret() == 'testing'

    @mock.patch.dict(os.environ, {'STS_CLIENT_SECRET': ''})
    @patch('src.utils.token_utils.boto3.session.Session')
    def test_get_secret_sem_credencial(self, mock_session_class):
        mock_session_object = mock.Mock()
        mock_client = mock.Mock()
        mock_client.get_secret_value.return_value = {"SecretString": json.dumps({"client_secret": "teste"})}
        mock_session_object.client.return_value = mock_client
        mock_session_class.return_value = mock_session_object
        assert get_secret() == 'teste'

    

    
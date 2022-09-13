def get_token_sts():
    client_secret = get_secret()

    data = {
        'client_id': os.getenv('STS_CLIENT_ID')
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    result = requests.post(os.getenv('STS_URL'), data=data, verify='./certificado')

    if result.status_code != 200:
        print(f'Chamada ao STS retornou {result.status_code}. ' f'Body{result.content}')
        raise Exception(f'Cahamda ao STS retornou {result.status_code}')
    
    try:
        return result.json()
    except Exception as e:
        print(e)
        raise Exception(f'JSON retorno invalido: {result.content}')

def get_secret():
    secret = os.getenv('STS_CLIENT_SECRET')
    if secret is not None and secret != '':
        return secret

    secret_name = os.getenv('CREDENTIALS')
    region_name = "sa-east-1"
    #Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        response = client.get_secret_value(
            SecretId=secret_name
        )

        if 'SecretsString' in response:
            secret = json.loads(response['SecretsString'])['client_secret']
        else:
            secret = json.loads(base64.b64decode(response['SecretBinary']))['client_secret']

        os.environ['STS_CLIENT_SECRET'] = secret
        return secret
    
    except Exception as e:
        raise e
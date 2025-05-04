import os
from pprint import pprint
from elasticsearch import Elasticsearch


ES_HOME=os.environ['ES_HOME']
cert_path='/config/certs/http_ca.crt'

ELASTIC_PASSWORD = 'PG_goG*Q7q_2u+pcKdlu'

# Create the client instance of Elasticsearch 9.0.0
es = Elasticsearch(
    'https://localhost:9200',
    ca_certs=f'{ES_HOME}{cert_path}',
    basic_auth=('elastic', ELASTIC_PASSWORD)
)

client_info=es.info()
print('Connected to Elasticsearch')
pprint(client_info.body)



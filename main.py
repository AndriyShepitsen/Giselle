import os
from pprint import pprint
from elasticsearch import Elasticsearch


ES_HOME=os.environ['ES_HOME']
cert_path='/config/certs/http_ca.crt'

ELASTIC_PASSWORD = 'PG_goG*Q7q_2u+pcKdlu'

# Create the client instance and let Will be about shortcuts about I don't know turn off so I recently switched to Apple but let it be so least you know how in my charm you can actually type instead of you can even talk instead of but it's not's say we put some coming client again
es = Elasticsearch(
    'https://localhost:9200',
    ca_certs=f'{ES_HOME}{cert_path}',
    basic_auth=('elastic', ELASTIC_PASSWORD)
)

client_info=es.info()
print('Connected to Elasticsearch')
pprint(client_info.body)



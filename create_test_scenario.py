from kinto_http import Client

# Login
credentials = ('paco', '123456')
client = Client(server_url="http://localhost:8888/v1", auth=credentials)

# Create bucket
client.create_collection(id='Tasks', bucket='default')
client.create_collection(id='Test', bucket='default')

# Add records
client.create_record(data={'title':'Create Documentation',
                           'description':'Create docs using Markdown',
                           'status':'Done'},
                     collection='Test', bucket='default')

client.create_record(data={'title':'Create Dockerfile',
                           'description':'Create Parse Dockerfile',
                           'status':'Done'},
                     collection='Test', bucket='default')

client.create_record(data={'title':'Update Computer',
                           'description':'Update Solus Distro',
                           'status':'Doing'},
                     collection='Test', bucket='default')

client.create_record(data={'title':'Read JMeter Tutorial',
                           'description':'JMeter tutorial on internet',
                           'status':'Doing'},
                     collection='Test', bucket='default')

client.create_record(data={'title':'Install Barrier',
                           'description':'Barrier Software',
                           'status':'Done'},
                     collection='Test', bucket='default')
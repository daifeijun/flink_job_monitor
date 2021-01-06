from pyapollo import ApolloClient
from pojo import properties
def getApolloData(key):
    '''
    :param key: 传入key
    :return: 返回apollo上对应的key键的value值
    '''
    props = properties.Properties(r"./env.properties")
    url=props.get('appurl')
    appid=props.get('appid')
    ns=props.get('ns')
    client = ApolloClient(app_id=appid,config_server_url=url)
    client.start()
    print(client.get_value(key,namespace=ns))
    return client.get_value(key,namespace=ns)
getApolloData('yarn')
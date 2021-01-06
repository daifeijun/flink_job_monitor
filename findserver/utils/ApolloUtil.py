from pyapollo import ApolloClient
class MyApollo:
    def __init__(self,appid,url,ns):
        """
        传入url,初始化对象
        :param url: 请求接口地址
        """
        self.url = url
        self.appid = appid
        self.ns = ns

    def getApolloData(self,key):
        '''
        :param key: 传入key
        :return: 返回apollo上对应的key键的value值
        '''
        client = ApolloClient(app_id=self.appid, config_server_url=self.url)
        client.start()
        return client.get_value(key, namespace=self.ns)
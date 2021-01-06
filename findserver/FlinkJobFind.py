#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pojo import DBServer as DB
from pojo import FindServer
from utils import properties,ApolloUtil
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    appid = sys.argv[2]
    ns = sys.argv[3]
    client=ApolloUtil.MyApollo(appid,url,ns)
    host=client.getApolloData('host')
    port=int(client.getApolloData('port'))
    username=client.getApolloData('username')
    password=client.getApolloData('password')
    dbname=client.getApolloData('dbname')
    # 获得mysql连接
    conn = DB.DataBase(host, port, username, password, dbname).getConn()
    # 传入mysql连接初始化server服务
    server = FindServer.ExcutorServer(conn)
    # 启动发现server服务
    server.findStart()
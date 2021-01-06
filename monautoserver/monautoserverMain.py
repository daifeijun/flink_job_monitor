# coding=utf-8
from utils import dfandmon
if __name__=="__main__":
    monlist = dfandmon.getdflist()
    automon = []
    dfandmon.monStart(monlist)

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket
import pandas as pd
import pickle as pickle
def Main():
    host = ''
    port = 53
    s = socket.socket()
    s.bind((host,port))
    while True:
        data1 = pd.Series();
        data2 = pd.Series();
        s.listen(5)
        c1, addr1 = s.accept()
    
        print ("Connection from :"+str(addr1))
        c2, addr2 = s.accept()
        print ("Connection from :"+str(addr2))
        
        
        data3 = c1.recv(50000000000)
        data1 = pickle.loads(data3)
        
        data4 = c2.recv(50000000000)
        data2 = pickle.loads(data4)
        
        print(data1)
        print(data2)
        
        global_item_set = (data1+data2)/2
        global_frequent_item_set = global_item_set[global_item_set>=160]
        
        print(global_frequent_item_set)
      
        c1.send(pickle.dumps(global_frequent_item_set))
        c2.send(pickle.dumps(global_frequent_item_set))
    
    c1.close()
    c2.close()
    
    
if __name__ == '__main__':
    Main()
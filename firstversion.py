
# coding: utf-8

# In[39]:

import pandas as pd
import itertools as iter
import re
import numpy as np
import socket
import pickle
from timeit import default_timer
rowskip = 1
no_of_rows =1000
minimum_support = 100
final_itemset = pd.DataFrame();


# In[43]:

def sendToServer(send_bytes):
    #host = '127.0.0.1'
    host = '169.254.0.153'
    port = 53
    s = socket.socket()
    s.connect((host,port))
    #print("Connected to Server")
    s.send(send_bytes)
    received_bytes = s.recv(500000)
    return received_bytes


# In[46]:

def get_combinations(dataframe,dim):   
    colComb = [a for a in iter.combinations(dataframe.columns,dim)]
    return colComb

def get_combinations2(lst,start,end):
    comb = (iter.combinations(lst, l) for l in range(start,end))
    return list(iter.chain.from_iterable(comb))

while True:
# In[40]:
    start = default_timer()
    transactions = pd.read_csv("original1.csv",skiprows = range (1,rowskip),nrows = no_of_rows)
    transactions
    
    
    # In[41]:
    
    one_item_count = transactions.sum(axis=0)
    print("\n\nOne Item Count:\n\n"+str(one_item_count))
    
    
    # In[42]:
    
    frequent_one_item_count = one_item_count[one_item_count >= minimum_support]
    print("\n\nFrequent One Item Count:\n\n"+str(frequent_one_item_count))
    
    
    # In[44]:
    
    global_frequent_one_itemset = pickle.loads(sendToServer(pickle.dumps(frequent_one_item_count)))
    print("\n\nGlobal Frequent One Item Count:\n\n"+str(global_frequent_one_itemset))
    
    
    # In[45]:
    
    # start = default_timer()
    # print (default_timer() - start)
    
    
    # In[47]:
    
    two_item_count = pd.Series()
    combinations = get_combinations(transactions,2)
    #print(combinations)
    for column_index in combinations: 
        columns = str(column_index).strip("(,')").split()
        column1 = columns[0].strip("',")
        column2 = columns[1].strip("',")
        if(column1 in global_frequent_one_itemset.index and column2 in global_frequent_one_itemset.index):
            temp = pd.Series([(transactions[column1] & transactions[column2]).sum()],index = [column1+","+column2])
            
            two_item_count = two_item_count.append(temp)
        
    print("\n\nTwo Item Count:\n\n"+str(two_item_count))
    
    
    # In[48]:
    
    frequent_two_item_count = two_item_count[two_item_count>=minimum_support]
    print("\n\nFrequent Two Item Count:\n\n"+str(frequent_two_item_count))
    
    
    # In[49]:
    
    global_frequent_two_itemset = pickle.loads(sendToServer(pickle.dumps(frequent_two_item_count)))
    
    
    # In[50]:
    
    print("\n\nGlobal Two Item Count:\n\n"+str(global_frequent_two_itemset))
    
    
    # In[51]:
    
    three_item_count = pd.Series()
    combinations = get_combinations(transactions,3)
    for column_index in combinations: 
        columns = str(column_index).strip("(,')").split()
        column1 = columns[0].strip("',")
        column2 = columns[1].strip("',")
        column3 = columns[2].strip("',")
    
        if((column1+","+column2) in global_frequent_two_itemset.index and (column1+","+column3) in global_frequent_two_itemset.index and (column2+","+column3) in global_frequent_two_itemset.index):
            temp = pd.Series([(transactions[column1] & transactions[column2] & (transactions[column1])).sum()],index = [column1+","+column2+","+column3])
            
            three_item_count = three_item_count.append(temp)
        
    print("\n\nThree Item Count:\n\n"+str(three_item_count))
    
    
    # In[52]:
    
    frequent_three_item_count = three_item_count[three_item_count>=minimum_support]
    print("\n\nFrequent Three Item Count:\n\n"+str(frequent_three_item_count))
    
    
    # In[53]:
    
    global_frequent_three_itemset = pickle.loads(sendToServer(pickle.dumps(frequent_three_item_count)))
    
    
    # In[54]:
    
    print("\n\nGlobal Frequent Three Item Count:\n\n"+str(global_frequent_three_itemset ))
    
    
    # In[55]:
    
    print("\n\nPrevious Final Itemset:\n\n"+str(final_itemset))
    
    
    # In[57]:
    
    rowskip += 1000
    if final_itemset.empty:
        final_itemset = global_frequent_three_itemset
    else:
        final_itemset = final_itemset.add(global_frequent_three_itemset,fill_value=0)
    print("\n\nNew Final Itemset:\n\n"+str(final_itemset))
    
    duration = default_timer() - start

    print("\n\nExecution Time:"+str(duration))
    
    if (int(input("\n\nDo you want to continue? Enter 1 for Yes\n")) == 1) :
        continue
    else:
        break


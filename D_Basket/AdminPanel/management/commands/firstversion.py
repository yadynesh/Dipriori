
# coding: utf-8

# In[25]:

import pandas as pd
import itertools as iter
import re
import numpy as np
import socket
import pickle
import matplotlib
from timeit import default_timer
rowskip = 1
no_of_rows = 10000
items = 60
support_percent = 10/100
confidence = 0 
minimum_support = support_percent * no_of_rows
final_three_itemset = pd.DataFrame();
final_two_itemset = pd.DataFrame();
final_one_itemset = pd.DataFrame();
print("Minimum support = "+str(minimum_support))


# In[26]:

def sendToServer(send_bytes):
    host = '127.0.0.1'
    #host = '169.254.0.153'
    port = 53
    s = socket.socket()
    s.connect((host,port))
    print("Connected Server")
    s.send(send_bytes)
    received_bytes = s.recv(500000)
    return received_bytes


# In[27]:

def get_combinations(dataframe,dim):   
    colComb = [a for a in iter.combinations(dataframe.columns,dim)]
    return colComb

def get_combinations_from_list(lst,start,end):
    comb = (iter.combinations(lst, l) for l in range(start,end))
    return list(iter.chain.from_iterable(comb))


# In[70]:

def add_to_final_itemset(final_set,frequent_itemset):
    if final_set.empty:
        final_set = frequent_itemset
    else:
        final_set = final_set.add(frequent_itemset,fill_value=0)
    return final_set


# In[71]:
while True:
    transactions = pd.read_csv("C:/Users/yadynesh/Final_Project/original3.csv",skiprows = range (1,rowskip),nrows = no_of_rows)
    if len(transactions) != no_of_rows:
        print("\n\n***********Not enough transactions***********\n\n")
        break
    
    
    # In[72]:
    
    one_item_count = transactions.sum(axis=0)
    print("One Item Count:\n\n"+str(one_item_count))
    
    
    # In[73]:
    
    frequent_one_item_count = one_item_count[one_item_count >= minimum_support]
    print("Frequent One Item Count:\n\n"+str(frequent_one_item_count))
    
    
    # In[74]:
    
    global_frequent_one_itemset = pickle.loads(sendToServer(pickle.dumps(frequent_one_item_count)))
    final_one_itemset = add_to_final_itemset(final_one_itemset,global_frequent_one_itemset)
    print("Global Frequent One Item Count:\n\n"+str(global_frequent_one_itemset))
    
     
    # In[76]:
    
    two_item_count = pd.Series()
    combinations = get_combinations(transactions,2)
    
    for column_index in combinations: 
        columns = str(column_index).strip("(,')").split()
        column1 = columns[0].strip("',")
        column2 = columns[1].strip("',")
        if(column1 in global_frequent_one_itemset.index and column2 in global_frequent_one_itemset.index):
            temp = pd.Series([(transactions[column1] & transactions[column2]).sum()],index = [column1+","+column2])
            
            two_item_count = two_item_count.append(temp)
        
    print("\n\nTwo Item Count:\n\n"+str(two_item_count))
    
    
    # In[77]:
    
    frequent_two_item_count = two_item_count[two_item_count>=minimum_support]
    print("\n\nFrequent Two Item Count:\n\n"+str(frequent_two_item_count))
    
    
    # In[78]:
    
    global_frequent_two_itemset = pickle.loads(sendToServer(pickle.dumps(frequent_two_item_count)))
    
    
    # In[79]:
    
    print("\n\nGlobal Two Item Count:\n\n"+str(global_frequent_two_itemset))
    final_two_itemset = add_to_final_itemset(final_two_itemset,global_frequent_two_itemset)
    print("\n\nFinal Two Item Count:\n\n"+str(final_two_itemset))
    
    
    # In[80]:
    
    three_item_count = pd.Series()
    combinations = get_combinations(transactions,3)
    for column_index in combinations: 
        columns = str(column_index).strip("(,')").split()
        column1 = columns[0].strip("',")
        column2 = columns[1].strip("',")
        column3 = columns[2].strip("',")
    
        if((column1+","+column2) in global_frequent_two_itemset.index and (column1+","+column3) in global_frequent_two_itemset.index and (column2+","+column3) in global_frequent_two_itemset.index):
            temp = pd.Series([(transactions[column1] & transactions[column2] & (transactions[column3])).sum()],index = [column1+","+column2+","+column3])
            
            three_item_count = three_item_count.append(temp)
        
    print("\n\nThree Item Count:\n\n"+str(three_item_count))
    
    
    # In[81]:
    
    frequent_three_item_count = three_item_count[three_item_count>=minimum_support]
    print("\n\nFrequent Three Item Count:\n\n"+str(frequent_three_item_count))
    
    
    # In[82]:
    
    global_frequent_three_itemset = pickle.loads(sendToServer(pickle.dumps(frequent_three_item_count)))
    
    
    # In[83]:
    
    print("\n\nGlobal Frequent Three Item Count:\n\n"+str(global_frequent_three_itemset ))
    
    
    # In[84]:
    
    
    rowskip += no_of_rows
    if final_three_itemset.empty:
        final_three_itemset = global_frequent_three_itemset
    else:
        final_three_itemset = add_to_final_itemset(final_three_itemset,global_frequent_three_itemset)
    print("\n\n Final Three Itemset:\n\n"+str(final_three_itemset))
    
    
    # In[85]:
    
    final_minimum_support = support_percent * rowskip
    
    
    # In[86]:
    
    print ("Number of rows scanned="+str(rowskip))
    


# In[87]:

final_two_items = pd.Series()
final_two_items = final_two_items.append(final_two_itemset)
for index1 in final_two_itemset.index:
    columns = str(index1).split(",")
    column1 = columns[0]
    column2 = columns[1]
    for index2 in final_three_itemset.index:
        if column1 in index2 and column2 in index2:
            final_two_itemset = final_two_itemset.drop(index1)
            break

# In[89]:

association_rules = pd.Series()
association_list = []

for inx in final_three_itemset.index:
    association_list = []
    columns = str(inx).split(",")
    column1 = columns[0]
    column2 = columns[1]
    column3 = columns[2]
    
    combinations = get_combinations_from_list([column1,column2,column3],1,4)
    column1 = ""
    column2 = ""
    column3 = ""
    for item in combinations:
        
        columns = str(item).strip("(,')").split()
        
        if (len(columns) == 1):
            column1 = columns[0].strip("',")
            if column1 not in association_list:
                confidence = (final_three_itemset[inx]/final_one_itemset[column1]) * 100 ;
                #print(confidence)
                if confidence > 80 :
                    association_list.append(column1)
                    association_rules  = association_rules.append(pd.Series(inx.replace(column1,''), index=[""+column1]))
                
     

for inx in final_three_itemset.index:
    association_list = []
    columns = str(inx).split(",")
    column1 = columns[0]
    column2 = columns[1]
    column3 = columns[2]
    
    combinations = get_combinations_from_list([column1,column2,column3],1,4)
    column1 = ""
    column2 = ""
    column3 = ""
    for item in combinations:
        
        columns = str(item).strip("(,')").split()
        

        if (len(columns) == 2):
            column1 = columns[0].strip("',")
            column2 = columns[1].strip("',")
            
            if column1 not in association_list and column2 not in association_list :
                confidence = (final_three_itemset[inx]/final_two_items[column1+","+column2]) * 100 ;
                #print(confidence)
                if confidence > 80 :
                    association_rules = association_rules.append(pd.Series(inx.replace(column1,'').replace(column2,''), index=[""+column1+","+column2]))
# In[91]:

print(association_rules)
final_one_itemset.to_csv(path="C:/Users/yadynesh/Final_Project/D_Basket/final_one_itemset.csv")
final_two_items.to_csv(path="C:/Users/yadynesh/Final_Project/D_Basket/final_two_itemset.csv")
final_three_itemset.to_csv(path="C:/Users/yadynesh/Final_Project/D_Basket/final_three_itemset.csv")

# In[ ]:




# In[ ]:




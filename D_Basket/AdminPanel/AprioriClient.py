def main():

    #importing the django settings file
    from django.conf import settings

    #importing Tables from the database
    from .models import Statistic, Item, Configuration
    import pandas as pd
    import itertools as iter
    import re
    import socket

    #This is to convert data to bytes.
    import pickle

    #This is used to display graphs.
    import matplotlib

    #This is for calculate the time taken.
    from timeit import default_timer


    '''
    Getting data from Statistic table.
    The method first() is used to retrieve the first row of the table as an object.
    We have only one row in the Statistic and Configuration Table.
    '''
    stats_object = Statistic.objects.first()

    #getting data from Configuration table
    conf_object = Configuration.objects.first()

    #starts calculating the time
    start_time = default_timer()

    '''
    Getting the number of rows already scanned, from the datbase (i.e. The number of transactions for which the 
    final itemsets are already generated. So we dont need to scan those transactions again.)
    '''
    rows_scanned = stats_object.rows_scanned

    '''
    Getting the number of batches scanned so far.Currently the batch size is 10000.
    '''
    total_batches = stats_object.total_batches
    batch_size = 10000


    items = 60

    #support percent is taken from the admin(on the website) and stored in the database.
    support_percent = conf_object.local_minimum_support/100
    confidence = 0

    #the minimum confidence required for an rule to be in the association_rules.
    required_confidence = conf_object.local_confidence

    #generating minimum support based on the batch_size and support_percent.
    minimum_support = support_percent * batch_size

    #creating three pandas Series.
    final_three_itemset = pd.Series();
    final_two_itemset = pd.Series();
    final_one_itemset = pd.Series();


    print("Minimum support = "+str(minimum_support))

    '''
    If rows_scanned == 1 then it indicates that no transactions have been processed until now.
    However if rows_scanned > 1 it indicates that some transactions have already been processed and
    the final_itemset for those transactions are already generated and stored.
    If this is the case, we going to read those final_itemsets which are already generated so that we
    can continue working on them when a new set of transactions arrive thus eliminating the need to process
    the old transactions again.
    '''
    if(rows_scanned > 1):
        final_one_itemset  = pd.Series.from_csv(path = settings.BASE_DIR+"/final_one_itemset.csv")
        final_two_itemset  = pd.Series.from_csv(path = settings.BASE_DIR+"/final_two_itemset.csv")
        final_three_itemset = pd.Series.from_csv(path = settings.BASE_DIR+"/final_three_itemset.csv")

    
    '''
    This function is used to send the data in bytes to the server and will return the data returned back
    by the server.
    '''
    def sendToServer(send_bytes):
        host = conf_object.server_ip_address
        port = 53
        s = socket.socket()
        s.connect((host,port))
        print("Connected Server")
        s.send(send_bytes)
        received_bytes = s.recv(500000)
        return received_bytes


    # In[27]:

    #This function is used to generate combinations of items in candidate itemsets.
    def get_combinations(dataframe,dim):   
        colComb = [a for a in iter.combinations(dataframe.columns,dim)]
        return colComb

    def get_combinations_from_list(lst,start,end):
        comb = (iter.combinations(lst, l) for l in range(start,end))
        return list(iter.chain.from_iterable(comb))


    # In[70]:

    
    #This function adds two pandas series.
    def add_to_final_itemset(final_set,frequent_itemset):
        if final_set.empty:
            final_set = frequent_itemset
        else:
            final_set = final_set.fillna(0).add(frequent_itemset)
        return final_set

    '''
    This method is used to clean the items in the association_rules.
    i.e removing extra commas and blank spaces
    '''
    def clean_three_items(items):
        items = items.split(",")
        cleaned_items = ""
        item1 = items[0]
        item2 = items[1]
        item3 = items[2]
        
        if (item1 != ""):
            cleaned_items += item1

        if (item2 != ""):
            if(cleaned_items != ""):
                cleaned_items += ","
            cleaned_items += item2

        if (item3 != ""):
            if(cleaned_items != ""):
                cleaned_items += ","
            cleaned_items += item3
            
        return cleaned_items

    # In[71]:
    
    #continue until size of a batch is not equal to batch_size
    while True:

        #reading transactions from csv.
        transactions = pd.read_csv(settings.BASE_DIR+"/AdminPanel/Final_Original2.csv",skiprows = range (1,rows_scanned),nrows = batch_size)

        #These two dataframes are used to write batch wise data to csvs which is then used to show batch wise graphs.
        batch_local_frequent_one_item_count = pd.DataFrame(columns = transactions.columns)
        batch_global_frequent_one_item_count = pd.DataFrame(columns = transactions.columns)

        #if the number of transactions not equal to specified batch size stop.
        if len(transactions) != batch_size:
            print("\n\n***********Not enough transactions***********\n\n")
            break
        
        
        # In[72]:
        
        #generating candidate one itemset
        one_item_count = transactions.sum(axis=0)
        print(type(one_item_count))
        print("One Item Count:\n\n"+str(one_item_count))

        #writing one itemset for current batch to the csv 
        one_item_count.to_frame().T.to_csv(path_or_buf = settings.BASE_DIR + "/batchwise_one_item_count.csv", mode = 'a',header = (rows_scanned==1), index = False)
        
        #generataing frequent one itemset
        frequent_one_item_count = one_item_count[one_item_count >= minimum_support]
        print("Frequent One Item Count:\n\n"+str(frequent_one_item_count))

        #writing the frequent one itemset for current batch to csv.
        batch_local_frequent_one_item_count = batch_local_frequent_one_item_count.add(frequent_one_item_count.to_frame().T, axis='columns', fill_value = 0.0)
        batch_local_frequent_one_item_count = batch_local_frequent_one_item_count.fillna(0)
        batch_local_frequent_one_item_count.to_csv(path_or_buf = settings.BASE_DIR + "/batchwise_local_frequent_one_item.csv", mode = 'a',header = (rows_scanned==1), index = False)

        #sending frequent one itemset to server and recieving global frequent one itemsets
        global_frequent_one_itemset = pickle.loads(sendToServer(pickle.dumps(frequent_one_item_count)))

        #adding the global frequent itemset to the final one itemset.
        final_one_itemset = add_to_final_itemset(final_one_itemset,global_frequent_one_itemset)
        print("Global Frequent One Item Count:\n\n"+str(global_frequent_one_itemset))

        #writing global frequent one itemset for current batch to csv.
        batch_global_frequent_one_item_count = batch_global_frequent_one_item_count.add(global_frequent_one_itemset.to_frame().T, axis='columns', fill_value = 0.0)
        batch_global_frequent_one_item_count = batch_global_frequent_one_item_count.fillna(0)
        batch_global_frequent_one_item_count.to_csv(path_or_buf = settings.BASE_DIR + "/batchwise_global_frequent_one_item.csv", mode = 'a',header = (rows_scanned==1), index = False)
        
         
        # In[76]:
        
        two_item_count = pd.Series()
        combinations = get_combinations(transactions,2)
        

        #generating candidate two itemsets from the global frequent one itemsets
        for column_index in combinations: 
            columns = str(column_index).strip("(,')").split()
            column1 = columns[0].strip("',")
            column2 = columns[1].strip("',")
            if(column1 in global_frequent_one_itemset.index and column2 in global_frequent_one_itemset.index):
                temp = pd.Series([(transactions[column1] & transactions[column2]).sum()],index = [column1+","+column2])
                
                two_item_count = two_item_count.append(temp)
            
        print("\n\nTwo Item Count:\n\n"+str(two_item_count))
        
        
        # In[77]:
        
        #generating frequent two itemsets
        frequent_two_item_count = two_item_count[two_item_count>=minimum_support]
        print("\n\nFrequent Two Item Count:\n\n"+str(frequent_two_item_count))
        
        #sending frequent two itemsets to server and recieving global frequent two itemset
        global_frequent_two_itemset = pickle.loads(sendToServer(pickle.dumps(frequent_two_item_count)))
        print("\n\nGlobal Two Item Count:\n\n"+str(global_frequent_two_itemset))

        #adding the global frequent two itemsets to the final two itemsets
        final_two_itemset = add_to_final_itemset(final_two_itemset,global_frequent_two_itemset)
        print("\n\nFinal Two Item Count:\n\n"+str(final_two_itemset))
        
        
        # In[80]:
        
        three_item_count = pd.Series()
        combinations = get_combinations(transactions,3)

        #generating candidate three itemsets from global frequent two itemsets
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
        
        #generating frequent three itemsets
        frequent_three_item_count = three_item_count[three_item_count>=minimum_support]
        print("\n\nFrequent Three Item Count:\n\n"+str(frequent_three_item_count))
        
        
        #sending frequent three itemsets to the server and recieving global frequent three itemsets
        global_frequent_three_itemset = pickle.loads(sendToServer(pickle.dumps(frequent_three_item_count)))
        print("\n\nGlobal Frequent Three Item Count:\n\n"+str(global_frequent_three_itemset ))
        
        
        # In[84]:
        
        #incrementing the rows_scanned as a new batch has been processed.
        rows_scanned += batch_size

        if final_three_itemset.empty:
            final_three_itemset = global_frequent_three_itemset
        else:
            final_three_itemset = add_to_final_itemset(final_three_itemset,global_frequent_three_itemset)
        print("\n\n Final Three Itemset:\n\n"+str(final_three_itemset))
        
        
        # In[85]:
        
        #calculating the minimum support based on the number of transactions scanned so far.
        final_minimum_support = support_percent * rows_scanned
        
        
        # In[86]:
        
        #incrementing the total_batches scanned by one 
        total_batches += 1
        print ("Number of rows scanned="+str(rows_scanned))
        
    
    # In[87]:
    # final_two_itemset = final_two_itemset[final_two_itemset>50000]  
    # final_three_itemset = final_three_itemset[final_three_itemset>50000]

    '''
    filtering the final_two_itemsets.
    i.e if a two_itemset is already a subset of frequent_three_itemset drop that itemset from two_itemset
    ''' 
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

    association_rules = pd.DataFrame(columns=['rule_leftside','rule_rightside','confidence'])
    association_list = []

    #generating association rules. one item on the left.
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
                    if confidence > required_confidence :
                        rule  = pd.DataFrame({'rule_leftside':[column1],'rule_rightside':[inx.replace(column1,'')],'confidence':[confidence]})
                        association_rules = association_rules.append(rule)
                    
         
    #generating association rules. two items on the left.                    
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
                    if confidence > required_confidence :
                        rule  = pd.DataFrame({'rule_leftside':[""+column1+","+column2],'rule_rightside':[inx.replace(column1,'').replace(column2,'')],'confidence':[confidence]})
                        association_rules = association_rules.append(rule)
    # In[91]:


    association_rules['rule_rightside'] = association_rules['rule_rightside'].apply(clean_three_items)
    print(association_rules)


    #writing  data to csvs and database.
    
    association_rules.to_csv(path_or_buf=settings.BASE_DIR+"/association_rules.csv")
    final_one_itemset.to_csv(path=settings.BASE_DIR+"/final_one_itemset.csv")
    final_two_items.to_csv(path=settings.BASE_DIR+"/final_two_itemset.csv")
    final_three_itemset.to_csv(path=settings.BASE_DIR+"/final_three_itemset.csv")

    end_time = default_timer()
    stats_object.run_time = round((end_time - start_time),4)

    stats_object.rows_scanned = rows_scanned

    stats_object.total_batches = total_batches

    stats_object.most_frequent_item = Item.objects.get(item_name = final_one_itemset.idxmax())

    stats_object.save()


if __name__ == "__main__":
    main()



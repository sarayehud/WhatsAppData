import json
import os

def read():
    #file_path= input('enter a file path:')
    File= open('C:/Users/97250/Desktop/saray.py/Q3/WhatsApp.txt', encoding='utf-8')
    diction(File)
    
    

def diction(File:str): 
    dic_id=dict()
    dic=dict()
    second_line=1
    n_line=0
    num=1
    lst=list()
    metadata=dict()
    AllData=dict()
    
    for line in File:
        line=line.rstrip()
        right=line.find('-') 
        left=line.find(':',right)        
        if left>0:    
            name=line[right+1:left]
            if name not in dic_id:
               dic_id[name]=num
               num=num+1
            dic['date']= line[0:right-1]
            
            dic['text'] = line[left: ]
           
            name_as_id= str(dic_id[name])
           
          
            lst.append({ 'id' : name_as_id, 'date': dic['date'] , 'text': dic['text'].strip()})
        if n_line == second_line:
            Start= line.find('"')
            End= line.find('"',Start+1)
            metadata['chatName'] = line[Start+1: End]
            chatName=metadata['chatName']
            metadata['date']= line[0:right-1]
            d=line.find('ידי')
            #f=line.find('+')
            metadata['creator']=line[d+3:]
        if left<0 and '-' not in line : 
           # dic['text']= (dic['text']+line).strip()
            lst.append(dic['text']+line)
           
            
    
            
            
        n_line +=1
    
    
    metadata['num_of_participants']=len(dic_id)   
    
    AllData= {'Massage':lst,'metdata':metadata}
    print(AllData)
    
#    json_string = json.dumps(lst2)
    son_string = json.dumps(AllData,indent=4, ensure_ascii=False)

    with open(os.path.join('C:/Users/97250/Desktop/saray.py/Q3',chatName+".txt"), 'w',encoding='utf-8') as f:
        f.write(son_string)

read()
 
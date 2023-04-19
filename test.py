#test to get  all file
from pickle import TRUE
import urllib.request
import requests as r
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def getdata(data):
    name = data['data']["tables"][0]['rows'][2]['cols'][8]['nodeValue']
    
    #===========theory==================
    theory = TRUE;
    thi = 25;
    th = []
    while(theory):
        th.append(int(data['data']["tables"][0]['rows'][2]['cols'][thi]['nodeValue']))
        if data['data']["tables"][0]['rows'][2]['cols'][thi+1]['nodeValue'].isdigit():
            thi=thi+5;
        else:
            theory =False
    pra= []
    practical = TRUE
    thi = thi+6
    while(practical):
        pra.append(int(data['data']["tables"][0]['rows'][2]['cols'][thi]['nodeValue']))
        if data['data']["tables"][0]['rows'][2]['cols'][thi+1]['nodeValue'].isdigit():
            thi=thi+5;
        else:
            practical =False 
    
    #-----------sum-------------
    thsum =sum(th)
    prsum =sum(pra)
    Sessional = int(data['data']["tables"][0]['rows'][2]['cols'][thi+6]['nodeValue'])
    sca = int(data['data']["tables"][0]['rows'][2]['cols'][thi+6+5]['nodeValue'])
    total = thsum+prsum+Sessional+sca
    
    
    #=============Final Result ===========================
    th.append(thsum)
    pra.append(prsum)
    list = th+pra
    list.insert(0,name)
    list.append(sca)
    list.append(Sessional)
    list.append(total)
    return list

def converting(content):
    url = "https://html2json.com/api/v1";
    response =  r.post(url,data=content)
    jdic = response.json()
    try:
        result = getdata(jdic)
        return result
    except Exception as e:
        print("Absent")
    

def opration(url):
    req =urllib.request.Request(url,headers=headers)
    try:
        response = urllib.request.urlopen(req)
        content = response.read().decode('utf-8')
        return converting(content)
    except urllib.error.HTTPError as e:
            print(f'HTTP error: {e.code}')

def geturl(string,num):
    sjdt = "http://result.bteevaluation.co.in/Odd_Semester/main/result.aspx?Roll_no="+string
    if(num<10):
       return opration(sjdt+"0"+str(num))
    else:
       return opration(sjdt+str(num))
    

def go(string):
    filename = "Student_Result.csv"
    with open(filename,'w') as csvfile:
        csvwritter = csv.writer(csvfile)
        x = 1
        while x <= 70:
            result =  geturl(string,x)
            if type(result)==list:
                csvwritter.writerow(result)
            print("Progress :" +str(round(x/0.7)))
            x=x+1

Collagecode = input("Enter your Collage Code  (Do not you space):")
BranchCode = input("Enter your Branch Code (Do not you space):")
Bactchyear = input("Enter your Batch Year (Do not you space) eg. 2022 :")
# print("E"+Bactchyear[2:]+Collagecode+BranchCode+"000")
go("E"+Bactchyear[2:]+Collagecode+BranchCode+"000")


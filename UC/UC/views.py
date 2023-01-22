from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from . import retriever
import json
import mysql.connector
from mysql.connector import Error
import socket
from dotenv import load_dotenv
import os

load_dotenv()
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')





def ready(request):
    r = 1
    return HttpResponse("Under Maintenance")

def passme(request):
    context = {}
    return HttpResponse(render(request,'index.html',context))

def sendme(request):
    check = 0
    token_check = 0
    count_check = 0
    x = request.GET['query']
    x = str(x)
    y = request.GET['psw']
    y = str(y)
    z = list()
    host_name = socket.gethostname()


    try:

        connection = mysql.connector.connect(host=DB_HOST,
                                                 database='test',
                                                 user='seantywork',
                                                 password=DB_PASS)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM counter;')
            z = cursor.fetchall()

    except Error as e:
        data = ['DB', 'Connection', 'Failed',e]
        context = {'res':data}
        return JsonResponse(context)

    for i in range(len(z)):
        if y == z[i][0] :
            token_check = 1
        if z[i][1] <= 100 and token_check == 1:
            count_check = 1
            new_num = z[i][1] + 1
            cursor.execute('UPDATE counter SET count = '+str(new_num)+' WHERE user = \''+z[i][0]+'\';')
            connection.commit()
            cursor.close()
            connection.close()
            break



    if  len(x) < 100 and x.isascii() and token_check == 1 and count_check == 1:
        
        res = retriever.retriever([x],1)

        res = res.sample(frac=1).reset_index(drop=True)
        if len(res) > 10 :
            res = res.head(10)

        res = res.reset_index().to_json(orient='records')
        data = []
        data = json.loads(res)
        context = {'res':data}
        return JsonResponse(context)

    elif len(x) < 100 and x.isascii() and token_check == 1 and count_check == 0:
        data = ['Auth', 'Expired']
        context = {'res':data}
        return JsonResponse(context)

    else :
        data = ['Credential', 'Not', 'Found','Or','Query','Invalid']
        context = {'res':data}
        return JsonResponse(context)


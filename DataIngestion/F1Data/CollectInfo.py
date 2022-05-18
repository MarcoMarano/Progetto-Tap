from datetime import datetime

import time
import json
import requests

import re
import sys
import socket

import http.client




key = "ah6gjf62tdkfm2xy89w2pg9n"



def Send_To(host, port , data):
    error = True
    while(error):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("socket creata---->" + str(sock))
            sock.connect( (host,port))
            print("invio i dati" + str(data))
            sock.sendall(json.dumps(data).encode())
            print("chiudo la connessione")
            sock.close()
            error = False
        except:
            print("Errore di connessione")
            time.sleep(10) # aspetto 10 secondi in caso fallisco la connessione




def CollectSeasonsInfos():
    con = http.client.HTTPSConnection("api.sportradar.us")
    url = "/formula1/trial/v2/en/seasons.json?api_key=" + key 
    con.request("GET",url)
    res = con.getresponse()
    data = res.read()
    return data


def SaveIntoFile(data):
    outputFile  = open("F1LiveData.json",'w')
    outputFile.write(data)
    outputFile.close()



def CollectStageInfoFromStageId(Id):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", "/formula1/trial/v2/en/sport_events/sr:stage:"+Id+"/summary.json?api_key=" + key)
    res = conn.getresponse()
    rawdata = res.read().decode('utf-8')
    return rawdata

def ExtarctData(data):
    season = json.loads(data)
    stages = season["stages"]
    for stage in stages:
        description = stage["description"]
        if description == "Formula 1 2022":
            rawId = stage["id"]
            campionatoID = rawId[9:]
    stageSummary = CollectStageInfoFromStageId(campionatoID)
    summary = json.loads(stageSummary)

    team = summary['teams']
    pilot = team['competitors']

    
    return  pilot




data = ExtarctData(CollectSeasonsInfos())
print(data)

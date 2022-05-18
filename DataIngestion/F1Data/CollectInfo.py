from cmath import inf
from datetime import datetime

import time
import json
import requests

import re
import sys
import socket

import http.client




key = "ah6gjf62tdkfm2xy89w2pg9n"
CurrentSeasonId = "sr:stage:937183"


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



def CollectStageInfoFromStageId():
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", "/formula1/trial/v2/en/sport_events/"+CurrentSeasonId+"/summary.json?api_key=" + key)
    res = conn.getresponse()
    rawdata = res.read()
    return rawdata


def CollectMoreINFOFromStageId():
    conn = http.client.HTTPSConnection("api.sportradar.us")

    conn.request("GET", "/formula1/trial/v2/us/sport_events/"+"sr:stage:324773"+"/probabilities.json?api_key="+ key)

    res = conn.getresponse()
    data = res.read()
    return data


def ExtractData(RawDataINFO):  #RawDataINFO corrisponde a seasonFile quindi conterra tutte le info 
                               # della stagione attuale
    Circuiti = RawDataINFO['stage']['stages']
    Piloti   = RawDataINFO['stage']['competitors']

    return Piloti


##! SERVE  A RACCOGLIERE I DATI DELLA SEASON CHE MOMENTANEAMENTE PER
##! DEBUG E COSTRUZIONE SONO SALVATI NEL FILE JSON 
##! QUINDI LEGGERE QUEL FILE PER EVITARE DI FARE TANTE RICHIESTE

# SeasonINFO = CollectStageInfoFromStageId()


InFile = open("F1LiveData.json")
SeasonFIle = json.loads(InFile.read())

outFile = open("Info.json","w")
data = CollectMoreINFOFromStageId()

info = json.loads(data)
outFile.write(json.dumps(info))















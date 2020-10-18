import os
from gtts import gTTS
import pyttsx3
import sys
import urllib.request
import urllib.parse
import threading
import random
import time
import requests
resultadoDescarga = [0]*10
def creaAudioGTTS(destino, voz, texto):
    tts = None
    if voz == "google_es":
        tts = gTTS(texto,lang='es-es')
    else:
        tts = gTTS(texto,lang='es-us')
    tts.save(str(destino)+"_orig")

def leeArchivo(archivo):
    f= open(archivo,"r")
    contents =f.read()
    f.close()
    return contents
def escribeArchivo(archivo):
    f = open("TTS"+archivo+".txt","w+")
    f.write("1")
    f.close()
def convierteArchivo(origen, destino):
    comando = "ffmpeg -i "+str(origen)+" -acodec pcm_s16le -ar 8000 -sample_fmt s16 -ac 1 -framerate 2 -y "+str(destino)
    os.system(comando)
    

voz = str(sys.argv[1])
archivoOrigen = str(sys.argv[2])
archivoDestino = str(sys.argv[3])
if "google" in voz:
    creaAudioGTTS(archivoDestino,voz,leeArchivo(archivoOrigen+".txt"))    
convierteArchivo(archivoDestino+"_orig",archivoDestino)
os.remove(archivoDestino+"_orig")
escribeArchivo(archivoOrigen)

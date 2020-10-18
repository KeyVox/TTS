from gtts import gTTS
from .ttsEngine import TTSEngine
class Google(TTSEngine):
    def __init__(self, idAsterisk:str, voz:str):        
        super().__init__(voz, 1, idAsterisk)
    
    def generarAudio(self)->bool:
        texto:str = super().leerContenido()
        tts: None
        if self.idVoz == "google_es":
            tts = gTTS(texto,lang='es-es')
        else:
            tts = gTTS(texto,lang='es-us')
        try:
            tts.save(self.archivoAudioSinConvertir)
            return True
        except:
            return False

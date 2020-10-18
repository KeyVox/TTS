class Launcher(object):
    voz:str = None
    categoriaVoz:int = None
    nombreArchivo:str = None
    def __init__(self, voz:str, categoriaVoz:int, nombreArchivo:str)->None:
        self.voz = voz
        self.categoriaVoz = categoriaVoz
        self.nombreArchivo = nombreArchivo
    def iniciaGenerador(self)->None:        
        engine:TTSEngine = None
        if self.categoriaVoz == 0:
            from .nuance import Nuance
            engine = Nuance(self.nombreArchivo, self.voz)
        elif self.categoriaVoz == 1:            
            if "google" in self.voz:
                from .google import Google
                engine = Google(self.nombreArchivo, self.voz)
        if engine.generarAudio():
            if engine.convertirAudio() and engine.validaTTS():
                engine.escribirBandera()
            else:
                print("Error: ffmpeg no se encuentra instalado en el equipo")
            engine.eliminarArchivoSinConvertir()
        else:
            #Aqui tendriamos que ver una forma de escoger otra engine
            pass        

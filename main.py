import sys
from andreaGenerador import Launcher

if(len(sys.argv) == 4):
    categoriaVoz:int = int(sys.argv[1])
    voz:str = sys.argv[2]
    idAsterisk:str = sys.argv[3]
    launcher = Launcher(voz, categoriaVoz, idAsterisk)
    launcher.iniciaGenerador()
else:
    print("Error, el programa se tiene que ejecutar:\nandreaGenerator [tipoVoz] [nombreVoz] [archivo]")
    

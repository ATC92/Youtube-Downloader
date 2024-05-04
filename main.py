# Importación de módulo YouTube
from pytube import YouTube
from Resources.funtions import *
from os import system

# Barra de inicio
inConsole(30)
print("\n")
# Seleccionamos el idioma
while True:
    print("[1] - Español\n[2] - English")
    idioma = input(">>> ")
    if(idioma == "1"):
        idioma ="es"
        break
    elif (idioma == "2"):
        idioma = "en"
        break
# Cargamos la opcion
string = cargar_strings(idioma)
# Try para verificar algún error.
try:
    while(True):
        # Lo mandamos a objeto de YouTube. (Formato video)      
        YT_Object = YoutubeLink(string)
        # Imprimimos la información
        printInformation(YT_Object,string)
        # Elección para el formato.
        format = FormatSelection(string)
        # Damos formato al objeto para comenzar la descarga.
        available_streams = VideoConverter(format,YT_Object,string)
        # Selección de la resolución
        VideoResolution(available_streams,string)
        # Pregunta al usuario para repetir el programa.
        while(True):
            try:
                print(string["RepetirPrograma"])
                print(string["RepetirPrograma2"])
                Question = int(input(">>>>> "))
                break
            except ValueError:
                print(string["Error"],"\n")
        if Question == 0:
            break
        system('cls')
# En caso de algún error inesperado, lanzará un error.
except Exception as e:
    print(string["OcurrioError"], e) 

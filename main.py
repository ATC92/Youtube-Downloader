# Importación de módulo YouTube
from pytube import YouTube
from Resources.funtions import *
from os import system

def main():
    inConsole(30)
    print("\n")
    # Try para verificar algún error.
    try:
        while(True):
            # Lo mandamos a objeto de YouTube. (Formato video)      
            YT_Object = YoutubeLink()
            # Imprimimos la información
            printInformation(YT_Object)
            # Elección para el formato.
            format = FormatSelection()
            # Damos formato al objeto para comenzar la descarga.
            available_streams = VideoConverter(format,YT_Object)
            # Selección de la resolución
            VideoResolution(available_streams)
            # Pregunta al usuario para repetir el programa.
            while(True):
                try:
                    Question = int(input("Desea ingresar otro link: [1] - SI . [0] - NO: "))
                    break
                except ValueError:
                    print("Error, intenta de nuevo.\n")
            if Question == 0:
                break
            system('cls')
    # En caso de algún error inesperado, lanzará un error.
    except Exception as e:
        print('Ocurrio un error:', e) 
# Inicio del programa.
if __name__ == "__main__":
    main()
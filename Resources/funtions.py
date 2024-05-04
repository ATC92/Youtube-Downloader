from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from tqdm import tqdm
import os
import time

def inConsole(iteraciones, delay=0.01):
    # For para saber cuantas iteraciones tiene que hacer.
    for i in range(iteraciones + 1):
        # Creamos porcentaje, donde se imprimira el incremento en % al final de la barra.
        porcentaje = ( i / iteraciones) * 100 # Donde divide el contador, con el total de iteraciones por hacer y lo multipla por 100 para hacerlo %
        # Creamos barra, para imprimir la barra donde se ira llenando a partir de la iteraciones.
        barra = "█" * int(( i / iteraciones) * 50)  # Dividimos el contador, por al cantidad de iteraciones y multiplicamos por el tamaño que deseamos para la barra.
        # Creamos espacioes, para imprimir los espacios en blanco de la barra, despues de las barras.
        espacios = " " * (50 - len(barra))  # Al tamaño total de la barra de carga, le restamos el tamaño de la 'barra'.
        # Imprimimos la barra para que sea visual en consola. 
        print(f"\r[{barra}{espacios}] {int(porcentaje)}%", end="", flush=True)
        # Le damos un delay, que ya esta pre colocado en el inicio de la def.
        time.sleep(delay)

def YoutubeLink(string):
    # Creamos una variable donde guardaremos el Link del video.
    # Verificamos que el link sea correcto
    while(True):
        try:
            print(string["LinkVideo"],"",end="")
            Link = input()
            YT_Object = YouTube(Link)
            return YT_Object
        except VideoUnavailable:
            print(string[f"ErrorVideoLoad"])

def FormatSelection(string):
    try:
        # Preguntar al usuario que formato lo desea
        print(string["OptionAudioVideo"])
        print(string["OptionSelection"])
        print(string["OptionSelection2"])
        format = int(input(">>> "))
        return format
    except ValueError:
        print(string["TryAgain"],"\n")
        
def printInformation(YT_Object,string):
    # Muestra información básica del video
    # Dando Título y Autor del objeto.
    print(string["Tittle"], YT_Object.title, "\n",string["Autor"], YT_Object.author)
    print() 
    # Duración del video, donde calculamos la duración en segundos y minutos
    duration_seconds = int(YT_Object.length)
    minutes, seconds = divmod(duration_seconds, 60)
    # Muestra en consola la duración del video. Minutos y Segundos: MM:SS
    print(string["Duration"], "{}:{}".format(minutes, seconds), "\n")
    
def VideoConverter(format,YT_Object,string):
    try:
        # Verificamos lo que entra es elegido por el usuario.
        match format:
            case 1:
                # Busca las mejores opciones para descargar en el formato deseado y la resolucion deseada.
                VideoOptions = YT_Object.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
            case 2:
                # Busca las mejores opciones para descargar en el formato deseado y la resolucion deseada.
                VideoOptions = YT_Object.streams.filter(only_audio=True) # , progressive=False, file_extension='mp4',audio_codec='mp4a.40.2').order_by('resolution').desc()
            case _:
                print(string["TryAgain"])
        return VideoOptions
    except Exception as e:
        print(string["OcurrioError"],e)

def VideoResolution(VideoOptions,string):
    # Obtenemos la direccion del Escritorio
    desktopDirectory= os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    # Despliega las opciones disponibles en resolución.
    print(string["Quality"])
    for i, Video in enumerate(VideoOptions):
        print(f"[{i + 1}]. {Video.resolution} - {Video.mime_type} - {Video.filesize / (1024*1024):.2f} MB")
    # Solicita al usuario que seleccione la calidad deseada
    # Ciclamos la opción para que el usuario ingrese una opción correcta.
    while True:
        print(string["OptionNumber"],"",end="")
        selection = input()
        try:
            option = int(selection)
            break
        except ValueError:
            print(string["Error"],"\n\n")
    # Verifica si la opción seleccionada es válida
    if 1<= option <= len(VideoOptions):  
        # Obtiene la información del video seleccionado.
        VideoSelected = VideoOptions[option-1]
        # Descarga el video en la calidad deseada.
        VideoSelected.download(output_path=desktopDirectory) 
        print(string["Download"],"\n\n") 
    else:
        print(string["SelectionInvalid"])  # Indica que la opción seleccionada no es válida
        
def cargar_strings(idioma):
    # Diccionario para almacenar las cadenas de texto
    strings = {}

    # Determinar la ruta del archivo según el idioma seleccionado
    ruta_archivo = f"Resources/Language/strings_{idioma}.txt"

    # Leer las cadenas de texto desde el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            # Separar la línea en clave y valor
            clave, valor = linea.strip().split(" = ")
            # Agregar la clave y valor al diccionario
            strings[clave] = valor

    return strings

def SelectionLenguaje():
    while True:
        try:
            print("[1] - Español\n[2] - English")
            option = int(input(">>>> "))
        except ValueError:
            print("Error")
        if(option > 0 and option < 3):
            if(option == 1):
                option = "es"
            elif (option == 2):
                option = "en"
            break
        
    return option
#Script que te copie al portapapeles los puertos que se han detectado en el nmap exportado a un archivo grepeable.
import argparse
import re
import subprocess

parser=argparse.ArgumentParser(description = "Script para copir los puertos de un archivo grepeable sacado de un escaneo rápido de nmap.")
parser.add_argument('archivo', help="Archivo grepeable")

args = parser.parse_args()

def puertos():
    try:
        with open(args.archivo, 'r') as f:
            for l in f:
                if "Ports:" in l:
                    linea = l
                    print(linea)
                    break
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")
        exit(1)
    except PermissionError:
        print("No tiene suficientes permisos para abrir este archivo.")
        exit(1)
    except:
        print("Error desconocido.")
        exit(1)


    ports = re.findall(r"(\d{1,5})/", linea) #Captura los numeros de la lina mediante expresiones regulares
    ports = [port.strip() for port in ports] #Quita los espacios
    ports = ",".join(ports) #Convierte la lista a una string separada por comas
    print(ports)

    subprocess.run(['xclip', '-selection', 'clipboard'], input=ports, text=True) #Ejecutamos xclip con subprocess en el que copiamos al portapapeles lo que hay en la variable ports

puertos()

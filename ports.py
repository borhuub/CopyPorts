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

    lista = re.findall(r"(\d{1,5})/", linea)
    ports = ",".join(lista)
    subprocess.run(['xclip', '-selection', 'clipboard'], input=ports, text=True)

    print("\n\033[1;34m" + "🔍 Puertos encontrados: " + "\033[0m")
    for puerto in lista:
        print(f"  ➜ \033[1;32m {puerto} \033[0m")
    print("\n\033[1;34m¡Puertos copiados en el portapapeles!\033[0m")

puertos()

import websocket
import time
import json
from tkinter import *
from tkinter import ttk,font
from tkinter import messagebox
from gato_game import *

try:
    import thread
except ImportError:
    import _thread as thread

my_id = None

def procesar_matriz(matriz):
    posx, posy, ganador = continuar_juego(matriz,my_id)
    print("posicion y", posy , "posicion x", posx)
    return posx, posy, ganador

def on_message(ws, message):
    global my_id
    message = json.loads(message)
    print(message)
    
    # Si el message tiene un id significa que todavia no ha iniciado el juego
    if "id" in message:
        if message["id"] == -1:
            print("ya no hay cupo")
            messagebox.showinfo("Error al ingresar a la sala", "Ya no hay cupo.")
            ws.close()
        else:
            print("mi id es: " + str(message["id"]))
            my_id =  message["id"]

    # Si no tiene id siginifica que el juego ya inicio
    else:
        if "empate" in message:
            print("Fue un empate")
            ws.close()
        elif "ganador" in message:
            print("El ganador es : " + str(message["ganador"]))
            messagebox.showinfo("¡Ganador!", "El ganador es : " + message["ganador"])
            ws.close()
        else:
            turno = message["turno"]
            matriz = message["matriz"]
            print("mi turno id: " + str(my_id) + " " + str(turno))
            
            # proceso de acuerdo a mis reglas
            x, y, ganador = procesar_matriz(matriz)

            # envio mi posicion de tiro
            my_message = json.dumps({"x": x, "y": y, "ganador": ganador, "id": my_id})
            ws.send(my_message)
            
def on_error(ws, error):
    print(error)
    estado.set("Estado:  Error interno")
    #lestados = Label(raiz, text="Error interno").place(x=(650/2)-25, y=60)
    messagebox.showinfo("¡Ocurrión un error!", error)


def on_close(ws):
    print("### closed ###")
    estado.set("Estado:  Cerrado")
    #lestados = Label(raiz, text="Cerrado").place(x=(650/2)-25, y=60)


def on_open(ws):
    def run(*args):
        print("Conectado...")
        estado.set("Estado:  Conectando")
        #lestados = Label(raiz, text="Conectando").place(x=(650/2)-25, y=60)

    thread.start_new_thread(run, ())

def conectarWebSocket():
    server = host.get()
    #lestados = Label(raiz, text=estado).place(x=(650/2)-25, y=60)
    estado.set("Estado:  En reposo")
    print(server)
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(server,
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

#Cambios
global estado
raiz = Tk()
raiz.title("Agente Gato")
#raiz.geometry("650x350")
raiz.resizable(0,0)
raiz.iconbitmap("gato.ico")
fuente = font.Font(weight='bold')
host = StringVar()
estado = StringVar()
host.set("ws://localhost:9000")
estado.set("Estado:  En reposo")

ltitulo = Label(raiz, text="Agente Gato!!",font=fuente)
ltitulo.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=30)
lestados = Label(raiz, textvariable=estado)
lestados.pack(side=TOP, fill=X, expand=True,padx=10, pady=5)

lhost = Label(raiz, text="Host:",font=fuente)
chost = ttk.Entry(raiz, textvariable=host, width=40)
lhost.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=1)
chost.pack(side=TOP, fill=X, expand=True, padx=10, pady=5)

Button(raiz, text='Conectar', bg="gray",font=fuente, command=conectarWebSocket).pack(padx=15, pady=15,side=TOP)
raiz.mainloop()
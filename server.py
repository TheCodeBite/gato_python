from tornado import websocket
import tornado.ioloop
import json
import time
import threading
import time
import tkinter as tk
from tkinter import messagebox, Label, StringVar, Button
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import tkinter.filedialog as tkFileDialog
import queue

def generear_copia_Matriz(matriz):
    list_matriz=[]
    for fila in range(0,3):
        for columna in range(0,3):
            list_matriz.append(matriz[fila][columna])
    return list_matriz

# PATRON DE DISEÑO SINGLETON PARA QUE SOLO HAYA UNA INSTANCIA DE ESTA CLASE
class Game(object):

    class __Game:
        def __init__(self):
            self.clients = 0
            self.matriz = [['-' for _ in range(3)] for _ in range(3)]
            self.bandera_turno = False
            self.clients_arr = []

        def __str__(self):
            return self.clients

    instance = None

    def __new__(cls):
        if not Game.instance:
            Game.instance = Game.__Game()
        return Game.instance
        

# SE CREA UNA INSTANCIA DE ESTA CLASE POR CADA CONEXIÓN
class EchoWebSocket(websocket.WebSocketHandler):
    
    # Se ejecuta cuando se conecta un cliente
    def open(self):
        self.game = Game()
        self.game.clients_arr.append(self)
        
        # Si hay cupo le envia su id
        if self.game.clients == 0:
            self.write_message(json.dumps({ "id": self.game.clients }))
            print ("Websocket con id " + str(self.game.clients) + " conectado")
            self.game.clients += 1
            stringjaja.set("Esperando a jugador 2...")
        
        # Si se conecta el ultimo cliente iniciar el juego
        elif self.game.clients == 1:
            self.write_message(json.dumps({ "id": self.game.clients }))
            print ("Websocket con id " + str(self.game.clients) + "conectado")
            self.game.clients += 1
            stringjaja.set("COMIENZA EL JUEGO =) GG")

            # Envia el mensaje que al cliente que tira primero
            self.game.bandera_turno = not self.game.bandera_turno # cambio de turno para el siguiente tiro
            message = json.dumps({ "turno": 0, "matriz": self.game.matriz })
            print("turno: 0")
            time.sleep(1)
            self.game.clients_arr[0].write_message(message)

        # Si ya no hay cupo manda un id de -1
        else:
            print ("Websocket sin cuppo")
            self.write_message(json.dumps({"id": -1 }))

    # Se ejecuta cuando recibe un mensaje del ultimo cliente que tiro        
    def on_message(self, message):
        message = json.loads(message)
        
        x = message["x"]
        y = message["y"]
        cliente_id = message["id"]
        ganador = message["ganador"]

        if '-' not in generear_copia_Matriz(self.game.matriz):
            print("Se empato el juego: ")
            tkMessageBox.showinfo("UPPS!", "EMPATE ¬¬")
            message = json.dumps({"empate": 0 })
            self.game.clients_arr[0].write_message(message)
            self.game.clients_arr[1].write_message(message)

        elif ganador:
            print("Gané el juego, mi id es: " + str(cliente_id))

            self.game.matriz[y][x] = cliente_id
            piece = grid[y][x]
            if str(cliente_id) == "0":
                piece.configure(text="X")
            else:
                piece.configure(text="O")

            tkMessageBox.showinfo("GANADOR","GANO ELJUGADOR CON ID "+ str(cliente_id))
            message = json.dumps({ "ganador": cliente_id })
            self.game.clients_arr[0].write_message(message)
            self.game.clients_arr[1].write_message(message)

        else:
            # insertar el id en la matriz de acuerdo a la posicion recibida
            self.game.matriz[y][x] = cliente_id
            print("tiro en x: " + str(x) + " y: " + str(y))
            siguiente_turno = 1 if self.game.bandera_turno else 0
            print(self.game.matriz)
            piece = grid[y][x]

            if str(cliente_id) == "0":
                piece.configure(text="X")
            else:
                piece.configure(text="O")

            message = json.dumps({ "turno": siguiente_turno, "matriz": self.game.matriz })
            print("turno: " + str(siguiente_turno))
            stringTurno.set("Turno "+ str(siguiente_turno))
            time.sleep(1)
            self.game.clients_arr[siguiente_turno].write_message(message)
            
            self.game.bandera_turno = not self.game.bandera_turno  # cambio de turno 
        
    # Se ejecuta cuando se cierra la conexión del cliente
    def on_close(self):
        print ("Websocket closed")
        tkMessageBox.showwarning("ATENCIÓN", "Se desconecto un jugador >:v ")

class Tareas():
    # propiedades de la ventana
    def __init__(self,):
        #self.parent = parent

        global root 
        root = tk.Tk()
        root.geometry("200x100+300+200")
        

        global stringjaja
        stringjaja = tk.StringVar()
        stringjaja.set("ESPERANDO JUGADORES n.n ")

        global otroLabel
        otroLabel = tk.Label(root, text=stringjaja.get(), textvariable=stringjaja)
        otroLabel.grid(row=12, column=0, padx = 20, pady = 5)

        global stringTurno
        stringTurno = tk.StringVar()
        stringTurno.set("Turno 0 ._. ")

        global labelTurno
        labelTurno = tk.Label(root, text=stringTurno.get(), textvariable=stringTurno)
        labelTurno.grid(row=16, column=0, padx = 20, pady = 5)

        global ventanaJuego
        ventanaJuego = tk.Toplevel()
        ventanaJuego.geometry("476x428+700+200")
        ventanaJuego.title("Tablero")

        # etiqueta status interfaz
        self.lbl_estado = tk.Label(root, text='STATUS:')
        self.lbl_estado.grid(row=9, column=0, padx = 20, pady = 5)

        
        blank = " " * 3
        for y in range(3):
            row = []
            for x in range(3):
                b = tk.Button(ventanaJuego, text=blank,height=5,justify="center",width=12, bd=4,font=("Arial", 16))
                #b.config(command=lambda widget=b: self.delete_button(widget))
                b.grid(column=x, row=y)
                #Store row and column indices as a Button attribute
                b.position = (y, x)
                row.append(b)
            grid.append(row)

        root.mainloop()
        
if __name__=='__main__':
    global grid
    grid = []
    
    thr = threading.Thread(name="hilo_grafica",target=Tareas)
    thr.start()

    application = tornado.web.Application([(r"/", EchoWebSocket),])
    application.listen(9000)
    tornado.ioloop.IOLoop.instance().start()
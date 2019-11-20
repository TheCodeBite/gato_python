import random

user = ''
DELIMITADOR = "-"
computer = ''   
posx = 0
posy = 0
ganador = False
segundo_tiro = True
primerTiro = True




tablero = [
    [DELIMITADOR,DELIMITADOR,DELIMITADOR],
    [DELIMITADOR,DELIMITADOR,DELIMITADOR],
    [DELIMITADOR,DELIMITADOR,DELIMITADOR]
]
pos = [0,2]

#MOSTRAR TABLERO
def show_tablero():
    for i in range(0,3):
        print(tablero[i][:])

#RECORRIDO DEL TABLERO
def Recorrido():
    blockX = 0 
    blocky = 0
    gane = False
    win = "not"
    enemy_win = "not"
    gane = ""
    ganador = False
    agregado = False
    #verificamos si podemos ganar en esta jugada
    for y in range(0,3):
        for x in range(0,3):
            if(tablero[y][x] == computer and enemy_win == "not"):
                if(y in pos and x in pos):
                    win,gane, agregado, blockX, blocky, ganador = Buscar_Gane(y, x, tablero, True, computer, user,True)
                else:
                    win,gane, agregado, blockX, blocky, ganador = Buscar_Gane(y,x, tablero, False, computer, user,True)
            if(agregado):
                print("se agrego un valor en jugada para ganar")
                break
    print("VALOR agregado", agregado)
    #verificamos que no haya ninguna jugada en peligro
    if not agregado:
        print("verificamos que no haya jugada peligrosa")
        for y in range(0,3):
            for x in range(0,3):
                if(tablero[y][x] == user and win == "not" ):
                    if(y in pos and x in pos):
                        enemy_win, gane, agregado, blockX, blocky, ganador = Buscar_Gane(y,x, tablero, True, user, computer,False)
                    else: 
                        enemy_win, gane, agregado, blockX, blocky, ganador = Buscar_Gane(y,x, tablero, False, user, computer, False)
                
                if(agregado):
                    print("se agrego un valor  bloquenado")
                    break
    print("VALOR agregado", agregado)
    if not agregado:
        print("no hay jugadas que genern peligro al bot")
        for y in range(0,3):
            for x in range(0, 3):
                if(tablero[y][x] == computer and y in pos and x in pos):
                    agregado, blockX, blocky, ganador = agrega_posicion(tablero, y, x, True)
                if(agregado):
                    print("se agrego")
                    break
    return blockX, blocky, ganador

def agrega_posicion(tablero, y, x, corner):
    global segundo_tiro
    posX = 0 
    posY = 0
    agregado = False

    print("x",x,"y", y)
    if((y == 0 and x == 0 and segundo_tiro) or (y == 0 and x == 2 and segundo_tiro and agregado == False)):
        if(tablero[2][1] == DELIMITADOR and tablero[2][0] == DELIMITADOR and tablero[2][2] == DELIMITADOR and agregado == False):
            tablero[2][1] = computer
            posX = 1
            posY = 2
            agregado = True
            segundo_tiro = False
    elif((y == 2 and x == 0 and segundo_tiro) or (y == 2 and x == 2 and segundo_tiro) and agregado == False):
        print("no hay pedos we aca arriba", tablero[0][1] , "-", tablero[0][0], tablero[0][2] )
        if(tablero[0][1] == DELIMITADOR and tablero[0][0] == DELIMITADOR and tablero[0][2] == DELIMITADOR and agregado == False):
            print("añadiendo", computer)
            tablero[0][1] = computer
            segundo_tiro = False
            agregado = True
            posX = 1
            posY = 0
    if(tablero[0][0] == DELIMITADOR and tablero[1][0] == DELIMITADOR and tablero[2][0] == DELIMITADOR and agregado == False):
        tablero[1][0] = computer
        print("Added")
        agregado = True
        posX = 0
        posY = 1

    elif(tablero[2][2] == DELIMITADOR and tablero[2][1] == DELIMITADOR and tablero[2][0] == DELIMITADOR and agregado == False):
        tablero[2][1] = computer
        print("Added")
        agregado = True
        posX = 1
        posY = 2

    if(tablero[0][0] == computer and tablero[2][1] == computer and tablero[1][0] == DELIMITADOR and tablero[2][0] == DELIMITADOR and agregado == False):
        tablero[2][0] = computer
        print("Added")
        agregado = True
        posX = 0
        posY = 2

    elif(tablero[0][2] == computer and tablero[2][1] == computer and tablero[1][2] == DELIMITADOR and tablero[2][2] == DELIMITADOR and agregado == False):
        tablero[2][2] = computer
        print("Added")
        agregado = True
        posX = 2
        posY = 2

    elif(tablero[2][0] == computer and tablero[0][1] == computer and tablero[0][0] == DELIMITADOR and tablero[1][0] == DELIMITADOR and agregado == False):
        tablero[0][0] = computer
        print("Added")
        agregado = True
        posX = 0
        posY = 0

    elif(tablero[2][2] == computer and tablero[0][1] == computer and tablero[0][2] == DELIMITADOR and tablero[1][2] == DELIMITADOR and agregado == False):
        tablero[0][2] = computer
        print("Added")
        agregado = True
        posX = 2
        posY = 0

    elif(tablero[1][0] == computer and tablero[2][2] == computer and tablero[2][0] == DELIMITADOR and tablero[2][1] == DELIMITADOR and agregado == False):
        tablero[2][0] = computer
        print("Added")
        agregado = True
        posX = 0
        posY = 2

    elif(tablero[2][0] == computer and tablero[1][2] == computer and tablero[2][2] == DELIMITADOR and tablero[2][1] == DELIMITADOR and agregado == False):
        tablero[2][2] = computer
        print("Added")
        posX = 2
        posY = 2
        agregado = True

    elif(tablero[0][0] == computer and tablero[1][2] == computer and tablero[0][1] == DELIMITADOR and tablero[0][2] == DELIMITADOR and agregado == False):
        tablero[0][2] = computer
        print("Added")
        agregado = True
        posX = 2
        posY = 0

    elif (tablero[0][2] == computer and tablero[1][0] == computer and tablero[0][0] == DELIMITADOR and tablero[0][1] == DELIMITADOR and agregado == False):
        tablero[0][0] = computer
        print("Added")
        agregado = True

    if(agregado == False):    
        salida = True
        while salida:
            posY = random.randint(0,2)
            posX = random.randint(0,2)

            if(tablero[posY][posX] == DELIMITADOR):
                print("No se encontro nada asi que hicimos un random X",posX,"Y",posY)
                tablero[posY][posX] = computer
                salida = False
                agregado = True
    
    return agregado, posX, posY, False


#AUMENTA PROBABILIDAD DE GANE
def primer_tiro(ficha):
    global primerTiro, DELIMITADOR
    print("mi ficha es: ", ficha)
    print("delitimitador: ", DELIMITADOR)
    x = 1
    y = 1
    if(tablero[1][1] == DELIMITADOR and ficha in tablero == False):
        y = pos[random.randint(0,1)]
        x = pos[random.randint(0,1)]
        tablero[ y ] [ x ] = ficha
    else:
        print("falso")
        tablero[x][y] = ficha
    
    primerTiro = False
    return x,y,False


def Buscar_Gane(y, x, tablero, corner, ficha, ficha_enemy, ia):
    contador = 1
    contador_enemigo = 1
    agregado = False
    bloqX = 0
    bloqY = 0
    gane=""
    retorno = ""
    #buscamos derecha izquierda
    for i in range(x+1, 3):
        if(tablero[y][i] == DELIMITADOR):
            bloqY = y
            bloqX = i

        if(tablero[y][i] == ficha_enemy):
            contador_enemigo = contador_enemigo + 1
            contador = 0
        elif(tablero[y][i] == ficha):
            contador = contador + 1

    for i in range (x-1, 0, -1):
        if(tablero[y][i] == DELIMITADOR):
            bloqY = y
            bloqX = i
        if(tablero[y][i] == ficha_enemy):
            contador_enemigo = contador_enemigo + 1
            contador = 0
        elif(tablero[y][i] == ficha):
            contador = contador + 1
    
    if(contador == 2):
        retorno = "win"
        gane = "lados"
        if(not (ia)):
            if(tablero[bloqY][bloqX] == DELIMITADOR):
                print("bloqueando -> posicion x", bloqX, "y",bloqY)
                tablero[bloqY][bloqX] = ficha_enemy
                agregado = True
            else:
                print("posicion ocupada", "X", bloqX, "Y", bloqY)
        elif(ia):
            if(tablero[bloqY][bloqX] == DELIMITADOR):
                print("añadiendo -> posicion x", bloqX, "y",bloqY)
                tablero[bloqY][bloqX] = ficha
                agregado = True
            else:
                print("posicon ocupada", "X", bloqX, "Y", bloqY)
    else:
        retorno = "not"
    
    #verificamos arriba y abajo
    if(not(retorno == "win")):
        contador = 1
        for i in range(y+1, 3):
            if(tablero[i][y] == DELIMITADOR):
                bloqY = i
                bloqX = x

            if(tablero[i][x] == ficha_enemy):
                contador = 0
                contador_enemigo = contador_enemigo + 1
            elif(tablero[i][x] == ficha):
                contador = contador + 1

        for i in range (y-1, 0, -1):
            if(tablero[y][i] == DELIMITADOR):
                bloqY = i
                bloqX = x

            if(tablero[i][x] == ficha_enemy):
                contador = 0
                contador_enemigo = contador_enemigo + 1
            elif(tablero[i][x] == ficha):
                contador = contador + 1
        if(contador == 2):
            retorno = "win"
            gane = "arriba"
            
            if(not (ia)):
                if(tablero[bloqY][bloqX] == DELIMITADOR):
                    print("bloqueando posicion x", bloqX, "y",bloqY)
                    tablero[bloqY][bloqX] = ficha_enemy
                    agregado = True
                else: 
                    print("posicion ocupada", "X", bloqX, "Y", bloqY)
            elif(ia):
                if(tablero[bloqY][bloqX] == DELIMITADOR):
                    print("añadiendo posicion x", bloqX, "y",bloqY)
                    tablero[bloqY][bloqX] = ficha
                    agregado = True
                else:
                    print("posicion ocupada", "X", bloqX, "Y", bloqY)
        else:
            retorno = "not"

    if(corner and retorno == "not" and agregado == False):
        if((y == 0 and x == 0) or (y == 2 and x == 2)):
            contador = 1
            for i in range(x+1, 3):
                if(tablero[i][i] == DELIMITADOR):
                    bloqX = i
                    bloqY = i
                if(tablero[i][i] == ficha_enemy):
                    contador = 0
                    contador_enemigo = contador_enemigo + 1
                elif(tablero[i][i] == ficha):
                    contador = contador + 1
            for i in range(x-1, 0, -1):
                if(tablero[i][i] == DELIMITADOR):
                    bloqX = i
                    bloqY = i
                if(tablero[i][i] == ficha_enemy):
                    contador = 0
                    contador_enemigo = contador_enemigo + 1
                elif(tablero[i][i] == ficha):
                    contador = contador + 1
            if(contador == 2):
                retorno = "win"
                gane = "equis"
        
                if(not (ia)):
                    if(tablero[bloqY][bloqX] == DELIMITADOR):
                        print("bloqueando posicion x", bloqX, "y",bloqY)
                        print("bloqeando X")
                        tablero[bloqY][bloqX] = ficha_enemy
                        agregado = True
                    else: 
                        print("posicion ocupada", "X", bloqX, "Y", bloqY)
                        print("ganando equis")
                elif(ia):
                    if(tablero[bloqY][bloqX] == DELIMITADOR):
                        print("añadiendo posicion x", bloqX, "y",bloqY)
                        tablero[bloqY][bloqX] = ficha
                        agregado = True
                    else:
                        print("posicion ocupada", "X", bloqX, "Y", bloqY)
        if((y == 0 and x == 2) or (y == 2 and x == 0)): 
            contador = 1
            for i in range(y+1, 3):
                if(tablero[y + i][x - i] == DELIMITADOR):
                    bloqX = x - i
                    bloqY = y + i
                if(tablero[y + i][x - i] == ficha_enemy):
                    contador = 0
                    contador_enemigo = contador_enemigo + 1
                elif(tablero[y + i][x - i] == ficha):
                    contador = contador + 1
            for i in range(y-1, 0, -1):
                if(tablero[y - i][x + i] == DELIMITADOR):
                    bloqX = x + i
                    bloqY = x - i
                if(tablero[y - i][x + i] == ficha_enemy):
                    contador = 0
                    contador_enemigo = contador_enemigo + 1
                elif(tablero[y - i][x - i] == ficha):
                    contador = contador + 1
            if(contador == 2):
                retorno = "win"
                gane = "arriba"
                
                if(not (ia)):
                    if(tablero[bloqY][bloqX] == DELIMITADOR):
                        print("bloqueando posicion x", bloqX, "y",bloqY)
                        print("bloqueando equis")
                        tablero[bloqY][bloqX] = ficha_enemy
                        agregado = True
                    else: 
                        print("posicion ocupada", "X", bloqX, "Y", bloqY)
                elif(ia):
                    if(tablero[bloqY][bloqX] == DELIMITADOR):
                        print("añadiendo posicion x", bloqX, "y",bloqY)
                        print(" equis")
                        tablero[bloqY][bloqX] = ficha
                        agregado = True
                    else:
                        print("posicion ocupada", "X", bloqX, "Y", bloqY)
            else:
                retorno = "not"
                
    
    return retorno, gane, agregado, bloqX, bloqY, False

            

#Seleccionar jugador
def Elejir_ficha_jugador(ficha):
    global computer, user
    if(ficha == "1"):
        user = ficha
        computer = "0"
    elif(ficha == "0"):
        user = ficha
        computer = "1"
    
    print("mi id es", computer)

##MAIN
end_game = False
def continuar_juego(table, ficha):
    global posx, posy, ganador,tablero, computer, user
    tablero = table
    print(tablero)
    #Elejir_ficha_jugador(ficha)
    if((str(ficha)) == '1'):
        user = '1'
        computer = "0"
    elif(str(ficha) == '0'):
        user = '0'
        computer = "1"
    
    print("mi id es", computer)

    if(not(end_game)):
        print("User",user,"Computer",computer)

        show_tablero()
        valor = computer in tablero == False
        print("si ", computer, " in \n", tablero, " = false", " Valor",str(valor))
        if(not computer in tablero):
            print("no hay posicion")
            posx, posy, ganador = primer_tiro(computer)
        else: 
            print("seguimo el juego")
            posx, posy, ganador = Recorrido()
    print("___________________________________________________")
    return posx, posy, ganador

#continuar_juego()

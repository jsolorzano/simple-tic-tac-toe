# -*- coding: utf-8 -*-

'''
Un simple programa que simula jugar a tic-tac-toe (nombre en inglés) 
con el usuario.
'''
def DisplayBoard(board):
    #
    # la función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola
    #
    # ~ print(board)
    print("+-------+-------+-------+")
    for row in board:
		    print("|       |       |       |")
		    print("|   "+row[0]+"   |   "+row[1]+"   |   "+row[2]+"   |")
		    print("|       |       |       |")
		    print("+-------+-------+-------+")

def EnterMove(board):
    #
    # la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
    #
    print("Turno para ti")
    entrada = True
    choose_box = int(input("Elije una casilla: (1 - 9): "))
    while entrada:
        if choose_box > 0 and choose_box < 10:
            if choose_box != 5:
                row = 0
                col = choose_box - 1
                if choose_box > 3 and choose_box < 7:
                    row = 1
                    col = choose_box - 4
                elif choose_box > 6:
                    row = 2
                    col = choose_box - 7
                
                print("Test", row, col)

                if board[row][col] != "X" and board[row][col] != "O":
                    board[row][col] = "O"
                    entrada = False
                else:
                    choose_box = int(input("La casilla está ocupada elije otra: (1 - 9): "))
            else:
                choose_box = int(input("La casilla está ocupada elije otra: (1 - 9): "))
        else:
            choose_box = int(input("Elije una casilla: (1 - 9): "))
				

def MakeListOfFreeFields(board):
    #
    # la función examina el tablero y construye una lista de todos los cuadros vacíos 
    # la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
    #
    ListOfFreeFields = []
    for key_r in range(len(board)):
		    for key_b in range(len(board[key_r])):
			      if board[key_r][key_b] != 'O' and board[key_r][key_b] != 'X':
				        ListOfFreeFields.append((key_r, key_b))
	
    return ListOfFreeFields

def VictoryFor(board, sign):
    #
    # la función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego
    #
    combinaciones = [
		[board[0][0],board[0][1],board[0][2]],
		[board[1][0],board[1][1],board[2][2]],
		[board[2][0],board[2][1],board[2][2]],
		[board[0][0],board[1][0],board[2][0]],
		[board[0][1],board[1][1],board[2][1]],
		[board[0][2],board[1][2],board[2][2]],
		[board[0][0],board[1][1],board[2][2]],
		[board[0][2],board[1][1],board[2][0]]
    ]
    
    combinacion_hecha = False
    
    for combinacion in combinaciones:
        cont = 0
        for elem in combinacion:
            if elem == sign:
                cont += 1
        if cont == 3:
            combinacion_hecha = True

    return combinacion_hecha

def DrawMove(board):
    #
    # la función dibuja el movimiento de la maquina y actualiza el tablero
    #
    print("Turno para la computadora")
    entrada = True
    choose_box = randrange(10)
    while entrada:
        if choose_box > 0 and choose_box < 10:
            if choose_box != 5:
                row = 0
                col = choose_box - 1
                if choose_box > 3 and choose_box < 7:
                    row = 1
                    col = choose_box - 4
                elif choose_box > 6:
                    row = 2
                    col = choose_box - 7
                
                print("Test", row, col)

                if board[row][col] != "X" and board[row][col] != "O":
                    board[row][col] = "X"
                    entrada = False
                else:
                    choose_box = randrange(10)
            else:
                choose_box = randrange(10)
        else:
            choose_box = randrange(10)


from random import randrange

# ~ for i in range(10):
    # ~ print(randrange(8))
    
board = [
	['1', '2', '3'],
	['4', '5', '6'],
	['7', '8', '9']
]

print("*** Inicio ***")
DisplayBoard(board)

for turn in range(1, 10):
	
	if turn % 2 == 0:
		print("*** Jugada "+str(turn)+" (Tu) ***")
		EnterMove(board)
		DisplayBoard(board)
		
		if VictoryFor(board, "O"):
			print("Tu has ganado")
			break
	else:
		print("*** Jugada "+str(turn)+" (CPU) ***")
		if turn == 1:
			print("Turno para la computadora")
			board[1][1] = "X"
			DisplayBoard(board)
		else:
			DrawMove(board)
			DisplayBoard(board)
		
		if VictoryFor(board, "X"):
			print("CPU ha ganado")
			break

# ~ ListOfFreeFields = MakeListOfFreeFields(board)

# ~ print(ListOfFreeFields)

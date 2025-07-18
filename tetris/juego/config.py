import pygame

#tamaño del juego
columnas=10
filas=20
celda=30

jue_ancho=columnas*celda
jue_alto=filas*celda

#area de puntos y fichas
barra_ancho=200
barra_poral=.7
puntos_al=1-barra_poral

#ventana
esp=20
ven_alto=jue_alto+esp*2
ven_ancho=jue_ancho+barra_ancho+esp*3




TETROMINOS = {
'T': {'forma': [(0,0), (-1,0), (1,0), (0,-1)], 'color': '#7b217f'},
'O': {'forma': [(0,0), (0,-1), (1,0), (1,-1)], 'color': '#f1e60d'},
'J': {'forma': [(0,0), (0,-1), (0,1), (-1,1)], 'color': '#204b9b'},
'L': {'forma': [(0,0), (0,-1), (0,1), (1,1)], 'color': '#f07e13'},
'I': {'forma': [(0,0), (0,-1), (0,-2), (0,1)], 'color':  '#6cc6f9'},
'S': {'forma': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': '#65b32e'},
'Z': {'forma': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': '#e51b20'}
}

puntos_data={1:40,2:100,3:300,4:1200}
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog
# Inicializa a variável pública resources como uma lista vazia
matrixs = []
x_size = 100
y_size = 100
colorss=0
def getxy(x, y):
    if x>-1:
      if y> -1:
          if x<x_size:
              if y<y_size:
                  return y*x_size+x
              else:
                  return -1
def setxy(x, y,color,matrix):
    z=getxy(x, y)
    if z>(-1):
        if z< x_size*y_size:
            matrix[z]=chr(color & 255)
    return matrix
def retxy(x, y,matrix):
    chr0=chr(0)
    if z>-1:
        z=getxy(x, y)
        chr0=matrix[z]
    return chr0
def pset(x, y,color,matrix):
    z=getxy(x, y)
    if z>(-1):
        if z< x_size*y_size:
            matrix[z]=chr(color & 255)
    return matrix
def point(x, y,matrix):
    chr0=chr(0)
    if z>-1:
        z=getxy(x, y)
        chr0=matrix[z]
    return chr0
def report(matrix):
    # Isso imprimirá a matriz criada
    for yy in range(y_size):
        print(matrix[yy*x_size:yy*x_size+x_size])
# Função para criar uma matriz x por y
def create_array(x, y,color):
    matrixs = []
    colun=[]
    x_size = x
    y_size = y
    if x <= 0 or y <= 0:
        raise ValueError("Os valores de x e y devem ser maiores que zero.")
    for xx in range(0,x*y):
        colun=colun+[chr(color & 255)]
        
    # Cria uma matriz vazia com o tamanho especificado
    print(len(colun))
    return colun
def hline (x, y,x1,color,matrix):
    if x1>x:
        for aa in range(x,x1):
            pset(aa,y,color,matrix)
def box (x, y,x1,y1,color,matrix):
    if x1>x:
        if y1>y:
            for aa in range(y,y1):
                hline(x,aa,x1,color,matrix)
def vline (x, y,y1,color,matrix):
    if y1>y:
        for aa in range(y,y1):
            pset(x,aa,color,matrix)
# Função para desenhar uma linha
def draw_line(draw, args):
    draw.line(args, fill="white", width=1)

# Função principal do interpretador
def interpretador_grafico(commands):
    for command in commands:
        parts = command.split(",")
        keyword = parts[0]

        if keyword == "hline":
            hline(int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]),matrixs)
        elif keyword == "vline":
            vline(int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]),matrixs)
        elif keyword == "box":
            box(int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]),colorss,matrixs)
        elif keyword == "bit":
            matrixs=create_array(int(parts[1]), int(parts[2]), int(parts[3]))
            
        elif keyword == "color":
            colorss=int(parts[1])

    with open("out.raw", 'w') as file:
        file.write(''.join(matrixs))
  

# Função para abrir a imagem no visualizador padrão do Windows
def abrir_imagem():
        with open("out.raw", 'w') as file:
            file.write(''.join(matrixs))

# Interface gráfica para inserir os comandos
root = tk.Tk()
root.title("Interpretador Gráfico")
root.configure(bg="blue")  # Define a cor de fundo da janela como azul
text = tk.Text(root,wrap="none", width=40, height=10, bg="blue", fg="white")
text.pack()
texto_pre_escrito = """bit,100,100,1,0
hline,0,0,1,100,9
vline,0,0,100,9
color,9,0,0,0
box,10,10,100,100"""
text.insert("1.0", texto_pre_escrito)
button = tk.Button(root, text="Interpretar e Visualizar", command=lambda: interpretador_grafico(text.get("1.0", "end-1c").split("\n")))
button.pack()

open_button = tk.Button(root, text="salvar Imagem", command=abrir_imagem)
open_button.pack()

root.mainloop()

import tkinter as tk
import random
from PIL import Image

image_jpeg = Image.open("imgs/background.jpg")

# Define o caminho e o nome do arquivo PNG de saída
output_path = "imgs/background.png"

# Salva a imagem JPEG como PNG
image_jpeg.save(output_path, "PNG")

# Criação da janela
window = tk.Tk()
window.title("Meu Jogo")
window.geometry("1300x750")
# Define a cor de fundo da janela
window.configure(background="#3a9c95")  # Substitua pela cor desejada

# Criação do Canvas
canvas = tk.Canvas(window, width=1200, height=675)
canvas.pack()

# Carregamento e exibição da imagem de fundo
background_image = tk.PhotoImage(file="imgs/background.png")
canvas.create_image(0, 0, anchor="nw", image=background_image)


# Cores
BLACK = "#000000"
WHITE = "#FFFFFF"

# Criação de um rótulo para exibir a pontuação
pontuacao = 0
pontuacao_label = tk.Label(window, text="Pontuação: " + str(pontuacao))
pontuacao_label.pack()

# Carregamento e exibição da imagem
image = tk.PhotoImage(file="imgs/Target-icon.png")
image_label = tk.Label(window, image=image)
image_label.place(x=350, y=250)  # Define a posição inicial da imagem

def mover_imagem(event):
    global pontuacao

    # Gera novas coordenadas X e Y para a imagem
    new_x = random.randint(0, 700)
    new_y = random.randint(0, 500)
    image_label.place(x=new_x, y=new_y)

    # Incrementa a pontuação ao mover a imagem
    pontuacao += 1
    pontuacao_label.config(text="Pontuação: " + str(pontuacao))

# Associa a função mover_imagem ao evento de clique na imagem
image_label.bind("<Button-1>", mover_imagem)

window.mainloop()

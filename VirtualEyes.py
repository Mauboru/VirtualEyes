import tkinter, tkVideoPlayer

#Funções
def telaCheia(event=None):
    fullscreen = Tela.attributes("-fullscreen")
    Tela.attributes("-fullscreen", not fullscreen)

def exibirTexto(texto):
    textoLabel.config(text=texto)

def loadingPlay(path, texto):
    video.stop()
    video.load(path)
    exibirTexto(texto)
    Tela.after(100, video.play)

def loopVideo(event):
    video.play()

#Tela
Tela = tkinter.Tk()
Tela.title("Expressões do ORACULO")
Tela.geometry("280x250+600+200")
Tela.attributes("-fullscreen", True)

# Configurar tecla de atalho para alternar o modo fullscreen (por exemplo, F11)
Tela.bind("<F11>", telaCheia)
Tela.bind("<Escape>", telaCheia)

# Mapeamento de teclas para expressões
expressoes = {
    "a": ("./Videos/expression_angry.mp4", "Expressão: Raiva"),
    "b": ("./Videos/expression_boring.mp4", "Expressão: Chateado"),
    "h": ("./Videos/expression_happy.mp4", "Expressão: Feliz"),
    "i": ("./Videos/expression_idle.mp4", "Expressão: Parado"),
    "l": ("./Videos/expression_loved.mp4", "Expressão: Apaixonado"),
    "s": ("./Videos/expression_sad.mp4", "Expressão: Triste"),
}

for key, (path, texto) in expressoes.items():
    Tela.bind(f"<{key}>", lambda event, v=path, t=texto: loadingPlay(v, t))

#Video
video = tkVideoPlayer.TkinterVideo(Tela, scaled=True)
video.grid(row=0, columnspan=3, sticky="nsew")
Tela.grid_rowconfigure(0, weight=1)
Tela.grid_columnconfigure(0, weight=1)

# Rótulo para exibir o texto
textoLabel = tkinter.Label(Tela, text="Expressão: Nenhuma", font=("Arial", 16))
textoLabel.grid(row=1, columnspan=3)

#Iniciando sempre em parado e ao encerrar vídeo repetir
loadingPlay("./Videos/expression_idle.mp4", "Expressão: Parado")
video.bind('<<Ended>>', loopVideo)

Tela.mainloop()
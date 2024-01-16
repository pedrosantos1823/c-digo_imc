import tkinter as tk

root = tk.Tk()
root.title('Calculadora do IMC')

def calcular():
    peso = float(pesoin.get())
    altura = float(alturain.get())
    imc = int(peso / (altura * altura))
    imc_str = str(imc)
    resultado.config(text = 'Seu IMC é '+ imc_str)
    if imc <= 18.5:
        resultado2.config(text = 'Você está abaixo do peso')
    elif imc in range(19,24):
        resultado2.config(text = 'Seu peso é ideal')
    else:
        resultado2.config(text = 'Você está acima do peso')

pesotxt = tk.Label(root, text = 'Insira seu peso (kg):')
pesotxt.pack()
pesoin = tk.Entry(root)
pesoin.pack()

alturatxt = tk.Label(root, text = 'Insira sua altura (m):')
alturatxt.pack()
alturain = tk.Entry(root)
alturain.pack()

botao = tk.Button(root, text = 'Calcular', command = calcular)
botao.pack()

resultado = tk.Label(root, text = '')
resultado.pack()

resultado2 = tk.Label(root, text = '')
resultado2.pack()

root.mainloop()

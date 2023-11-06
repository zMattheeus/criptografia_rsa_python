import random
import math
from tkinter import *

descrypt = "Matheus"

# Função para verificar se um número é primo usando o teste de Miller
def verificador_primo(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False

    return True

# Função para gerar um número primo aleatório com um número específico de bits
def gerar_num_primo(bits):
    while True:
        num = random.getrandbits(bits)
        if verificador_primo(num):
            return num

# Função para calcular o MDC (máximo divisor comum) de dois números
def max_div_comum(a, b):
    while b:
        a, b = b, a % b
    return a

# Função para calcular o inverso multiplicativo de 'a' mod 'm' usando o algoritmo de Euclides estendido
def mod_inverso(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Função para gerar as chaves pública e privada
def gerar_chaves(bits):
    p = gerar_num_primo(bits)
    q = gerar_num_primo(bits)
    n = p * q
    phi = (p - 1) * (q - 1) # Função totiente de Euler

    # Expoente de cifragem 'e' (geralmente um número pequeno, por exemplo, 65537)
    e = 65537

    # Calcular o expoente de decifragem 'd' usando o inverso multiplicativo
    d = mod_inverso(e, phi)

    return ((n, e), (n, d))

# Função para criptografar uma mensagem
def criptografar(chave_publica, mensagem):
    n, e = chave_publica
    mensagem_criptografada = [pow(ord(char), e, n) for char in mensagem]
    return mensagem_criptografada

# Função para descriptografar uma mensagem
def descriptografar(chave_privada, mensagem_criptografada):
    n, d = chave_privada
    mensagem_descriptografada = ''.join([chr(pow(char, d, n)) for char in mensagem_criptografada])
    return mensagem_descriptografada

# Teste do algoritmo
bits = 28  # Tamanho dos números primos, quanto maior, maior será o numero de cada caracter
chave_publica, chave_privada = gerar_chaves(bits)


def botao_cript():
    
    global mensagem
    mensagem = entry_msg.get()

    if len(mensagem) > 128:
       texto_128 = "Digite uma mensagem com apenas 128 caracteres"
    else:
        texto_128 = f"Mensagem original: {mensagem}"

        global mensagem_criptografada
        mensagem_criptografada = criptografar(chave_publica, mensagem)
        texto_cripto = f"Mensagem criptografada: {mensagem_criptografada}"
    
    msg_original["text"] = texto_128
    msg_criptografada["text"] = texto_cripto
   

def btn_descript():
            chave = entry_chave.get()

            if chave != descrypt:
                key = "Chave incorreta"
    
            else:
                mensagem_descriptografada = descriptografar(chave_privada, mensagem_criptografada)
                key = f"Mensagem descriptografada: {mensagem_descriptografada}"

            mensagem_descriptografada_label["text"] = key


janela = Tk()

janela.title("Criptografia APS")
janela.config(bg= "#151919")
janela.geometry("1124x400")

# Apresentação
texto_apresentacao = Label(janela, text="Telinha em Python",bg="#151919", fg="white", font=("Helvetica", 14))
texto_apresentacao.grid(column=1, row=0, pady=15)

# Digite a mensagem que vai ser criptografada
digite_msg = Label(janela, text ="Digite sua mensagem: ", bg="#151919", fg="white")
digite_msg.grid(column=0, row=1, padx=10)
entry_msg = Entry(janela, width=130)
entry_msg.grid(column=1, row=1, padx=15, pady=10)

# Botão da criptografia

botao_criptografar = Button(janela, text="Clique para criptografar", command=botao_cript, bg="#151919", fg="white")
botao_criptografar.grid(column=2, row=1, padx=10)

# Mostrar a menssagem original
msg_original = Label(janela, text="", bg="#151919", fg="white")
msg_original.grid(column=1, row = 3, pady=10)

# Mostrar a menssagem criptografada
msg_criptografada = Label(janela, text="", bg="#151919", fg="white")
msg_criptografada.grid(column=1, row=5, pady=10)

# Pedir a chave

pedir_chave = Label(janela, text="Chave: ", bg="#151919", fg="white")
pedir_chave.grid(column=0, row=7)
entry_chave = Entry(janela, width=130)
entry_chave.grid(column=1, row=7, padx=15, pady=10)

# Botão para descriptografar com a chave

btn_chave = Button(janela, text="Inserir Chave", command=btn_descript, bg="#151919", fg="white")
btn_chave.grid(column=2, row=7, padx=10)

# Mostrar mensagem descriptografada

mensagem_descriptografada_label = Label(janela, text="", bg="#151919", fg="white")
mensagem_descriptografada_label.grid(column=1, row=8, pady=20)

janela = mainloop()
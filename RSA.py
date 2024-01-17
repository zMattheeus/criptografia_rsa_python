import random
import math

chave_tradata = []

# Função para verificar se um número é primo usando o teste de Miller-Rabin
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

    # Escolher um expoente de cifragem 'e' (geralmente um número pequeno, por exemplo, 65537)
    e = 65537

    # Calcular o expoente de decifragem 'd' usando o inverso multiplicativo
    d = mod_inverso(e, phi)

    return ((n, e), (n, d))

# Função para criptografar uma mensagem
def criptografar(chave_publica, mensagem):
    n, e = chave_publica
    menssagem_criptografada = [pow(ord(char), e, n) for char in mensagem]
    return menssagem_criptografada

# Função para descriptografar uma mensagem
def descriptografar(chave_privada, menssagem_criptografada):
    n, d = chave_privada
    menssagem_descriptografada = ''.join([chr(pow(char, d, n)) for char in menssagem_criptografada])
    return menssagem_descriptografada

# Teste do algoritmo
bits = 28  # Tamanho dos números primos, quanto maior, maior será o numero de cada caracter
chave_publica, chave_privada = gerar_chaves(bits)


chave_tradata.extend(chave_privada)

resultado = ', '.join(map(str, chave_tradata))

resultado_sem_virgulas_espacos = resultado.replace(',', '').replace(' ', '')



mensagem = input("Digite sua mensagem: ")
if len(mensagem) > 128:
  print("Digite uma menssagem com apenas 128 caracteres")
else:
  print(f"Mensagem original: {mensagem}")
    
  mensagem_criptografada = criptografar(chave_publica, mensagem)
  print(f"Mensagem criptografada: {mensagem_criptografada}")

  print(resultado_sem_virgulas_espacos)

  chave = input("Digite a Chave de descriptografia: ")

  
  
  if chave != resultado_sem_virgulas_espacos:
    print("Chave incorreta")
  
  else:
    mensagem_descriptografada = descriptografar(chave_privada, mensagem_criptografada)
    print(f"Mensagem descriptografada: {mensagem_descriptografada}")
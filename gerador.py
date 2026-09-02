import sys
import random
import string

def gerar_id():
    sufixo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"AP-{sufixo}"

def validar_aposta(linha):
    partes = linha.strip().split(",")
    numeros = partes[1:]
    return 6 <= len(numeros) <= 15

def gerar_linha_aposta():
    id_aposta = gerar_id()
    qtd_numeros = random.randint(6, 15)
    numeros = sorted(random.sample(range(1, 61), qtd_numeros))
    return f"{id_aposta}," + ",".join(map(str, numeros))

if __name__ == "__main__":
    qtd_linhas = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    with open("apostas.csv", "w") as f:
        processadas = 0
        while processadas < qtd_linhas:
            linha = gerar_linha_aposta()
            if validar_aposta(linha):
                f.write(linha + "\n")
                processadas += 1
import random
import string

def gerar_linha():
    sufixo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    id_aposta = f"AP-{sufixo}"
    
    qtd = random.randint(6, 15)
    numeros = sorted(random.sample(range(1, 61), qtd))
    
    return f"{id_aposta}," + ",".join(map(str, numeros))

with open("apostas.csv", "w") as f:
    for _ in range(10):
        f.write(gerar_linha() + "\n")
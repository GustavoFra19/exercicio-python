nivelAcesso = 6
portaDestravada = False

if nivelAcesso >= 5:
    portaDestravada = True
    print("Acesso liberado! seu nivel de acesso é: ", nivelAcesso)
else: 
    print("Acesso negado")
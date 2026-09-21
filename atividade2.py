def analisar_temperaturas(temperaturas):
    soma = 0
    alertas = 0

    for temperatura in temperaturas:
        soma += temperatura

        if temperatura > 30.0:
            alertas += 1

    media = soma / len(temperaturas)

    return media, alertas

def main():
    temperaturas = [22.5, 25.0, 31.2, 28.4, 19.8]

    media, alertas = analisar_temperaturas(temperaturas)

    print("=== Análise das Temperaturas ===")
    print(f"Temperatura média do dia: {media:.2f} °C")
    print(f"Quantidade de alertas de calor: {alertas}")


main()   
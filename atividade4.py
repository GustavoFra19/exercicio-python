class DispositivoIot:
    def __init__(self, nome, bateria):
        self.nome = nome

        if bateria < 0:
            self.bateria = 0
        elif bateria > 100:
            self.bateria = 100
        else:
            self.bateria = bateria


class HubCentral:
    def __init__(self):
        self.dispositivos_conectados = []

    def adicionar_dispositivo(self, dispositivo):
        self.dispositivos_conectados.append(dispositivo)

    def relatorio_bateria_baixa(self):
        nomes_baixa = []

        for dispositivo in self.dispositivos_conectados:
            if dispositivo.bateria < 20:
                nomes_baixa.append(dispositivo.nome)

        if not nomes_baixa:
            return "Nenhum dispositivo com bateria abaixo de 20%."

        return ", ".join(nomes_baixa)


sensor1 = DispositivoIot("Sensor Sala", 18)
sensor2 = DispositivoIot("Câmera Jardim", 45)
sensor3 = DispositivoIot("Termostato", 12)

hub = HubCentral()
hub.adicionar_dispositivo(sensor1)
hub.adicionar_dispositivo(sensor2)
hub.adicionar_dispositivo(sensor3)

print("Dispositivos com bateria abaixo de 20%:")
print(hub.relatorio_bateria_baixa())

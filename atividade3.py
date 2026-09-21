class LuminariaSmart:
    def __init__(self, id_dispositivo, ligada=False, intensidade=0):
        self.id_dispositivo = id_dispositivo
        self.ligada = ligada
        self.intensidade = intensidade

    def inverter_estado(self):
        self.ligada = not self.ligada

    def ajustar_intensidade(self, nova_intensidade):
        if nova_intensidade < 0:
            self.intensidade = 0
        elif nova_intensidade > 100:
            self.intensidade = 100
        else:
            self.intensidade = nova_intensidade

    def __str__(self):
        return (
            f"LumináriaSmart(id={self.id_dispositivo}, "
            f"ligada={self.ligada}, intensidade={self.intensidade}%)"
        )


luminaria = LuminariaSmart(id_dispositivo=101)
luminaria.inverter_estado()
luminaria.ajustar_intensidade(75)

print(luminaria)

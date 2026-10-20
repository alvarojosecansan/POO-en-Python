class TarjetaCredito:
    def __init__(self, titular): self.titular = titular
    def calcular_cashback(self, monto): return 0.0

class TarjetaGold(TarjetaCredito):
    def calcular_cashback(self, monto): return monto * 0.02

class TarjetaBlack(TarjetaCredito):
    def calcular_cashback(self, monto): return monto * 0.05

monto = 100000
for t in [TarjetaCredito("Carlos"), 
          TarjetaGold("Alvaro"), 
          TarjetaBlack("Maria")]:
    print(f"Titular: {t.titular}, cashback de ${t.calcular_cashback(monto):.2f} por una compra de ${monto:.2f}")
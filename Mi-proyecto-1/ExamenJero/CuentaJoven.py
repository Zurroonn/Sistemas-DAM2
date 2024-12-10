class CuentaCorriente:
    def __init__(self,numero,titular,saldo):
        self.numero=numero
        self.titular=titular
        self.saldo=saldo

    def getdatos(self):
        return (f"Numero de cuenta: {self.numero}.Titular de la cuenta:{self.titular}.Saldo de la cuenta:{self.saldo}")

    def ingresar(self,value):
        self.saldo=self.saldo+value


    def retirar(self,value):
        self.saldo=self.saldo-value




cuenta=CuentaCorriente(3,"Alejandro",200)
cuenta.ingresar(300)
cuenta.retirar(100)


class CuentaJoven(CuentaCorriente):
    def __init__(self, numero, titular, saldo,bono):
        super().__init__(numero, titular, saldo)
        self.bono=bono
        self.saldo=self.saldo+bono

    def getBonus(self):
        return self.bono

    def getdatos(self):
        return f"{super().getdatos()}.La cantidad del bono es:{self.bono}"

cuenta2=CuentaJoven(3,"Alejandro",300,0)
cuenta2.ingresar(100)
print(cuenta.getdatos())
print(cuenta2.getdatos())




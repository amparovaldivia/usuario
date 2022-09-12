class Usuario:
    def __init__(self,nombre,email,saldo) -> None:
        self.nombre=nombre
        self.email=email
        self.saldo=saldo

    def hacer_deposito(self,monto):
        self.saldo=self.saldo+monto
        

    def hacer_retiro(self, monto):
        self.saldo=self.saldo-monto

    def mostrar_balance_usuario(self): 
        print(self.saldo)

    def  transfer_dinero(self, other_user, monto): 
        self.hacer_retiro(monto)
        other_user.hacer_deposito(monto)
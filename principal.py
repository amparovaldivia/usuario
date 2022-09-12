from usuario import Usuario

usuario_uno=Usuario("Juan","juan@gmail.com",1000)
usuario_dos=Usuario("Luisa","luisa@gmail.com",20000)
usuario_tres=Usuario("Lila","lila@gmail.com",34000)

usuario_uno.hacer_deposito(50000)
usuario_uno.hacer_deposito(70000)
usuario_uno.hacer_deposito(100000)
usuario_uno.hacer_retiro(20000)
usuario_uno.mostrar_balance_usuario()

usuario_dos.hacer_deposito(150000)
usuario_dos.hacer_deposito(81533)
usuario_dos.hacer_retiro(22000)
usuario_dos.mostrar_balance_usuario()

usuario_tres.hacer_deposito(500500)
usuario_tres.hacer_retiro(35000)
usuario_tres.hacer_retiro(15000)
usuario_tres.hacer_retiro(120000)
usuario_tres.mostrar_balance_usuario()

usuario_tres.transfer_dinero(usuario_dos,15000)
usuario_tres.mostrar_balance_usuario()



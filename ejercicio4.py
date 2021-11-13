"""Se pide crear una clase que refleje una cuenta bancaria. Esta clase va a tener cómo atributos
el ID de la cuenta bancaria, el nombre de titular, una fecha de apertura, un número de cuenta
y un saldo. Por favor, aplique el tipo que mejor corresponda a cada atributo.

La cuenta bancaria deberá tener como mínimo un método para retirar dinero,
otro para ingresar dinero y otro para transferir dinero de una cuenta bancaria
a otra cuenta bancaria. De una cuenta bancaria no se podrá retirar nunca dinero
(ni transferir) si la cantidad de dinero a retirar o transferir es mayor que el saldo.

Crea una cuenta bancaria a Plazo Fijo, en la cual cuando se retira dinero de algún modo antes
de una Fecha de Vencimiento además del dinero a retirar se penaliza con un 5% adicional.

Crea además una cuenta Vip, que tendrá un atributo adicional que es el saldo negativo máximo
que puede tener. En las cuentas Vip uno podrá tener saldo negativo siempre que no supere este valor.

A continuación, construye una aplicación que permita crear los tres tipos de cuentas.
El ID tiene que ser un número entero incremental, el nombre del titular puede ser inventado,
la fecha de apertura y fecha de vencimiento deben ser aleatorias siendo la fecha de apertura
más antigua que la fecha de vencimiento, y el número de cuenta tiene que ser un número aleatorio
de 12 dígitos. Cuando las cuentas estén iniciadas a un sueldo inicial de 10.000 €, transferir dinero
de unas a otras las cantidades de 2000 €, ingresar 575 € y retirar dinero 78 €.
"""
from datetime import date
import random
class CuentaBancaria():
    def __init__(self,ID,titular,fechaApertura,nºcuenta,saldo):
        str : self.ID = ID
        str : self.titular = titular
        self.fechaApertura = fechaApertura.date(2020,11,6)
        int : self.nºcuenta = nºcuenta
        float: self.saldo = saldo
    def retirarDinero(self, dineroRetirado):
        if (self.saldo)<dineroRetirado:
            print("No dispone del dinero suficiente para retirar la cantidad que desea")
        else:
            self.saldo = self.saldo - dineroRetirado
            print("Ha retirado: "+str(dineroRetirado)+"€. Su saldo actual es de: "+str(self.saldo)+"€")
    def ingresarDinero(self, dineroIngresado):
        self.saldo = self.saldo + dineroIngresado
        print("Ha ingresado: "+str(dineroIngresado)+"€. Su saldo actual es de: "+str(self.saldo)+"€")
    def transferirDinero(self, dineroTransferido):
        if self.saldo<dineroTransferido:
            print("No dispone del dinero suficiente para transferir la cantidad que desea")
        else:
            self.saldo = self.saldo - dineroTransferido
            print("Ha transferido: "+str(dineroTransferido)+"€. Su saldo actual es de: "+str(self.saldo)+"€")
class CuentaPlazoFijo():
    def __init__(self,ID,titular,fechaApertura,nºcuenta,saldo):
        str : self.ID = ID
        str : self.titular = titular
        fechaApertura = fechaApertura.date(2020,11,6)
        int : self.nºcuenta = nºcuenta
        float: self.saldo = saldo

    def retirarDinero(self,dineroRetirado):
        hoy=input("Intorduce la fecha en la que quiere retirar el dinero: "+date())
        vencimiento=input("Introduce la fecha de vencimiento de tu cuenta: "+date())
        if hoy<vencimiento:
            self.saldo = self.saldo - dineroRetirado - (self.saldo*0.05)
            print("Ha retirado: "+str(dineroRetirado)+"€ antes de la fecha de vencimiento, " +
            "por lo que se le ha cargado un 5"+ "%" +"dicional. Su saldo actual es de: "+str(self.saldo)+"€")
        else:
            self.saldo = self.saldo - dineroRetirado
            print("Ha retirado: "+str(dineroRetirado)+"€ después de la fecha de vencimiento, " +
            "por lo que no se le ha cargado un 5"+ "%" +"dicional. Su saldo actual es de: "+str(self.saldo)+"€")
    def ingresarDinero(self, dineroIngresado):
        self.saldo = self.saldo + dineroIngresado
        print("Ha ingresado: "+str(dineroIngresado)+"€. Su saldo actual es de: "+str(self.saldo)+"€")
    def transferirDinero(self, dineroTransferido):
        if dineroTransferido>self.saldo:
            print("No dispone del dinero suficiente para transferir la cantidad que desea")
        else:
            self.saldo = self.saldo - dineroTransferido
            print("Ha transferido: "+str(dineroTransferido)+"€. Su saldo actual es de: "+str(self.saldo)+"€")

class CuentaVIP():
    def __init__(self,ID,titular,fechaApertura,nºcuenta,saldo,negativoMax):
        str : self.ID = ID
        str : self.titular = titular
        fechaApertura = fechaApertura.date(2020,11,6)
        int : self.nºcuenta = nºcuenta
        float: self.saldo = saldo
        float : self.negativoMax = negativoMax
    def retirarDinero(self, dineroRetirado):
        if dineroRetirado>self.negativoMax:
            print("No dispone del dinero suficiente para retirar la cantidad que desea")
        else:
            self.saldo = self.saldo - dineroRetirado
            print("Ha retirado: "+str(dineroRetirado)+"€. Su saldo actual es de: "+str(self.saldo)+"€")
    def ingresarDinero(self, dineroIngresado):
        self.saldo = self.saldo + dineroIngresado
        print("Ha ingresado: "+str(dineroIngresado)+"€. Su saldo actual es de: "+str(self.saldo)+"€")
    def transferirDinero(self, dineroTransferido):
        if dineroTransferido>self.negativoMax:
            print("No dispone del dinero suficiente para transferir la cantidad que desea")
        else:
            self.saldo = self.saldo - dineroTransferido
            print("Ha transferido: "+str(dineroTransferido)+"€. Su saldo actual es de: "+str(self.saldo)+"€")
class lasTresCuentas(CuentaBancaria,CuentaPlazoFijo,CuentaVIP):
    cuenta1 = CuentaBancaria("ES100200300","María",date(2021,3,19),random.randint(1,15),10000)
    cuenta2 = CuentaPlazoFijo("ES200300400","Sara",date(2021,1,12),random.randint(1,15),5000)
    cuenta3 = CuentaVIP("ES300400500","Paula",date(2021,3,6),random.randint(1,12),2000,3000)
    if cuenta1.saldo>=10000:
        cuenta1.transferirDinero(2000)
        cuenta1.retirarDinero(78)
        cuenta1.ingresarDinero(575)
        cuenta2.saldo=cuenta2.saldo+2000
        cuenta3.saldo=cuenta3.saldo+2000
    if cuenta2.saldo>=10000:
        cuenta2.transferirDinero(2000)
        cuenta2.retirarDinero(78)
        cuenta2.ingresarDinero(575)
        cuenta1.saldo=cuenta1.saldo+2000
        cuenta3.saldo=cuenta3.saldo+2000
    if cuenta3.saldo>=10000:
        cuenta3.transferirDinero(2000)
        cuenta3.retirarDinero(78)
        cuenta3.ingresarDinero(575)
        cuenta2.saldo=cuenta2.saldo+2000
        cuenta1.saldo=cuenta1.saldo+2000
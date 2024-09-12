__author_ = 'Mauricio Ordoñez'
_license_ = 'GPL'  #GPL codigo libre
_version_ = '1.0.0'
_email_ = 'anderson.ordonezz@campusucc.edu.co'

class CuentaCorriente:
    __saldo = 0
    __numero_cuenta = ''
    
_method_ = 'DarSaldo'
_parameter_ = 'ninguno'
_return_ = 'saldo'
_description_ = 'retorna el saldo actual de la cuenta del cliente'
def darSaldo(self):
    return self.__saldo

_method_ = 'ConsignarValor'
_parameter_ = 'monto'
_return_ = 'ninguno'
_description_ = 'Permite consignar un monto a la cuenta corriente'
def consignarValor(self, monto):
    self.__saldo = self.__saldo + monto
       
_method_ = 'RetirarValor'
_parameter_ = 'monto'
_return_ = 'valor retirado'
_description_ = 'se retira una cantidad de dinero si la cuenta cuenta con dinero suficiente'
def retirarValor(self, monto):
    self.__saldo = self.__saldo - monto
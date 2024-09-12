__author_ = 'Mauricio Ordoñez'
_license_ = 'GPL'  #GPL codigo libre
_version_ = '1.0.0'
_email_ = 'anderson.ordonezz@campusucc.edu.co'

class CuentaAhorros:
    __saldo = 0
    __numero_cuenta = ''
    __interes_mensual = 0

_method_ = 'ConsignarValor'
_parameter_ = 'nuevoValor'
_return_ = 'valor consignado'
_description_ = 'Depositar un valor a la cuenta.'
def consignarSaldo(self, monto):
    self.__saldo = self.__saldo + monto
    
_method_ = 'DarSaldo'
_parameter_ = 'ninguno'
_return_ = 'saldo'
_description_ = 'retorna el saldo actual de la cuenta del cliente'
def darSaldo(self):
    return self.saldo + self.interes_Mensual 


_method_ = 'RetirarValor'
_parameter_ = 'monto'
_return_ = 'valor retirado'
_description_ = 'se retira una cantidad de dinero si la cuenta cuenta con dinero suficiente'
def retirarValor(self, monto):

    self.saldo = monto

_method_ = 'DarInteresMensual'
_parameter_ = 'ninguno'
_return_ = 'interes mensual'
_description_ = 'retorna el interes mensual ganado'
def darInteresMensual(self):
    
    return self.interes_mensual
    
_method_ = 'actualizarSaldoPorPasoMes'
_parameter_ = 'ninguno'
_return_ = ''
_description_ = 'actualiza el saldo de la cuenta aumentando el interes mensual'    
def actualizarSaldoPorPasoMes(self):

    return 
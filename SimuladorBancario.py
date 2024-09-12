__author_ = 'Mauricio Ordoñez'
_license_ = 'GPL'  #GPL codigo libre
_version_ = '1.0.0'
_email_ = 'anderson.ordonezz@campusucc.edu.co'

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from Tiempo import Tiempo
from CDT import CDT

class Banco:
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ATRIBUTOS 
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    __nombre_cliente = ''
    __numero_de_cedula = ''
    __mes_actual = Tiempo()
    
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ASOCIACIONES
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    __cuenta_corriente = CuentaCorriente()
    __cuenta_ahorros = CuentaAhorros()
    __cdt = CDT()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # METODOS
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def darNombreCliente(self):
    return self.nombre_cliente

_method_ = 'DepositarCuentaCorriente'
_parameter_ = 'monto'
_return_ = 'ninguno'
_description_ = 'Muestra el saldo total de todas las cuentas'
def depositarCuentaCorriente(self, monto):
    self.__cuenta_corriente.consignarValor(monto)


_method_ = 'PasarAhorrosCuentaCorriente'
_parameter_ = 'ninguno'
_return_ = 'ninguno'
_description_ = 'Metodo que permite pasar el saldo de la cuenta de ahorros a la cuenta corriente'
def pasarAhorrosCuentaCorriente(self):
    saldoAhorros = self.__cuenta_ahorros.darSaldo()
    self.__cuenta_ahorros.retirarValor(saldoAhorros)
    self.__cuenta_corriente.consignarValor(saldoAhorros)
    
_method_ = 'retirarAhorro'
_parameter_ = 'monto'
_return_ = 'ninguno'
_description_ = 'Metodo que permite retirar un saldo de la cuenta ahorros'
def retirarAhorro(self,monto):
    self.__cuenta_ahorros.retirarValor(monto)
    
    
_method_ = 'darSaldoCorriente'
_parameter_ = 'ninguno'
_return_ = 'ninguno'
_description_ = 'Metodo que permite dar el saldo de la cuenta corriente'
def darSaldoCorriente(self):
    self.__cuenta_corriente.darSaldo()


_method_ = 'retirarTodo'
_parameter_ = 'ninguno'
_return_ = 'ninguno'
_description_ = 'Metodo retira el saldo existente de la cuenta ahorros y de la cuenta corriente'
def retirarTodo(self):
    self.__cuenta_ahorros.retirarValor(self.__cuenta_ahorros.darSaldo())
    self.__cuenta_corriente.retirarValor(self.__cuenta_corriente.darSaldo())
    
    
_method_ = 'duplicarAhorro'
_parameter_ = 'ninguno'
_return_ = 'ninguno'
_description_ = 'Metodo que duplica el valor existente de la cuenta'
def duplicarAhorro(self):
    self.__cuenta.consignarSaldo(self.__cuenta.darSaldo())
        
        
_method_ = 'CalcularSaldoTotal'
_parameter_ = 'None'
_return_ = 'saldo total de totas las cuentas'
_description_ = 'Muestra el saldo total actual en todas las cuentas'
def calcularSaldoTotal(self):
    return self.__cuenta_corriente.darSaldo() + self.__cuenta_corriente.darSaldo() + self.__cdt.darSaldo()
__author_ = 'Mauricio Ordoñez'
_license_ = 'GPL'  #GPL codigo libre
_version_ = '1.0.0'
_email_ = 'anderson.ordonezz@campusucc.edu.co'


class CDT:
    saldo_invertido = 0
    valor_interes = 0
    
    
_method_ = 'SaldoAInvertir'
_parameter_ = 'nuevoSaldo'
_return_ = 'None'
_description_ = 'Establece un nuevo saldo a invertir en el CDT'
def SaldoAInvertir(self, valorParaInvertir):
    self.saldo_invertido = valorParaInvertir


_method_ = 'ActualizarSaldoPorMes'
_parameter_ = 'None'
_return_ = 'None'
_description_ = 'Actualiza el saldo del CDT aplicando el interés mensual correspondiente'
def  ActualizarSaldoPorMes(self):
   return  

_method_ = 'mostrar saldo total'
_parameter_ = 'None'
_return_ = 'suma de valor invertido mas intereses'
_description_ = 'Muestra el saldo despues de un mes, sumandole al valor invertido el interes mensual'
def darSaldo(self):
    self.saldo_invertido + self.valor_interes

    
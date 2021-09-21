# -*- coding: utf-8 -*-
#Importação de modulos
import abc
from unittest import TestCase,main
from logging import raiseExceptions


#Criação de classes
class Calculadora(object):
    def calcular(self,arg1,arg2,operador):
        operacao = OperacaoFabrica().criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(arg1,arg2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operador):
        if (operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self,arg1,arg2):
        pass

#Classes de Operação
class Soma(Operacao):
    def executar(self, arg1, arg2):
        resultado = arg1 + arg2
        return resultado
class Subtracao(Operacao):
    def executar(self, arg1, arg2):
        resultado = arg1 - arg2
        return resultado
class Divisao(Operacao):
    def executar(self, arg1, arg2):
        resultado = arg1 / arg2
        return resultado


#Testes
class Testes(TestCase):
    def test_soma(self):
        calculo_soma = Calculadora()
        result = calculo_soma.calcular(2,3,'soma')
        self.assertEqual(result,5)

    def test_divisao(self):
        calculo_divisao = Calculadora()
        result = calculo_divisao.calcular(2,4,'divisao')
        self.assertEqual(result,0.5)

    def test_subtracao(self):
        calculo_subtracao = Calculadora()
        result = calculo_subtracao.calcular(10,50,'subtracao')
        self.assertEqual(result, -40)


executar = """CALCULADORA
Operações:\n
    Soma            +
    Subtracao       -
    Divisao         /"""


def codigo():
    operacoes=['soma','subtracao','divisao']
    operacao=input("Digite o nome da operação:").lower()
    if operacao not in operacoes:
        print("Operação não reconhecida")
        codigo()
    arg1=float(input("Digite o primeiro valor:"))
    arg2=float(input("Digite o segundo valor:"))
    resultado = Calculadora().calcular(arg1,arg2,operacao)
    print ("Resultado = {0:g}".format(float(resultado)))


print(executar)
codigo()
main()

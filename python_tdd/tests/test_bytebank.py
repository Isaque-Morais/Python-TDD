from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        #Given
        entrada = '13/03/1999' 
        esperado = 24

        #When
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  

        #Then
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        #Given
        entrada = ' Lucas Carvalho ' 
        esperado = 'Carvalho'

        #When
        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() 

        #Then
        assert resultado == esperado 

    def test_quando_descrescimo_salario_recebe_100000_deve_retornar_90000(self):
        #Given
        entrada_name = 'Isaque Santos'
        entrada_data = '12/01/2000'
        entrada_salario = 100000
        esperado = 90000

        #When
        funcionario_teste = Funcionario(entrada_name, entrada_data, entrada_salario)
        funcionario_teste.descrescimo_salario()
        resultado = funcionario_teste.salario

        #Then
        assert resultado == esperado 

    # @mark.calcular_bonus
    def test_quando_calcular_bonus_receber_10000_deve_retorna_100(self):

        #Given
        entrada = 1000
        esperado = 100

        #When
        funcionario_teste = Funcionario('Fulano', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        #Then
        assert resultado == esperado

    # @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_expection(self):
        #Given
        with pytest.raises(Exception):
            entrada = 1000000

            #When
            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            #Then
            assert resultado
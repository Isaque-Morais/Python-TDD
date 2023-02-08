from codigo.bytebank import Funcionario

class TestClass:
        def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
            entrada = ' Lucas Carvalho ' # Given
            esperado = 'Carvalho'

            lucas = Funcionario(entrada, '11/11/2000', 1111)
            resultado = lucas.sobrenome() # When

            assert resultado == esperado

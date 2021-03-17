class calculadora():
    def __init__(self):
        self.funcoes = {
            "soma" : self.soma,
            "-" : self.subtracao,
            "x" : self.multiplicacao,
            "/" : self.divisao,
            "raiz_quadrada" : self.raiz_quadrada,
            "%" : self.porcentagem
        }
        
    def soma(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y
    
    def multiplicacao(self, x, y):
        return x * y
    
    def divisao(self, x, y):
        return x / y
    
    def raiz_quadrada(self, x):
        return x ** (1/2)
    
    def porcentagem(self, x, y):
        return (x * y) / 100
    
if __name__ == "__main__" :
    
    Calculadora = calculadora()
    resultado  = Calculadora.funcoes['-'](1, 2)
    print (f"resultado = {resultado}")
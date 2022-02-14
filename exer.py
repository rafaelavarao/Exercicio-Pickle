import pickle

class FormulaCocaCola:
    def __init__(self, ingredientes, temperatura, açucar, nomeDoProprietario):
        self.__ingredientes = ingredientes
        self.__temperatura = temperatura
        self.__açucar = açucar
        self.__nomeDoProprietario = nomeDoProprietario

    @property
    def ingredientes(self):
        return self.__ingredientes

    @property 
    def temperatura(self):
        return self.__temperatura

    @property
    def açucar(self):
        return self.__açucar

    @property 
    def nomeDoProprietario(self):
        return self.__nomeDoProprietario

formula = FormulaCocaCola('agua gaiseficada', '3°C', '9g', 'Asa Griggs Candler')

with open('formulaSecreta.pickle', 'wb') as arq:
    pickle.dump(formula, arq)

senha_Digitada = input('Digite a senha para acessar os atributos. ')
senha = '123'

if senha_Digitada == senha:
    with open('formulaSecreta.pickle', 'rb') as arq:
        formula = pickle.load(arq)
        print(f'A formula secreta é {formula.ingredientes}, temperatura: {formula.temperatura}, Açucar: {formula.açucar} e o nome do proprietario é: {formula.nomeDoProprietario}')
else:
    print('Acesso negado.')


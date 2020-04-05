#Simulador de dado
#Python version: 3.7.3
#Simular o uso de um dado gerando um valor de 1 ate 6
#Ainda tem que ver como colocar acento nas palavras

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    #Define o comportamento inicial
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6 
        #Layout
        self.layout =[
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('nao')]
        ]

    def Iniciar(self):
        #Criar uma janela
        self.janela = sg.Window('Simulador de dado', layout=self.layout)        
        #Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        #Fazer alguma coisa com esses valores
        
        try:
            if self.eventos=="sim":
                self.GerarValorDoDado()
            elif self.eventos=="nao":
                print("\nAgradecemos sua participacao.")
            else:
                print("\nPor favor, digite somente algumas das opcoes abaixo:\n ")
                print("'sim', 'nao', 's' ou 'n'")
        except:
            print("Ocorreu um erro ao receber sua resposta")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

#Instanciando a classe SimuladorDeDado para usa-la
simulador = SimuladorDeDado()
simulador.Iniciar()
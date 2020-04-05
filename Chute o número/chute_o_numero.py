#Projeto3 - Chute o número
#Criar um algoritmo que gera um número aleatório e o programa tem
##que ficar me perguntando qual o valor até que eu acerte
import random
import PySimpleGUI as sg
class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo =1
        self.valor_maximo=100
        self.tentar_novamente =True

    def Iniciar(self):
        #layout
        self.layout = [
            [sg.Text("Seu chute",size=(20,0))],
            [sg.Input(size=(14,20),key="ValorChute")],
            [sg.Button("Chutar!")],
            [sg.Output(size=(30,10))]
        ]
        #Criar uma janela
        self.janela = sg.Window("CHUTE UM NÚMERO", layout=self.layout)
        self.GerarNumeroAleatorio()
        
        try:
            while True:
                #Receber valores
                self.evento, self.valores = self.janela.Read()
            
                if self.evento == "Chutar!":
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print("\nChute um valor menor")
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print("\nChute um valor mais alto")
                            break
                        if int(self.valor_do_chute)==self.valor_aleatorio:
                            self.tentar_novamente = False
                            print("\nParabéns, você acertou!!!")
                            break
        except:
            print("\nDigite apenas números.")
        

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute1 = ChuteONumero()
chute1.Iniciar()
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
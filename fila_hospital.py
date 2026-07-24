class Paciente:
    def __init__(self,nome, idade, sexo, prioridade):
        self.nome=nome
        self.idade=idade
        self.sexo=sexo
        self.prioridade=prioridade

    def __str__(self):
        return f"{self.nome} | {self.idade} anos | {self.sexo} | Prioridade: {self.prioridade}"
    
class Fila:
    def __init__(self):
        self.fila = []

    def cadastrar(self):
        
        nome= input('Nome? ')
        

        while True:
            idade = input('Idade: ')
            if idade.isnumeric():
                idade = int(idade)
                break
            else:
                print('Digite sua idade com numeros')

        sexo = input('Sexo: ').upper()

        while True:

            prioridade = input('Prioridade(VERDE,VERMELHO,AMARELO,PRETO): ').upper()
            if prioridade not in ('VERDE','VERMELHO','AMARELO','PRETO'):
                print('Digite uma cor válida')
            else:
                break



        paciente=Paciente(nome,idade,sexo,prioridade)
        self.inserir_paciente(paciente)

    def inserir_paciente(self,paciente):

        #--------FILA VAZIA-----------------------

        if len(self.fila) == 0:

            self.fila.append(paciente)
            print(f'O paciente {paciente} foi para a fila')
            return

        #-----------PRETO----------------------------------

        if paciente.prioridade == 'PRETO':
            self.fila.append(paciente)
            print(f'O paciente {paciente} foi para a fila')

        #------------VERDE--------------------------------

        elif paciente.prioridade == 'VERDE':
            pos = 0
            for i in self.fila:
                if i.prioridade in ('VERDE','AMARELO','VERMELHO'):
                    pos+=1

            self.fila.insert(pos,paciente)
            print(f'O paciente {paciente} foi para a fila')

        #----------AMARELO-------------------------------------

        elif paciente.prioridade =='AMARELO':

            pos = len (self.fila)
            verdes = 0
            

            for i in range((pos-1),-1,-1):

                if self.fila[i].prioridade == 'VERDE':
                    verdes+=1

                    if verdes == 2:
                        pos = i
                        break

                elif self.fila[i].prioridade in ('VERMELHO','AMARELO'):
                    pos = i + 1



            self.fila.insert(pos,paciente)
            print(f'O paciente {paciente} foi para a fila')     

        #------------VERMELHO------------------------------------
        
        elif paciente.prioridade =='VERMELHO':

            pos=0

            for i in self.fila:
                if i.prioridade == 'VERMELHO':
                    pos += 1

            self.fila.insert(pos,paciente)
            print(f'O paciente {paciente} foi para a fila')

    def proximo(self):

        if len(self.fila) == 0:
            print('\nFila vazia\n')

        else:
            print(f'\n{self.fila[0].nome} venha até o guiche\n')
            self.fila.pop(0)

    def mostrar(self):

        if len(self.fila) == 0:
            print('\nFila vazia\n')
        #usar enumerate
        else:
            for i in self.fila:
                print(i)

    def proximo_da_fila(self):

        if len(self.fila) == 0:
            print('\nfila está vazia\n')

        else:
            print(f'\nO(a) proximo da fila é {self.fila[0]}\n')

def menu():
    print('\nDigite 1 para entrar na fila')
    print('Digite 2 para chamar o proximo elemento')
    print('Digite 3 para ver a fila')
    print('Digite 4 para ver proximo da fila')
    print('Digite 5 para fechar a fila')
    opcao=input('\nQual opção desejada? \n')
    return opcao

cliente = Fila()

while True:

    opcao=menu()
    

    if opcao == '1':
       
        cliente.cadastrar()

    elif opcao == '2':

        cliente.proximo()

    elif opcao == '3':

        cliente.mostrar()

    elif opcao == '4':

        cliente.proximo_da_fila()

    elif opcao == '5':

        break

    else:
        print('\nDigite uma opção valida\n')


    
    

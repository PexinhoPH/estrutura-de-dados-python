fila=[]
def menu():
    print('\nDigite 1 para entrar na fila')
    print('Digite 2 para chamar o proximo elemento')
    print('Digite 3 para ver a fila')
    print('Digite 4 para ver proximo da fila')
    print('Digite 5 para fechar a fila')
    opcao=input('\nQual opção desejada? \n')
    return opcao

opcao= menu()

while True:
    opcao = menu()
    if opcao == '1':

        elemento = input('\nQuem está entrando na fila? \n')
        fila.append(elemento)
        
    
    elif opcao == '2':

        if len(fila) == 0:
            print('\nFila vazia\n')

        else:
            print(f'\nDirija-se ao caixa {fila[0]}\n')
            fila.pop(0)
            

    elif opcao == '3':

        for i in fila:
            print(i)
        
        

    elif opcao == '4':

        if len(fila) == 0:
            print('\nFila está vazia\n')
            
        else:
            print(f'\nO próximo da fila é o(a) {fila[0]}\n')
            

    elif opcao == '5':

        print('\nA fila foi encerrada\n')
        break

    else:
        print('\nDigite uma opção valida\n')
        


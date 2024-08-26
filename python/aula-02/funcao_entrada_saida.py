nome = input("Informe seu nome:")
idade = input("Informe sua idade:")

if nome is not None:
    #Alterando o end para mudar o final do print
    print(f"O nome inserido foi: {nome}", f"e a idade inserida foi: {idade}", end="...\n")
    # foi adicionado os 3 pontos mas o padrão é apenas a quebra de linha \n

    print("Espaço vazio no lugar da quebra", end=" " )
    print("Teste") 
    #Neste exemplo foi substituido pelo espaço vazio fazendo com que os prints fiquem na mesma linha
    print("======================")
    #Alterando o sep para mudar o valor que separa
    print(nome,idade, sep="#")

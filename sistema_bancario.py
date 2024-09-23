from datetime import datetime

conta = 0
extrato = ""
limitesaq = 0
limiteacoes = 0
atual = datetime.today()
ultima = datetime.today();
#função para depositar
def depositar(cont,val):
    global limiteacoes
    global ultima
    valido = False
    #se o valor do deposito for negativo ou o limite de ações for 10 não vai depositar
    if val<0 or limiteacoes>=10:
        print("Depósito invalido")
    else:
        valido = True
    # se o limite de transações for alcançado
    if limiteacoes >= 10:
        print("Limite de transações diario alcançado")
    # se o deposito for valido vai adicionar na conta e adicionar ao extrato a operação
    if (valido == True):
        global extrato
        limiteacoes += 1
        ultima = datetime.today();
        extrato += f"Depósito com valor de R$ {val} data: {datetime.now().strftime("%d/%m/%Y")} Horario: {datetime.now().strftime("%H:%M:%S")}\n "
        return cont + val
    else:
        return cont
#função para sacar
def sacar(cont,val):
    valido = False
    global limitesaq
    global limiteacoes
    global ultima
    #se o valor de saque for menor que o valor na conta
    #e o valor for maior que zero e menor ou igual a 500 e o usuario ainda não tenha feito 3 saques e não tenha alcançado o limite de transações
    #será valido o saque
    if (cont>val and val>0 and val<= 500 and limitesaq < 3 and limiteacoes<10):
        valido = True
        limitesaq += 1
    #se o valor da conta for menor que o valor de saque
    if cont<val:
        print("Valor de saque maior que valor na conta")
    #se o valor do saque for menor que 0
    if (val<0):
        print("Valor de saque invalido")
    #se o limite de saque for alcançado
    if limitesaq >= 3:
        print("Limite de saque alcançado")
    #se o limite de transações for alcançado
    if limiteacoes >= 10:
        print("Limite de transações diario alcançado")
    #se o saque for valido adiciona no extrato a operação e subtrai da conta o valor
    if valido == True:
        global extrato
        limiteacoes+= 1
        ultima = datetime.today();
        extrato += f"Saque com valor de R$ {val} data: {datetime.now().strftime("%d/%m/%Y")} Horario: {datetime.now().strftime("%H:%M:%S")}\n"
        return conta - val
    else:
        return cont

########parte principal do programa#########
while True:

    print('''
    ######-Menu-######
    |   (1)-Depósito |
    |   (2)-Saque    |
    |   (3)-Extrato  |
    |   (4)-Sair     |  
    ######-Menu-######
    ''')
    op = int(input())
    #se o dia,mês e ano forem diferentes da ultima ação vai resetar o limite de ações
    if ultima.strftime("%d/%m/%Y") != atual.strftime("%d/%m/%Y"):
        limiteacoes = 0
        print(f"Limite de transações resetado {ultima} + {atual}")
    #se opção 4 for escolhida o programa acaba
    if op == 4:
        break
    #se opção 1 for escolhida o programa irá depositar
    if op == 1:
        dep = float(input("De quanto será o depósito?"))
        conta = depositar(conta,dep)
    #se opção 2 for escolhida o programa irá sacar
    if op == 2:
        saq = float(input("De quanto será o saque?"))
        conta = sacar(conta,saq)
    #se opção 3 for escolhida o programa irá imprimir o extrato
    if op == 3:
        print(f'''
        ########################################-Extrato-########################################
        \n
        {extrato}
        Saldo atual da conta R$ {conta}          
        ########################################-Extrato-########################################
        ''')
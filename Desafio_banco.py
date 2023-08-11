menu="""

[d]Depositar
[s]Sacar
[e]extrato
[q]sair

=>"""

saldo=0
limite=500
extrato=""
numero_saque=0
LIMITE_SAQUE=3

while True:
    opcao=input(menu)
    if opcao=="d":
        valor=float(input("informe o valor do depositto:"))
        if valor>0:
            saldo+=valor
            extrato+=f"deposito: R${valor:.2f}\n"
        else:
            print("Operaçao falhou! Valor informado invalido.")    
    elif opcao=="s":
      valor=float(input("informe o valor do saque: "))
      excedeu_saldo=valor>saldo
      exedeu_limite=valor>limite
      exedeu_saque=numero_saque>=LIMITE_SAQUE
      if excedeu_saldo:
          print("operaçao falhou! sem saldo suficiente.") 
      elif exedeu_limite:
          print("operaçao falhou! valor do saque exede o limite.")
      elif exedeu_saque:
          print("operaçao falho! numero  maxio de saques exedido.")
      elif valor>0:   
        saldo-=valor
        extrato+=f"saque:R$ {valor:.2f}\n"
        numero_saque+=1
      else:
          print("operaçao falhou!valor informado e invalido")  
    elif opcao=="e":
        print("\n========= EXTRATO =========")
        print("sem movimentaçoes."if not extrato else extrato)
        print(f"\nsaldo: R${saldo:.2f}")      
        print("===========================")
    elif opcao=="q":
        break
    else:
        print("Operaçao invalida, Selecione novamente  a opçao desejada.")    
        
          


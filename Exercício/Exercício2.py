#Durante a manutenção de um sistema você observou que o cálculo para
#desconto do E-COMMERCE estava dando errado. Mediante a entrada do
#valor de um produto, realize o calculo de 15% sobre o valor do produto.
#Critérios de Aceite:
#O usuário deve digitar o valor do produto
#Deve ser exibido o Valor total do produto e seu desconto
try:
    produto = float(input("Digite o valor:"))
    Desconto = produto - (produto * 0.15)
    print(f"valor do produto com 15% de desconto: {Desconto}")
    print(f"Resultado do valor {produto}")
    
except ValueError:
    print("Digite um número")
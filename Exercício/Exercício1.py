#Você foi contratada(o) para desenvolver um sistema de Escola com o objetivo
#de calcular as médias dos alunos.
#Critérios de Aceite:
# O usuário deve digitar 3 notas
# Deve ser exibida a média das 3 notas
try:
    nota1 = int(input("Digite a primeira nota:"))
    nota2 = int(input("Digite a segunda nota:"))
    nota3 = int(input("Digite a terceira nota:"))
    Media = (nota1 + nota2 + nota3) / 3
    if Media >= 7:
        print("Paranbéns, você passou!")
    elif Media < 7: 
        print("Você não passou")
except ValueError:
    print("Isso é uma letra")

    
        
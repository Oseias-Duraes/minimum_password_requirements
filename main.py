import re

senha = input("Insira a senha a ser verificada: ")

if len (senha) < 8: #Verificando o tamanho mínimo da senha
    u = False

pattern1 = re.compile("[A-Z].*" * 2) #verificando se tem letras maísculas
v = re.search(pattern1, senha)

pattern2 = re.compile("[a-z].*" * 4) # Verificando se têm letras minúsculas
w = re.search(pattern2, senha)

pattern3 = re.compile("[0-9].*" * 4) # Verificando se tem dígitos inteiros
x = re.search(pattern3, senha)

pattern4 = re.compile("[@!#$%^&*()/].*" * 2) #Verificando se existem caracteres especiais.
y = re.search(pattern4, senha)

if u == False or v == None or w == None or x == None or y == None:
    print ("Senha inválida")

else:
    print("Senha validada com sucesso!")




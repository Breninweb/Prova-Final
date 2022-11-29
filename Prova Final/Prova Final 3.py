listaNomes = []
listaAnos = []
listaTelefones = []
listaEmails = []

for usuarios in range(3):
    nomes = str(input("Qual o seu nome? "))
    listaNomes.append(nomes)
    anos = int(input("Quantos anos você tem? "))
    listaAnos.append(anos)
    telefones = int(input("Qual o seu número de telefone? "))
    listaTelefones.append(telefones)
    emails = str(input("Qual o seu endereço de email? "))
    listaEmails.append(emails)

print("------ Lista de usuários ------")
print("USUÁRIO 1")
print(f"Nome: {listaNomes[0]}")
print(f"Idade: {listaAnos[0]}")
print(f"Telefone: {listaTelefones[0]}")
print(f"E-mail: {listaEmails[0]}")
print("-------------------------------")
print("USUÁRIO 2")
print(f"Nome: {listaNomes[1]}")
print(f"Idade: {listaAnos[1]}")
print(f"Telefone: {listaTelefones[1]}")
print(f"E-mail: {listaEmails[1]}")
print("-------------------------------")
print("USUÁRIO 3")
print(f"Nome: {listaNomes[2]}")
print(f"Idade: {listaAnos[2]}")
print(f"Telefone: {listaTelefones[2]}")
print(f"E-mail: {listaEmails[2]}")
print("-------------------------------")



nome = input("Digite seu nome: ");
while (len(nome) < 6 or len(nome) > 30):
    nome = input("Digite seu nome novamente: ");

idade = input("Digite sua Idade: ");
while (idade < 0 or idade > 150):
    idade = input("Digite sua idade novamente: ");

peso = input("Digite seu peso: ");
while (peso < 0):
    peso = input("Digite seu peso novamente: ");

altura = input("Digite sua Altura: ");
while (altura < 0):
    altura = input("Digite sua altura novamente:");

sexo = input("Digite seu Sexo: [F] ou [M]: ");
while ((sexo != 'M' and sexo != 'F' ) or (sexo != 'm' and sexo != 'f')):
    sexo = input("Digite seu sexo novamente")

print("\n\nDados Pessoais: ");
print ('\nNome: '+ nome);
print ('\nIdade: %d' % (idade));
print ('\nPeso: %2f' % (peso));
print ('\nAltura: %.2f' % (altura));
print ('\nSexo' + sexo);

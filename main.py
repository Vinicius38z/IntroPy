def print_hi(name):
    
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def contagem_progressiva(fim):
    for numero in range(fim): # Repetir o bloco de 0 até fim
        print(numero)         # exibir o número

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        #contador = numero + 1
        #print(f'{contador}- {nome}')
        if numero < 9:

            print(f'00{numero + 1} - {nome}')

        elif numero < 99:
            print(f'0{numero + 1} - {nome}')

        else:
            print(numero + 1,'-',nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>9}'.format(numero))



if __name__ == '__main__':
    print_hi('Vinicius')


# Chamar a função calcular area do retangulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A area do retangulo é de: {resultado} m²')

# Chamar a função calcular area do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A area do quadrado é de: {resultado} m²')
    
# Chamar a função calcular a area do triangulo
    resultado = calcular_area_do_triangulo(7,2)
    print(f'A area do triangulo é de: {resultado} m²')
    
# Executar uma contagem progressiva
    contagem_progressiva(11)
    
# Exibir o nome do candidato várias vezes
    apoiar_candidato('Faker', 100)
# Brincar de Plim
    brincar_de_plim(100)

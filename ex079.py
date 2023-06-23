valores = []
r = 'S'
print('=' * 80)
while r == 'S':
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Você já adicionou esse valor')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso')
    print('=' * 80)
    r = str(input('Quer colocar mais valores? [S/N]')).upper().strip()
    if r == 'S':
        print('Ok. ', end = '')
    if r == 'N':
        ordem = sorted(valores)
        print('Os valores adicionados digitados em ordem crescente é: ', end = '')
        print(ordem)
print('=' * 80)

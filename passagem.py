# RA 252062

import sys

# classe que guarda o dia, o mês e o ano de determinado voo
class Data:
    
    def __init__ (self, dia, mes, ano, voo='') :
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.voo = voo
    
    @property
    def dia(self) :
        return self._dia
    
    @property
    def mes(self) :
        return self._mes
    
    @property
    def ano(self) :
        return self._ano
    
    @property
    def voo(self) :
        return self._voo
    
    @dia.setter
    def dia(self, data) :
        self._dia = data
    
    @mes.setter
    def mes(self, data) :
        self._mes = data
    
    @ano.setter
    def ano(self, data) :
        self._ano = data

    @voo.setter
    def voo(self, valor) :
        self._voo = valor

# classe que guarda as informações dadas de determinado voo
class Voo:

    def __init__ (self, numero, origem='', destino='', data='', valor='', indice='') :
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.data = data
        self.valor = valor
        self.indice = indice
    
    @property
    def origem(self) :
        return self._origem
    
    @property
    def destino(self) :
        return self._destino
    
    @property
    def data(self) :
        return self._data
    
    @property
    def valor(self) :
        return self._valor
    
    @property
    def indice(self) :
        return self._indice
    
    @origem.setter
    def origem(self, codigo) :
        self._origem = codigo
    
    @destino.setter
    def destino(self, codigo) :
        self._destino = codigo
    
    @data.setter
    def data(self, entrada) :
        self._data = entrada
    
    @valor.setter
    def valor(self, preco) :
        self._valor = preco
    
    @indice.setter
    def indice(self, i) :
        self._indice = i

# classe que guarda os dados de Jairzinho
class Dados :

    def __init__ (self, saida, inicio='', fim='') :
        self.saida = saida
        self.inicio = inicio
        self.fim = fim

    @property
    def saida(self) :
        return self._saida
    
    @property
    def inicio(self) :
        return self._inicio
    
    @property
    def fim(self) :
        return self._fim
    
    @saida.setter
    def saida(self, dado) :
        self._saida = dado
    
    @inicio.setter
    def inicio(self, data) :
        self._inicio = data
    
    @fim.setter
    def fim(self, data) :
        self._fim = data

# função que retorna a quantidade de dias em determinado mês
# como os anos na entrada são sempre 2021 ou 2022, não são bissextos
def dias_mes(mes) :
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :
        return 31
    if mes == 2 :
        return 28
    if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
        return 30

# função que conta a duração em dias de uma data a outra
def conta_dias(inicio, fim) :
    duracao = 0
    if inicio.ano == fim.ano :
        for i in range(inicio.mes+1, fim.mes) :
            duracao += dias_mes(i)
        duracao += dias_mes(inicio.mes) - inicio.dia + 1
        duracao += fim.dia
    else :
        for i in range(inicio.mes+1, 13) :
            duracao += dias_mes(i)
        for i in range(1, fim.mes) :
            duracao += dias_mes(i)
        duracao += dias_mes(inicio.mes) - inicio.dia + 1
        duracao += fim.dia
    return duracao

voos = []
i = 0

# entrada com cada uma das operações
# lê o arquivo até End Of File
for line in sys.stdin:
    op = line.strip()
    if op == 'registrar' :
        voos.append(Voo(int(input())))
        voos[i].origem, voos[i].destino = map(str, input().split())
        voos[i].data = input()
        voos[i].valor = float(input())
        i += 1
    
    elif op == 'alterar' :
        num, novo_valor = map(str, input().split())
        num = int(num)
        novo_valor = float(novo_valor)
        for j in voos :
            if j.numero == num :
                print (f'{num} valor alterado de {j.valor} para {novo_valor}')
                j.valor = novo_valor
    
    elif op == 'cancelar' :
        num = int(input())
        for j in voos :
            if j.numero == num :
                voos.remove(j)
    
    elif op == 'planejar' :
        plano = Dados(input())
        plano.inicio, plano.fim = map(str, input().split())

# definição das datas das férias e dos vôos
comeca = Data(int(plano.inicio[:2]), int(plano.inicio[3:5]), int(plano.inicio[6:]))
acaba = Data(int(plano.fim[:2]), int(plano.fim[3:5]), int(plano.fim[6:]))
datas = []
for i in range(len(voos)) :
    datas.append(Data(int(voos[i].data[:2]), int(voos[i].data[3:5]), int(voos[i].data[6:]), voos[i].numero))

# criação de listas que contêm as possibilidades de idas e de voltas
possiveis_idas = []
possiveis_voltas = []

# se a data do vôo está dentro do período de férias de Jairzinho e se a origem do vôo é o mesmo aeroporto de onde Jairzinho sai,
# adicionamos esse vôo na lista de possíveis idas
for i in range(len(voos)) :
    if datas[i].ano == comeca.ano and voos[i].origem == plano.saida :
        if (datas[i].mes == comeca.mes and datas[i].dia >= comeca.dia) or (datas[i].mes > comeca.mes) :
            if ((datas[i].ano == acaba.ano and (datas[i].mes < acaba.mes or (datas[i].mes == acaba.mes and datas[i].dia < acaba.dia)))
                or datas[i].ano < acaba.ano) :
                voos[i].indice = i
                possiveis_idas.append(voos[i])
    elif datas[i].ano < comeca.ano and voos[i].origem == plano.saida :
        voos[i].indice = i
        possiveis_idas.append(voos[i])

# se a data do vôo está dentro do período de férias de Jairzinho e se o destino do vôo é o mesmo aeroporto de onde Jairzinho sai,
# adicionamos esse vôo na lista de possíveis voltas
for i in range(len(voos)) :
    if datas[i].ano == acaba.ano and voos[i].destino == plano.saida :
        if (datas[i].mes == acaba.mes and datas[i].dia <= acaba.dia) or (datas[i].mes < acaba.mes) :
            if ((datas[i].ano == comeca.ano and (datas[i].mes > comeca.mes or (datas[i].mes == comeca.mes and datas[i].dia > comeca.dia)))
                  or datas[i].ano > comeca.ano) :
                voos[i].indice = i
                possiveis_voltas.append(voos[i])
    elif datas[i].ano < acaba.ano and voos[i].destino == plano.saida :
        voos[i].indice = i
        possiveis_voltas.append(voos[i])

# criação de uma lista que contém o par ida-volta de Jairzinho
par = []

# selecionamos a viagem mais barata que tem no mínimo 4 dias
# se há empate no valor, selecionamos a viagem de maior duração
for i in possiveis_idas :
    for j in possiveis_voltas :
        if i.destino == j.origem and conta_dias(datas[i.indice], datas[j.indice]) >= 4 :
            if len(par) == 0 :
                par.append(i)
                par.append(j)
            elif ((i.valor + j.valor < par[0].valor + par[1].valor)
                  or (i.valor + j.valor == par[0].valor + par[1].valor
                      and conta_dias(datas[i.indice], datas[j.indice]) > conta_dias(datas[par[0].indice], datas[par[1].indice]))) :
                par[0] = i
                par[1] = j

# o programa imprime os vôos de ida e de volta que atendem as necessidades de Jairzinho
print (par[0].numero)
print (par[1].numero)

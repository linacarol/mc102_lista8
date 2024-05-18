# RA 252062

class Data:
    """
    classe que guarda o dia, o mes e o ano de determinado voo

    ela eh iniciada com os seguintes valores nesta ordem: dia, mes, ano
    """
    
    def __init__ (self, dia, mes, ano) :
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    @property
    def dia(self) :
        return self._dia
    
    @property
    def mes(self) :
        return self._mes
    
    @property
    def ano(self) :
        return self._ano
    
    @dia.setter
    def dia(self, data) :
        self._dia = data
    
    @mes.setter
    def mes(self, data) :
        self._mes = data
    
    @ano.setter
    def ano(self, data) :
        self._ano = data

class Voo:
    """"
    classe que guarda as informacoes de determinado voo

    ela eh iniciada com os seguintes valores nesta ordem: origem, destino, data, valor
    """

    def __init__ (self, origem, destino, data, valor) :
        self.origem = origem
        self.destino = destino
        self.data = data
        self.valor = valor
    
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

class Dados :
    """"
    classe que guarda os dados de Jairzinho

    ela eh iniciada com os seguintes valores nesta ordem: saida, inicio das ferias, fim das ferias
    """

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

def dias_mes(mes) :
    """"
    funcao que retorna a quantidade de dias existentes em determinado mes
    """

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :
        return 31
    if mes == 2 :
        return 28       # como os anos da entrada sao sempre 2021 ou 2022, nunca eh bissexto
    if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
        return 30

def conta_dias(inicio, fim) :
    """
    funcao que recebe duas datas e retorna a quantidade de dias existentes entre elas
    """
    
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

voos = dict()
op = input()

# loop que recebe a entrada do usuário até que ele digite 'planejar'
while op != 'planejar' :
    if op == 'registrar' :
        num = int(input())
        origem, destino = map(str, input().split())
        data = input()
        valor = float(input())
        voos[num] = Voo(origem, destino, data, valor)       # os voos sao armazenados em dicionarios cujas chaves sao os numeros
    
    elif op == 'alterar' :
        num, novo_valor = map(str, input().split())
        num = int(num)
        novo_valor = float(novo_valor)
        print (f'{num} valor alterado de {voos[num].valor} para {novo_valor}')
        voos[num].valor = novo_valor
    
    elif op == 'cancelar' :
        num = int(input())
        del voos[num]
    
    op = input()

# ao escolher 'planejar', Jairzinho insere seus dados
plano = Dados(input())
plano.inicio, plano.fim = map(str, input().split())

# definicao das datas das ferias e dos voos
comeca = Data(int(plano.inicio[:2]), int(plano.inicio[3:5]), int(plano.inicio[6:]))
acaba = Data(int(plano.fim[:2]), int(plano.fim[3:5]), int(plano.fim[6:]))
datas = dict()
for chave in voos.keys() :
    datas[chave] = Data(int(voos[chave].data[:2]), int(voos[chave].data[3:5]), int(voos[chave].data[6:]))

# criacao de listas que contem as possibilidades de idas e de voltas
possiveis_idas = []
possiveis_voltas = []

# se a data do voo esta dentro do periodo de ferias de Jairzinho e se a origem do voo eh o mesmo aeroporto de onde Jairzinho sai,
# adicionamos esse voo na lista de possiveis idas
for chave in voos.keys() :
    if datas[chave].ano == comeca.ano and voos[chave].origem == plano.saida :
        if (datas[chave].mes == comeca.mes and datas[chave].dia >= comeca.dia) or (datas[chave].mes > comeca.mes) :
            if ((datas[chave].ano == acaba.ano and (datas[chave].mes < acaba.mes or (datas[chave].mes == acaba.mes and datas[chave].dia < acaba.dia)))
                or datas[chave].ano < acaba.ano) :
                possiveis_idas.append(chave)
    elif datas[chave].ano < comeca.ano and voos[chave].origem == plano.saida :
        possiveis_idas.append(chave)

# se a data do voo esta dentro do periodo de ferias de Jairzinho e se o destino do voo eh o mesmo aeroporto de onde Jairzinho sai,
# adicionamos esse voo na lista de possiveis voltas
for chave in voos.keys() :
    if datas[chave].ano == acaba.ano and voos[chave].destino == plano.saida :
        if (datas[chave].mes == acaba.mes and datas[chave].dia <= acaba.dia) or (datas[chave].mes < acaba.mes) :
            if ((datas[chave].ano == comeca.ano and (datas[chave].mes > comeca.mes or (datas[chave].mes == comeca.mes and datas[chave].dia > comeca.dia)))
                  or datas[chave].ano > comeca.ano) :
                possiveis_voltas.append(chave)
    elif datas[chave].ano < acaba.ano and voos[chave].destino == plano.saida :
        possiveis_voltas.append(chave)

# criação de uma lista que contem o par ida-volta de Jairzinho
par = []

# selecionamos a viagem mais barata que tem no mínimo 4 dias
# se ha empate no valor, selecionamos a viagem de maior duracao
for i in possiveis_idas :
    for j in possiveis_voltas :
        if voos[i].destino == voos[j].origem and conta_dias(datas[i], datas[j]) >= 4 :
            if len(par) == 0 :
                par.append(i)
                par.append(j)
            elif ((voos[i].valor + voos[j].valor < voos[par[0]].valor + voos[par[1]].valor)
                  or (voos[i].valor + voos[j].valor == voos[par[0]].valor + voos[par[1]].valor
                      and conta_dias(datas[i], datas[j]) > conta_dias(datas[par[0]], datas[par[1]]))) :
                par[0] = i
                par[1] = j

# o programa imprime os numeros dos de ida e de volta que atendem as necessidades de Jairzinho
print (par[0])
print (par[1])

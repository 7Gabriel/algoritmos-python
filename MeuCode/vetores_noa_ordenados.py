
#Estrutura de dados
#Vetor nao ordenado

#Estamos desenvolvendo nossas proprias estruturas de dados, achamos que as implementaçoes
#das bibliotecas de terceiros nao estao atendendo as nossas necessidades.
# Assim sendo, contratamos um desenvolvedor para criar
# uma classe que represente um vetor nao ordenado#
#para que essa que classe atenda as necessidades do software em desenvolvimento
#A implementacao precisa ter ao menos 3 funcionalidades

#Inserir
#Pesquisar
#Excluir

import numpy as np

class VetorNaoOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

    #o(2)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('capacidade maxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    #O(n) - linear
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
            return -1

    #O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultima_posicao -= 1


vetor = VetorNaoOrdenado(10)

vetor.insere(4)
vetor.insere(3)
vetor.insere(2)

vetor.imprime()

vetor.pesquisar(2)

vetor.excluir(2)


vetor.imprime()
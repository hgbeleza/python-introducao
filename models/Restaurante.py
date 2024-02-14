from models.Avaliacao import Avaliacao
from models.cardapio.ItemCardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    # __init__ => método que vai ser chamado quando a classe for instância
    # os atributos passam a ser propriedades obrigatórios
    def __init__(self, nome, categoria):
        # self => convenção usada para referenciar a 
        #         instância atual de uma classe dentro 
        #         dos métodos dessa classe.
        self._nome = nome.title()
        self._categoria = categoria
        self._status = False
        self._cardapio = []
        self._avaliacao = []
        # inserindo o objeto na lista `restaurantes` assim que é instância
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'**NOME DO RESTAURANTE**'.ljust(25)} | {'**CATEGORIA**'.ljust(25)} | {'**AVALIAÇÃO**'.ljust(25)} | {'**STATUS**'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.nota_media).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'working' if self._status else 'not working'

    def alternar_status(self):
        self._status = not self._status

    def receber_avalicao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def nota_media(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        # `isinstance(objeto, classe)` => função embutida que é usada para verificar
        #                                 se um objeto é uma instância de uma classe 
        #                                 ou de uma classe derivada dela.
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                msg_prato = f'{i}. Nome: {item._nome} | R$ {item._preco} | Descrição: {item.descricao}'
                print(msg_prato)
            else:
                msg_bebida = f'{i}. Nome: {item._nome} | R$ {item._preco} | Tamanho: {item.tamanho}'
                print(msg_bebida)

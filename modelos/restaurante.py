from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes=[]
    #F2 troca em todos os lugares necessarios com aquele argumento
    #__init__ cria um construtor que exige os argumentos
    #SELF pode ser substituido com qualquer texto mas é o padrão do python
    def __init__(self, nome, categoria):
        #.title Faz a primeira letra ficar maiuscula 
        self._nome = nome.title()
        #.upper faz todas as letras ficarem maiusculas
        self._categoria = categoria.upper()
        # _ limita o acesso ao argumento 
        self._ativo = False

        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    #__str__ faz a classe ser mostrada como uma string
    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(20)} | Status")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 10:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property
    def  media_avaliacoes(self):
        if not self._avaliacao:
            return "Sem avaliação"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        #round quantidade de casas decimais 
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_item_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"Cardapio do Restaurante {self._nome}\n")
        # i,item in enumerate faz a contagem dos itens da lista
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,"tamanho"):
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}"
                print(mensagem_bebida)
            else:
                    mensagem_prato = f"{i}. Nome: {item._nome} | Preço:R${item._preco} | Descrição: {item.descricao}"
                    print(mensagem_prato)


    
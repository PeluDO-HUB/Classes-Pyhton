from modelos.restaurante import Restaurante
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("praça","Gourmet")
# restaurante_praca.receber_avaliacao("Luiz",10)
# restaurante_praca.receber_avaliacao("Renata",3)
# restaurante_praca.receber_avaliacao("luana",10)

bebida_suco = Bebida("Suco Tradicional",7.0,"Grande")
prato_almoco_dia = Prato("Prato do dia",30.0,"Arroz, feijão e mistura do dia")
prato_almoco_dia.aplicar_desconto()
bebida_suco.aplicar_desconto()
restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_almoco_dia)

restaurante_mexicano = Restaurante("Caliente","Mexicana")
restaurante_pizza = Restaurante("Pizza maluca","Pizzaria")

restaurante_praca.alternar_estado()

def main():
    # Restaurante.listar_restaurantes()
   restaurante_praca.exibir_cardapio
if __name__ == "__main__":
    main()

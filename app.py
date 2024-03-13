from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça","Gourmet")
restaurante_praca.receber_avaliacao("Luiz",10)
restaurante_praca.receber_avaliacao("Renata",3)
restaurante_praca.receber_avaliacao("luana",10)

restaurante_mexicano = Restaurante("Caliente","Mexicana")
restaurante_pizza = Restaurante("Pizza maluca","Pizzaria")

restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()
if __name__ == "__main__":
    main()

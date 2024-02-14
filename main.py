from models.Restaurante import Restaurante
from models.cardapio.Bebida import Bebida
from models.cardapio.Prato import Prato

bebida_1 = Bebida('coca-cola', 5.0, '500ml')
prato_1 = Prato('Pãozinho', 2.0, 'Pãozinho legal')
restaurante_1 = Restaurante('restaurante 1', 'categoria 1')
restaurante_1.adicionar_no_cardapio(bebida_1)
restaurante_1.adicionar_no_cardapio(prato_1)

bebida_1.aplicar_desconto()
prato_1.aplicar_desconto()

def main():
    restaurante_1.exibir_cardapio

if __name__ == "__main__":
    main()
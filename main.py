from models.Restaurante import Restaurante

restaurante_1 = Restaurante('restaurante 1', 'categoria 1')
restaurante_1.alternar_status()
restaurante_1.receber_avalicao('fulano 1', 8)
restaurante_1.receber_avalicao('fulano 2', 10)
restaurante_1.receber_avalicao('fulano 3', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
from sistema.sistema import Sistema

sistema = Sistema()

sistema.get_loja().get_estoque().adicionar_brinquedo('Carrinho', 9.99, '5 anos - 10 anos', 10)
sistema.get_loja().get_estoque().adicionar_brinquedo('Boneca', 24.99, '6 anos - 12 anos', 8)
sistema.get_loja().get_estoque().adicionar_brinquedo('Quebra-Cabeça', 37.99, '10 anos - 15 anos', 15)
sistema.get_loja().get_estoque().adicionar_brinquedo('Bola de Futebol', 60.00, '8 anos - 17 anos', 5)

sistema.get_loja().registrar_usuario('Maria', '037.080.006-09', '68909-094', '(96) 99386-3947', 'maria@email.com', 5534487465411109, 'A1@senha')
sistema.get_loja().registrar_usuario('João', '593.691.990-04', '62031-080', '(88) 98431-5735', 'joao@email.com', 4539532077833899, 'B2@senha')
sistema.get_loja().registrar_usuario('José', '486.905.496-50', '29194-548', '(27) 98221-4584', 'jose@email.com', 214959681938006, 'C3@senha')

def main():
    sistema.run()
    
if __name__ == "__main__":
    main()
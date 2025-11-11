precos_base = [20, 15, 10]

capacidade = [50, 50, 40, 40, 30, 30]
assentos_disponiveis = [50, 50, 40, 40, 30, 30]

vendidos_inteira = [0, 0, 0, 0, 0, 0]
vendidos_meia = [0, 0, 0, 0, 0, 0]
vendidos_vip = [0, 0, 0, 0, 0, 0]

receita_inteira = [0, 0, 0, 0, 0, 0]
receita_meia = [0, 0, 0, 0, 0, 0]
receita_vip = [0, 0, 0, 0, 0, 0]

avaliacoes = [[], [], []] # 0: Filme 1, 1: Filme 2, 2: Filme 3
ingressos = [[], [], []] # 0: Inteira, 1: Meia, 2: VIP

def avaliar_filme ():
    filme = int(input("Escolha um filme para avaliar:\n1. Avaliar Filme 1\n2. Avaliar Filme 2\n3. Avaliar Filme 3\n"))

    while (filme > 0) and (filme < 4):
        if filme == 1: 
            avaliacao = int(input(f"Avalie o Filme {filme} (1 a 5 estrelas) "))
            if (avaliacao > 0) and (avaliacao  < 6):
                print ("Avaliação registrada com sucesso.")
                avaliacoes[0].append(avaliacao)
            else:
                print("Erro: A nota deve ser entre 1 e 5.")
        elif filme == 2: 
            avaliacao = int(input(f"Avalie o Filme {filme} (1 a 5 estrelas) "))
            if (avaliacao > 0) and (avaliacao  < 6):
                print ("Avaliação registrada com sucesso.")
                avaliacoes[1].append(avaliacao)
            else:
                print("Erro: A nota deve ser entre 1 e 5.")
        elif filme == 3: 
            avaliacao = int(input(f"Avalie o Filme {filme} (1 a 5 estrelas) "))
            if (avaliacao > 0) and (avaliacao  < 6):
                print ("Avaliação registrada com sucesso.")
                avaliacoes[2].append(avaliacao)
            else:
                print("Erro: A nota deve ser entre 1 e 5.")
                menu_principal()
        break

def exibe_relatorio():
    print("Relatório Final")

def compra_ingressos():
    
    print(f"\nompra realizada com sucesso!")
    print(f"Valor total: R$ {total:.2f}")
    print(f"Assentos restantes: {assentos_disponiveis[indice]}")

def menu_principal():
    opcao = int(input("1. Comprar ingressos para Filme 1 - Sessão 1\n2. Comprar ingressos para Filme 1 - Sessão 2\n3. Comprar ingressos para Filme 2 - Sessão 1\n4. Comprar ingressos para Filme 2 - Sessão 2\n5. Comprar ingressos para Filme 3 - Sessão 1\n6. Comprar ingressos para Filme 3 - Sessão 2\n7. Avaliar um filme\n8. Encerrar o dia e exibir o relatório\n"))

    while (opcao > 0) and (opcao < 9):
        if (1 <= opcao <= 6): 
            compra_ingressos()
        elif (opcao == 7): 
            avaliar_filme()
        elif (opcao == 8):
            exibe_relatorio()
        else:
            print ("Opção inválida.")
        break

menu_principal()
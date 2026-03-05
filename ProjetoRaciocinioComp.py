portfolio_musicas = {}
musicas = []
import datetime
import json

# CRIA O MENU PRINCIPAL
def abrir_menu_principal():
    print("\n----- MENU PRINCIPAL - MÚSICAS -----\n")
    print("ADD - Incluir Nova Música")
    print("LIST - Lista a quantidade e o nome das Músicas já cadastradas")
    print("ABOUT - Informação do Responsável pelo Portfólio")
    print("EDIT - Alterar uma Música")
    print("DOWNLOAD - Altera o Status da Música para Baixada")
    print("DEL - Excluir uma Música cadastrada")
    print("QUIT - Sair do Registro de Músicas\n")

# CRIA A FUNÇÃO PARA SALVAR O ARQUIVO JSON
def salvar_dados():
    with open('musicas_salvas.json', 'w') as projeto_salvo:
        json.dump(musicas, projeto_salvo)

# CRIA A FUNÇÃO PARA ABRIR O ARQUIVO JSON
def abrir_arquivo_salvo():
    try:
        global musicas
        with open('musicas_salvas.json', 'r') as projeto_salvo:
            musicas = json.load(projeto_salvo)

    except FileNotFoundError:
        print('Arquivo não encontrado!')
        musicas = []


# CRIA A LISTA ORDENADA
def ordenar_musica(musica):
    return musica['nome']

# CRIA A FUNÇÃO PARA EXIBIÇÃO DAS MÚSICAS

def listar_musicas():
    if len(musicas) != 0:
        lista_ordenada = sorted(musicas, key=ordenar_musica)
        print(f'\nAtualmente você tem {len(musicas)} Músicas cadastradas. São elas:')
        # Sugestão do GEMINI AI para exibir corretamente o nome das chaves:
        nomes_para_exibir = {
            'nome': 'Nome da Música',
            'estilo': 'Estilo Musical',
            'artista': 'Nome do Artista / Banda',
            'status': 'Baixada?',
            'historico': 'Histórico'
        }
        for item, musica in enumerate(lista_ordenada):
            # Usamos o "item" para criar um cabeçalho bonito
            print(f'\n--- MÚSICA {item + 1} ---')
            for chave, valor in musica.items():
                # O capitalize() deixa a chave mais bonita (ex: 'Nome' em vez de 'nome')
                nome_bonito = nomes_para_exibir.get(chave, chave.upper())
                if chave == 'status':
                    if valor == True:
                        valor = 'Sim'.upper()
                    else:
                        valor = 'Não'.upper()
                elif chave == 'historico':
                    print(f'{nome_bonito}:')  # Imprime o título
                    for item in valor:
                        # 1. Pega a Data (posição 0)
                        data = item[0]
                        # 2. Pega a Descrição (posição 1)
                        descricao = item[1]
                        # 3. Formata a data com Horas e Minutos
                        data_str = data #.strftime('%d/%m/%Y %H:%M')
                        # 4. Imprime a linha formatada
                        print(f'   - {descricao} em {data_str}')
                    continue
                print(f'{nome_bonito}: {valor}')

            print('-' * 50)  # Separador no final
        input('\nPRESSIONE <ENTER> para continuar...')
    else:
        print('Você não tem nenhuma Música cadastrada.')
        input('\nPRESSIONE <ENTER> para continuar...')

# ABRE MENU / "LOOP" PRINCIPAL DO CÓDIGO

abrir_arquivo_salvo()
while True:

    # ABRE O MENU PRINCIPAL
    abrir_menu_principal()

    opcao = input("Digite a opção: ").upper()

    #BLOCO QUE CRIA A LISTA DE PORTFÓLIOS
    match opcao:

        case 'ADD':
            #INICIA O LOOP PARA INCLUSÃO DOS PORTFOLIOS
            while True:
                try:
                    cadastro_de_musicas = int(input('\nQuantas novas Músicas você quer cadastrar? '))
                    if cadastro_de_musicas <= 0:
                        # COMANDO RAISE SUGERIDO PELO MONITOR 21/12/25
                        raise ValueError
                except ValueError:
                    print('Número de Músicas à cadastrar inválido, digite novamente: ')
                    continue
                else:
                    for i in range(cadastro_de_musicas):
                        while True:
                            nome_da_musica = input('\nDigite o Nome da música: ').upper()
                            nome_ja_existe = False
                            for m in musicas:
                                if nome_da_musica == m['nome'].upper():
                                    nome_ja_existe = True
                            if nome_ja_existe:
                                print(f'\nVocê já cadastrou a musica {nome_da_musica}')
                                continue
                            elif nome_da_musica == '':
                                print('Nome inválido, digite novamente: ')
                                continue
                            else:
                                data_str=datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
                                estilo_da_musica = input('\nDigite o Estilo da música: ').upper()
                                nome_do_artista = input('\nDigite o Nome do Artista: ').upper()
                                portfolio_musicas = {'nome': nome_da_musica,
                                                     'estilo': estilo_da_musica,
                                                     'artista': nome_do_artista,
                                                     'status': False,
                                                     'historico': [(data_str, 'Cadastro inicial: ')]}
                                musicas.append(portfolio_musicas)
                                print(f'\nSUCESSO! Música ' + portfolio_musicas['nome'] + ' adicionada!')
                                salvar_dados()
                                input('\nPRESSIONE <ENTER> para continuar...')
                            break
                    break

        # BLOCO QUE EXIBE A QUANTIDADE E QUAIS PORTFÓLIOS JÁ ESTÃO CADASTRADOS.

        case 'LIST':
            listar_musicas()
            continue

        # BLOCO QUE MOSTRA O RESPONSÁVEL PELOS PORTFÓLIOS.
        case 'ABOUT':
            print('Aluno: Emanoel Douglas Nascimento')
            input('\nPRESSIONE <ENTER> para continuar...')
    
        #BLOCO QUE PERMITE A ALTERAÇÃO DE PORTFÓLIOS CADASTRADOS.
        case 'EDIT':
            if len(musicas) == 0:
                print('Você não tem nenhuma Música cadastrada.')
                input('\nPRESSIONE <ENTER> para continuar...')
                continue
            listar_musicas()
            editmusica = input('\nDigite o nome da Música para alterar: ').upper()
            musica_encontrada = None
            for m in musicas:
                if editmusica == m['nome'].upper():
                    musica_encontrada = m
                    break
            if musica_encontrada != None:
                data_str = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
                nova_musica = input('\nDigite o nome da Nova Música para alterar: ').upper()
                musica_encontrada['nome'] = nova_musica
                musica_encontrada['estilo'] = input('\nDigite o nome do novo Estilo para alterar: ').upper()
                musica_encontrada['artista'] = input('\nDigite o nome do novo Artista para alterar: ').upper()
                nova_ocorrencia = (data_str, 'Dados atualizados')
                musica_encontrada['historico'].append(nova_ocorrencia)
                print(f'A música: {editmusica}, foi alterada para {nova_musica}, com novo estilo: {musica_encontrada["estilo"]}'
                      f' e novo artista: {musica_encontrada["artista"]}')
                salvar_dados()
                input('\nPRESSIONE <ENTER> para continuar...')
            else:
                print('\nVocê nao tem nenhuma Música cadastrada com este nome.')
                input('\nPRESSIONE <ENTER> para continuar...')
                continue

        #BLOCO QUE PERMITE A ALTERAÇÃO DO STATUS DA MÚSICA PARA BAIXADA
        case 'DOWNLOAD':
            if len(musicas) == 0:
                print('Você não tem nenhuma Música cadastrada.')
                input('\nPRESSIONE <ENTER> para continuar...')
                continue
            listar_musicas()
            editmusica = input('\nDigite o nome da Música para alterar: ').upper()
            musica_encontrada = None
            for m in musicas:
                if editmusica == m['nome'].upper():
                    musica_encontrada = m
                    break
            if musica_encontrada != None:
                data_str = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
                musica_encontrada['status'] = True
                nova_ocorrencia = ((data_str), 'Música baixada em:')
                musica_encontrada['historico'].append(nova_ocorrencia)
                print(f'A música: {editmusica}, foi baixada em {data_str}')
                input('\nPRESSIONE <ENTER> para continuar...')
            else:
                print('\nVocê nao tem nenhuma Música cadastrada com este nome.')
                input('\nPRESSIONE <ENTER> para continuar...')
                continue

        # BLOCO QUE PERMITE A EXCLUSÃO DE PORTFÓLIOS CADASTRADOS.
        case 'DEL':
            while True:
                if len(musicas) == 0:
                    print('Você não tem nenhuma Música cadastrada.')
                    input('\nPRESSIONE <ENTER> para continuar...')
                    break
                listar_musicas()
                excluir_musica = input('\nDigite o nome da Música para excluír ou "ALL" para todas: ').upper()

                if excluir_musica == 'ALL':
                    opcaoall = input('Tem certeza? (S/N) - ESTA OPERAÇÃO NÃO PODERÁ SER DESFEITA! ').upper()
                    if opcaoall == 'S':
                        musicas.clear()
                        print('\nTodas as Música Removidas!')
                        input('\nPRESSIONE <ENTER> para continuar...')
                        break

                    elif opcaoall == 'N':
                        input('\nPRESSIONE <ENTER> para voltar ao MENU...')
                        break
                else:
                    musica_encontrada = None
                    for m in musicas:
                        if excluir_musica == m['nome'].upper():
                            musica_encontrada = m
                            break
                    if musica_encontrada != None:
                        opcaomusica = input('Tem certeza? (S/N) ´ESTA OPERAÇÃO NÃO PODERÁ SER DESFEITA! ').upper()

                        if opcaomusica == 'S':
                            musicas.remove(musica_encontrada)
                            print(f'\nMúsica {excluir_musica}, Removida!')
                            input('\nPRESSIONE <ENTER> para continuar...')
                            break
                        else:
                            input('\nPRESSIONE <ENTER> para continuar...')
                            break
                    else:
                        print('\nVocê nao tem nenhuma Música cadastrada com este nome.')
                        input('\nPRESSIONE <ENTER> para continuar...')
                        break

        #BLOCO QUE ENCERRA O CÓDIGO
        case 'QUIT':
            salvar_dados()
            print('Dados atualizados com sucesso.')
            print("Saindo do gestor de portfolio!")
            break  # FECHA O LOOP PRINCIPAL DO CÓDIGO
    
        #BLOCO QUE VERIFICA O COMANDO INICIAL CORRETO A SER DIGITADO
        case _:
            print('Erro! Comando não reconhecido! Por favor digite novamente: ')
            input('\nPRESSIONE <ENTER> para continuar...')
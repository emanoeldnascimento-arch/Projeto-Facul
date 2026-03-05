# Diário de Bordo de IA - Emanoel Douglas Nascimento

Data 21/10/25   
## Dificuldade encontrada:
Eu não conseguia fazer o tratamento do dado
digitado pelo usuário quando ele digita a 
quantidade de Protfólios quer cadastrar.
Se digitar menor que 0 trata o erro, porém se 
digitasse uma string, o código quebrava
Na mentoria, me foi passado o comando.
Tentei com o o Try / Exeption e na mentoria me 
orientaram a usar, também, o comando "raise".
O código rodou certinho...

Questionei, também, ao Gemini, como fazer o 
programa parar, até que o usuário pressionasse 
uma tecla. Implementação esta, que fiz ao digitar
os comandos LIST e EDIT, pois são menus em 
desenvolvimento. O usuário receberá a mensagem 
"MENU PARA EDITAR OS PORTFÓLIOS, EM 
DESENVOLVIMENTO!" e o programa aguardará até que
pressione a tecla ENTER.

### PROMPT ENVIADO PARA A IA:
Como fazer uma linha de um programa parar até 
que o usuário pressione uma tecla para o programa
continuar rodando?

## RESPOSTA DA IA (RESUMO):
O input() é usado principalmente para receber
dados do usuário, mas ele trava a execução do 
programa até que o usuário digite algo e 
pressione a tecla Enter.

Data 25/11/205

Implementei a lista de "listadeportfolios" para inclusão dos novos Portfólios.

Implementei no Menu Principal a opção "ADD", que adiciona novos Portfólios na
lista de portfólios.
Esta implementação verifica se as entradas do usuários (novos Portfólios), já estão
cadastrados. Caso já estejam, informa com a mensagem "Este Portfólio já foi 
incluído. Digite o próximo: "

Implementei no Menu Principal a opção "QTD", para verificar a quantidade de 
Portfólios cadastrados e informar quais Portfólios já estão cadastrados.

Implementei no Menu Principal a opção para "DEL" para excluir um portfólio já 
cadastrado.
Este comando informa os Portfólios cadastrados e pergunta qual portfólio deve 
ser excluído.

Implementei no Menu "QTD" e "DEL" a função sorted(), para que a lista seja exibida
em órdem alfabética ao usuário.
 
A dúvida que persistiu foi com relação a estrutura do bloco "try, except, else"
Questionei ao Gemini para tentar esclarecer a estrutura do bloco, e conseguir
resolver os erros do programa.

### ### PROMPT ENVIADO PARA A IA:
O comando try pode ser usado com o else, no python?

## RESPOSTA DA IA (RESUMO):
Sim, o bloco try pode ser usado com o else. A estrutura completa é geralmente
try...except...else...finally.
Essa estrutura (try...except...else) é muito útil para controlar o fluxo do
programa em relação ao tratamento de erros.
Nós sabemos que o bloco except é executado apenas quando ocorre um erro 
(Exception) no bloco try.

### Com esta explicação consegui definir corretamente o bloco "ADD" para inclusão de novos Portfólios.


Data 27/010/2025

Pesquisei na documentação do Python a correta extensão para utilizar o comando sorted()
Pelo que verifiquei, no meu código, o retorno está sendo em órdem alfabética, porém ao
digitar os dados numericos, como "Nom de Protfóli", exmplo: Portfólio: 1, 2, etc..
O sistema não reconhece por exemplo o número 20, ou 35, ele considera 2.0 ou 3.5 ai 
a órdem apresentada fica incorreta...

## QUESTIONEI PARA O GEMINI, PORQUE ISTO ACONTECE:

## PROMPT ENVIADO PARA A IA:
Porque o comando soreted(), não coloca em órdem números maiores que 10? 
Ou seja ele reconhece o número 20 ou 35, como 2.0 ou 3.5 mas não como vinte
ou trinta e cinco. Desta forma a ordem apresentada fica incorreta..

### RESPOSTA DO GEMINI (RESUMIDA):
Essa é uma excelente observação, e o problema que você está descrevendo acontece
não porque o sorted() não consegue ordenar números maiores que 10, mas porque
ele está tratando a sua lista como uma lista de STRINGS (texto), e não como uma
lista de NÚMEROS (inteiros ou floats).Quando o Python ordena strings, ele faz
uma ordenação lexicográfica (alfabética), comparando caractere por caractere
a partir do primeiro.1. Como o sorted() Vê a Sua Lista (Como Strings)
Quando você tem uma lista de strings, o Python ordena assim:
Ordem Errada (Strings)Como o Python Compara (Caractere por Caractere)'1'O 1º caractere '1' vem antes de '2' e '3'.'10'O 1º caractere '1' vem antes de '2' e '3'.'2'O 1º caractere '2' vem antes de '3'.'20'O 1º caractere '2' vem antes de '3'.'3'O 1º caractere '3' é o último na comparação inicial.'35'O 1º caractere '3' é o último na comparação inicial.

## Questinado para o Gemini:
## Como aceitar na lista, dados alfanumericos, com reconhecimento dos números decimais ou centesimais?

### RESPOSTA DO GEMINI:
Ótima pergunta! Se você está lidando com uma lista que contém tanto texto 
(alfanumérico) quanto números, e esses números podem incluir decimais/centesimais
(usando vírgula como separador decimal, comum no Brasil), a ordenação se torna
mais complexa.
O Python usa o ponto (.) como separador decimal padrão. Se os seus dados usam
a vírgula (,), você terá que tratar isso na função de ordenação.
Para resolver isso, você precisa usar o parâmetro key do sorted() junto com 
uma função personalizada (geralmente uma lambda) que lida com a conversão 
de forma inteligente.

Solução: Função key que Lida com Texto, Números e Vírgulas
A melhor abordagem é criar uma função que tenta converter o item para um 
número (tratando a vírgula) e, se a conversão falhar (porque o item é texto), 
retorna o próprio item para ordenação alfabética.
Exemplo:

def obter_chave_ordenacao(item):
    """
    Tenta converter o item para float, tratando a vírgula como separador decimal.
    Se não for um número válido, retorna o próprio item para ordenação alfabética.
    """
    try:
        # 1. Tenta substituir a vírgula (,) por ponto (.) para o Python entender o decimal
        item_para_converter = str(item).replace(',', '.')
        
        # 2. Tenta converter para float (número decimal)
        # Multiplicamos por 1 para garantir que números sejam tratados como números
        return float(item_para_converter) * 1  
    except ValueError:
        # Se falhar (porque é texto ou alfanumérico), retorna o item original (texto)
        return str(item)

Exemplo da sua lista com dados misturados e decimais com vírgula:
dados_mistos = ["Maçã", "2,5", "Banana", "10", "Uva", "1,85", "20,0", "1"]

Usa a função personalizada no 'key' do sorted()
lista_ordenada = sorted(dados_mistos, key=obter_chave_ordenacao)

print("Lista Original:", dados_mistos)
print("Lista Ordenada:", lista_ordenada)

## O que consegui resolver com a explicação da IA:

Como não aprendemos o comando "def" função. Tentei implementar a lógica para 
ordenação da lista, no inicio do programa, logo após a criação da lista,
porém sem sucesso! Vamos aguardar mais algumas aulas... :)



Conversei na Mentoria com a Julia e ela me orientou a usar a Função DEF, para organizar
melhor o código.
Criamos a função "def obter_chave_ordenacao(item):" que trata os itens da lista,
deixando os itens da lista organizados (valores numericos e string´s)
Esta função é chamada quando executadas as opções "ADD", "QTD" e "DEL"

Implementamos a validação na entrada de dados "ADD" verificando se a variável digitada
possui "," caso positivo print "Digite o valor sem virgula".
O problema desta validação é que o sistema considera sempre a virgula digitada
como um erro. Ou seja, não verifica apenas números, mas alfanumerico também. Se o 
nome digitado for "teste,1" acusa erro e pedirá para digitar outro nome sem virgula.
Implementamos o comando "continue" que interrompe o loop e retorna para a mesma
sequencia interrompida.

Data 28/10/2025

Implementei o parâmetro "EDIT" que altera o nome dos Portfolios cadastrados.
Com ajuda do GEMINI, consegui implementar a alteração da seguinte forma:
Primeiramente criamos uma variável para guardar o elemento que vamos alterar "editlist"
Verificamos em qual posição da lista (indice) está o elemento que queremos alterar:
indice_editlist = listadeportfolios.index(editlist)
Criamos uma nova variável "novoitem" para guardar o nome novo para o Portfolio.
Alteramos o nome antigo para o novo com o comando:
listadeportfolios[indice_editlist] = (novoitem), finalizando com a mensagem:
print(f"\n{editlist} alterado com sucesso! Novo nome: {novoitem}")

## Perguntas feitas para a IA: 
## Em python, qual o comando para alterar uma lista?
## Como eu verifico qual o indice de um item da lista?
## Como fazer a alteração de um item da lista, se não sabemos em que indice o item está?


### Primeiramente o GEMINI seguiu com o raciocínio para localizar a indexação do valor dentro
### da lista que temos que alterar: 
### frutas = ['uva', 'banana', 'maçã'] (Modificar o elemento no índice 1 (que é 'banana') para 'laranja'
### frutas[1] = 'laranja' 
### print(frutas) 
### Resultado: ['uva', 'laranja', 'maçã']
 
### Para o segundo questionamento, a opção dada pelo GEMINI foi 
### o comando: lista.index(valor_do_item)
### Com este comando foi possível indenificar, dentro da lista o item a ser alterado.
### Por fim, consegui implementar a alteração com a criação de variáveis para guardar o indice
### correto do item a ser alterado, finalizando a alteração com o comando 
### listadeportfolios[indice_editlist] = (novoitem)


## Data 29/10/2025

O ajuste sugerido pelo professor era para listar os portfólios, na opção LIST, um em cada
linha e não na mesma linha como havia implementado antes:
Após várias tentativas sem sucesso, questionei para o GEMINI, da seguinte forma:

Este é o código em Python: (anexei o código)
Precisamos listar os portfólios cadastrados, quanto o usuário digia a opção LIST, em linhas diferentes e em órdem ascendente, como fazer? Explique detalhadamente, como se eu tivesse 10 anos.

## Resposta da IA foi apenas para organizar as linhas do bloco LIST. A lógica de processamento estava incorreta. Bastava organizar a lista apenas uma vez e mostrar o cabeçalho apenas uma vez: "print(f"\nAtualmente você tem {len(listadeportfolios)} Portfólios cadastrados. São eles:")" Na sequencia fazer o loop "for item in lista_ordenada", para imprimir os portfólios, cadastrados, um em cada linha.

## Com esta explicação, consegui implementar esta lógica nos blocos "EDIT" e "DEL", deixando a exebição mais estética.

### Aproveitei também, para explorar a sintaxe do comando "enumerate", explicado pelo GEMINI:

## Data 31/10/2025

## Dificuldade encontrada:

Eu fiz, utilizando o match / case, uma condição para validar a edição de 
alteração dos porfólios cadastrados, porém o match/case não trata a condição.
Por exemplo: caso o "novoitem" esteja na lista (in listadeportfolios), faça:

### Prompt enviado ao GEMINI:
o comando case pode ser usado da forma:
case novoitem in listadeportfolios:

### Resposta da IA:
O match/case não usa in para verificar associação. A sintaxe case... in... não é um 
recurso nativo do Structural Pattern Matching (match/case) no Python.
O match/case é projetado principalmente para verificar a ESTRUTURA (ou seja, o 
formato, os elementos, ou os atributos) de um objeto, e não para verificar se
um item pertence a uma coleção.
Para fazer essa verificação de associação (in) dentro de um bloco match/case,
você precisa usar uma cláusula if (ou Guard - Guarda). A cláusula if é 
uma condição adicional que você pode anexar a qualquer case. O case só é 
executado se o padrão for correspondido e a condição if for True.
Veja como seu cenário seria implementado corretamente:
"case item_capturado if item_capturado in lista_de_portfolios:"
Explicação:
match novo_item: O objeto que está sendo avaliado é a variável novo_item.
case item_capturado: O match primeiro tenta casar com este padrão. Um nome 
de variável simples aqui, como item_capturado, atua como um padrão de captura
e sempre tem sucesso (ele captura o valor de novo_item).
if item_capturado in lista_de_portfolios: Este é o Guard (Guarda). 
Ele verifica se o item capturado está dentro da sua lista. Se for True, 
o código dentro do case é executado.

### Minha análise e Aprendizado
Eu entendi que a estrutura match/case somente pode ser utilizada para associações
simples (formatos, elementos ou atributos), porém para associações mais elaboradas
o ideal é usar a estrutura if/else/case.
Porém, podemos acossiar o if com o case, como neste caso, na linha do programa:
case novoitem if novoitem in listadeportfolios:
o comando if valida de o novo item está na listadeprotfolios, e caso positivo
executa o case, caso negativo o case é igonrado e o programa segue.


## Data 19/11/25

### Dificuldade: Não estava entendendo como criar o novo dicionário dentro da Lista já criada. Eu entendi que deveria apenas substituir a lista pelo dicionário.

### Pergunta ao Gemini: Preciso refatorar o código abaixo (anexei o Código anterior só com a lista), com listas já existente, incluindo dicionários e listas, como devo fazer?

### Resposta do Gemini:
Vamos trabalhar nessa refatoração juntos! É uma excelente ideia evoluir de uma lista simples de nomes (strings) para uma lista de dicionários. Isso vai permitir que o seu programa escale e guarde muito mais informações sobre cada portfólio no futuro.
A mudança de conceito
Atualmente, a sua estrutura de dados se parece com isto:
### Lista de Strings (Atual)
listadeportfolios = ["ACOES", "FUNDOS", "CRIPTOS"]

Para usar dicionários, vamos transformar cada item da lista em um "objeto" com propriedades. A estrutura passará a ser algo assim:
### Lista de Dicionários (Meta)
listadeportfolios = [
    {"nome": "ACOES", "id": 1, "data_criacao": "21/12/2025"},
    {"nome": "FUNDOS", "id": 2, "data_criacao": "22/12/2025"}
]
Isso muda a forma como acessamos os dados (ao invés de só chamar o item, chamaremos item['nome'], por exemplo).

## O que aprendi com o GEMINI
Após algumas tentativas a consegui montar a estrutura do dicionário e entender que ele fica alocado dentro da lisa.
Uma lista pode conter vários dicionários de forma infinita..
Entendi que a inclusão dos dados no dicionário se dá pelo comando:
musica_encontrada['estilo'] = input('\nDigite o nome do novo Estilo para alterar: ').upper()
Para cada informação a ser digitada mudamos apenas a chave mas a variável "musica_encontrada" é a mesma para alocação dos dados corretamente.
A Estrutura para inclusão do dicionário completa finalizada, ficou assim:

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
                                estilo_da_musica = input('\nDigite o Estilo da música: ').upper()
                                nome_do_artista = input('\nDigite o Nome do Artista: ').upper()
                                portfolio_musicas = {'nome': nome_da_musica,
                                                     'estilo': estilo_da_musica,
                                                     'artista': nome_do_artista,
                                                     'status': False,
                                                     'historico': [(datetime.datetime.now(), 'Cadastro inicial: ')]}
                                musicas.append(portfolio_musicas)
                                print(f'\nSUCESSO! Música ' + portfolio_musicas['nome'] + ' adicionada!')
                                input('\nPRESSIONE <ENTER> para continuar...')

### Outra dificuldade foi entender como o código mostraria ao usuários os dados do Dicionários de forma correta.
Por exemplo: "Histórico" em vez de "historico"

Questionado ao Gemini, como fazer esta adaptação. num primeiro momento foi passado o comando .capitalize(), porém este comando apenas torna maiúscula a primeira letra da chave
Questionado ao Gemini:
Qual a outra opção para o captalizs(), se eu quiser mostrar o Historico, com o acento: Histórico?

Resposta do Gemini:
Para resolver isso de forma profissional, usamos o que chamamos de "Dicionário de Tradução" (ou Label Mapping).
A ideia é simples: você cria um dicionário separado que serve apenas para dizer: "Quando o código ler 'historico', mostre na tela 'Histórico'"
Vantagens:
Flexibilidade: Podemos mudar o texto da tela, sem precisr mudar o nome da variável no banco de dados ('nome')
Segurança: Se no decorrer do dias, acrescentarmos um novo campo e esquecermos de colocar no "tradutor", o comando .get(chave, chave.upper()) garante que o código não quebra, ele apenas mostra o nome original em maiúsculo como reserva.
Como ficou o código depois desta alteração:

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
                        data_str = data.strftime('%d/%m/%Y %H:%M')
                        # 4. Imprime a linha formatada
                        print(f'   - {descricao} em {data_str}')
                    continue
                print(f'{nome_bonito}: {valor}')

            print('-' * 50)  # Separador no final
        input('\nPRESSIONE <ENTER> para continuar...')

este bloco está dentro do bloco List

## O que aprendi com o Gemini:
Esta forma de mostrar as variáveis em tela com nome mais atrativo é um tipo de "mascara" que o código vai puxar apenas para jogar as informações na tela.

## Data 21/11/25

Reescrevi a função def que organizava o código em órdem alfabética, deixando mais "limpa" 
Como era:

        # ORGANIZA A LISTA EM ORDEM CRESCENTE
        def obter_chave_ordenacao(item):
            try:
                valor_numerico = float(item)
                return 0, valor_numerico
            except ValueError:
                return 1, item.upper()

como ficou:

        # CRIA A LISTA ORDENADA
        def ordenar_musica(musica):
            return musica['nome']

No bloco LIST foi inserido a linha:
        
        lista_ordenada = sorted(musicas, key=ordenar_musica)

Esta alteração foi implementada com auxílio do pessoal da Monitoria (Julia e Denian)
A lista ordenada foi criada com o comando sorted.

## Data 27/11/25

Na live com a mentoria (Julia e Denian), revisamos o comando "LIST", dentro da função que já havia sido criada, porém não estava funcionando corretamente
Não estava listando as músicas em órdem alfabética.
Foi corrigido a função "ordenar_musica" e a linha com o comando sorted.
Ai o código rodou corretamente.

## Data 30/11/2025

### Questionei ao Gemini, como incluir o comando "with", para criar arquivos Jason e garantir que os dados não sejam perdidos ao encerrar o código.

### Resposta do Gemini, primeiramente tería que alterar a entrada de dados no bloco ADD, pois o dicionário, no campo "historico" está com o comando "datetime.datetime.now()", muito complexo para o jason "entender"

Transformamos os dados em uma variável "data_str" string para não dar conflito no Jason



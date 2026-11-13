'''
UC003 - Manter cobranças

Objetivo: Permitir que o tesoureiro cadastre, edite e consulte cobranças
dos cooperados, com geração das parcelas.

Requisitos:
- RF05001

Ator:
- Tesoureiro

Responsável pela elaboração: Ludmilla Judaico
'''

# 🟢 [FP] - FLUXO PRINCIPAL (CADASTRAR COBRANÇA PARCELADA)
# ---------------------------------------------------------------

# O ator acessa a página de cobranças, o sistema exibe a página de listagem de cobranças. O tesoureiro acessa o formulário de cadastro de cobrança. Ele verifica que o
# título do formulário é "Cadastro de cobranças". Ele observa que existem
# os campos:
# - Cooperado
# - Nome da cobrança
# - Descrição
# - Recorrência (Única, Parcelada ou Recorrente)
# - Valor (R$)
# - Número de parcelas
# - Intervalo entre parcelas (dias)
# - Data de lançamento
# - Data do primeiro vencimento
# - Tipo de juros (simples ou composto)
# - Taxa de juros (%)
# - Opções
# -- Botão "Salvar"
# -- Botão "Cancelar"

# O ator seleciona um cooperado ativo, informa o nome "Mensalidade",
# a categoria "Mensalidade", a recorrência "Parcelada", o valor
# R$ 1.000,00, 3 parcelas, intervalo de 30 dias, a data de lançamento
# e a data do primeiro vencimento.

# O ator seleciona o tipo de juros "Simples" e a taxa de 2%.

# O ator seleciona a opção "Salvar". [A6][A7][E1][E2][E3]

# O sistema verifica que os dados estão corretos [RN1] [RN2] [RN3]

# O sistema gera as 3 parcelas com status "Aberta" [RN4]

# O sistema exibe uma mensagem de sucesso.

# O ator retorna para a página de cobranças.

# O ator verifica que a cobrança cadastrada está na lista.

# O ator abre o detalhe da cobrança e verifica as 3 parcelas, todas
# com status "Aberta" e valores 333,33 / 333,33 / 333,34.


# 🟠 [A1] - BUSCAR COBRANÇA
# ---------------------------------------------------------------

# O ator acessa a página de cobranças.

# O sistema exibe a listagem de cobranças.

# O ator informa o nome da cobrança (ou o cooperado) no campo de busca
# e seleciona 'Pesquisar'.

# O sistema exibe somente as cobranças que correspondem aos termos
# digitados, sem os registros removidos.

# Caso não haja resultados, o sistema exibe uma mensagem informativa.


# 🟠 [A2] - CONSULTAR DETALHE DA COBRANÇA
# ---------------------------------------------------------------

# O ator executa [A1].

# O ator seleciona uma cobrança da lista.

# O sistema exibe o detalhe com:
# - Dados da cobrança
# - Parcelas (valor original, valor atualizado e status)
# - Comprovantes
# - Histórico de alterações

# O ator verifica que as informações correspondem ao cadastro.


# 🟠 [A3] - EDITAR COBRANÇA
# ---------------------------------------------------------------

# O ator executa [A1].

# O ator seleciona a cobrança e clica no botão para editar.

# O sistema exibe a página de edição com os campos preenchidos. O campo
# "Cooperado" está bloqueado para alteração. [E4]

# O ator altera o valor da cobrança e seleciona "Salvar". [E5]

# O sistema recalcula somente as parcelas ainda não pagas. As parcelas
# pagas permanecem inalteradas. [RN5]

# O sistema registra no log de auditoria o usuário, a data, a hora e os
# valores anterior e novo de cada campo alterado.

# O sistema exibe mensagem de sucesso.

# O ator abre o detalhe da cobrança e verifica o novo valor das
# parcelas não pagas.


# 🟠 [A4] - CADASTRAR COBRANÇA ÚNICA
# ---------------------------------------------------------------

# O ator executa o fluxo principal, mas seleciona a recorrência "Única".

# O sistema bloqueia os campos "Número de parcelas" (1) e "Intervalo"
# (0). [RN6]

# O ator preenche os demais campos e seleciona "Salvar".

# O sistema gera uma única parcela com status "Aberta".


# 🟠 [A5] - CADASTRAR COBRANÇA RECORRENTE
# ---------------------------------------------------------------

# O ator executa o fluxo principal, mas seleciona a recorrência
# "Recorrente".

# O sistema oculta o campo "Número de parcelas" e informa que o valor
# é o de cada ciclo. [RN7]

# O ator preenche os demais campos e seleciona "Salvar".

# O sistema gera somente a primeira parcela. As demais são geradas
# pela rotina do UC001.


# 🟠 [A6] - CANCELAR O CADASTRO
# ---------------------------------------------------------------

# O ator seleciona "Cancelar" antes de salvar.

# O sistema descarta os dados e retorna à listagem. Nenhuma cobrança
# é criada e nenhum registro de log é gerado.


# 🟠 [A7] - FILTRAR COBRANÇAS
# ---------------------------------------------------------------

# O ator executa [A1] e aplica filtros por status, período, valor
# mínimo e máximo, recorrência e ativas/inativas.

# O sistema exibe a lista paginada, agrupada por mês de vencimento,
# respeitando os filtros.


# 🔴 [E1] - CAMPOS OBRIGATÓRIOS NÃO PREENCHIDOS
# ---------------------------------------------------------------

# O ator seleciona "Salvar" sem preencher algum campo obrigatório.

# O sistema destaca os campos inválidos, exibe mensagem de erro e não
# salva a cobrança.


# 🔴 [E2] - COOPERADO INATIVO
# ---------------------------------------------------------------

# O ator tenta cadastrar a cobrança para um cooperado inativo.

# O sistema impede o cadastro e informa que a cobrança só pode ser
# cadastrada para cooperado ativo. [RN2]


# 🔴 [E3] - COBRANÇA DUPLICADA
# ---------------------------------------------------------------

# O ator cadastra uma cobrança com mesmo cooperado, nome, valor,
# recorrência e intervalo de uma cobrança ativa.

# O sistema impede o cadastro e informa que já existe uma cobrança
# idêntica. [RN3]


# 🔴 [E4] - TENTATIVA DE TROCAR O COOPERADO
# ---------------------------------------------------------------

# O ator tenta alterar o cooperado na edição (campo bloqueado ou
# requisição direta).

# O sistema rejeita a alteração e mantém o cooperado original. [RN5]


# 🔴 [E5] - EDITAR COBRANÇA CANCELADA
# ---------------------------------------------------------------

# O ator tenta editar uma cobrança com status "Cancelada".

# O sistema bloqueia a edição e informa que a cobrança está cancelada.
# [RN5]


# 🟣 [RN1] VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------
# São obrigatórios: Cooperado, Nome, Categoria, Valor, Recorrência,
# Intervalo e Data de lançamento. O Número de parcelas é obrigatório
# nas parceladas. Descrição e juros são opcionais.
# A taxa de juros, quando informada, deve ser maior que 0% e menor
# que 100%.

# 🟣 [RN2] COOPERADO ATIVO
# ---------------------------------------------------------------
# A cobrança só pode ser cadastrada para cooperado ativo.

# 🟣 [RN3] COBRANÇA IDÊNTICA
# ---------------------------------------------------------------
# O sistema impede cadastro idêntico (mesmo cooperado, nome, valor,
# recorrência e intervalo) a uma cobrança já ativa.

# 🟣 [RN4] GERAÇÃO DE PARCELAS
# ---------------------------------------------------------------
# Nas parceladas, todas as parcelas são geradas no cadastro. A soma
# das parcelas é igual ao valor total e a diferença de centavos fica
# na última parcela. Toda parcela nasce com status "Aberta".

# 🟣 [RN5] REGRAS DE EDIÇÃO
# ---------------------------------------------------------------
# A edição afeta apenas parcelas não pagas. O cooperado não pode ser
# trocado. Cobranças canceladas não podem ser editadas.

# 🟣 [RN6] COBRANÇA ÚNICA
# ---------------------------------------------------------------
# Cobrança única é uma parcelada com 1 parcela e intervalo 0.

# 🟣 [RN7] COBRANÇA RECORRENTE
# ---------------------------------------------------------------
# O valor informado é o de cada ciclo. As parcelas seguintes são
# geradas pela rotina automática.

# 🔵 [DR] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------
# Entrada: cooperado ativo, nome "Mensalidade", valor R$ 1.000,00,
# 3 parcelas, intervalo 30 dias.
# Saída: 3 parcelas "Aberta" (333,33; 333,33; 333,34), soma igual a
# R$ 1.000,00 e mensagem de sucesso.

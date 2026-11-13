'''
UC006 - Criar acordo de negociação para inadimplente

Objetivo: Permitir que o tesoureiro crie e envie uma proposta de
acordo de pagamento a um cooperado inadimplente.

Requisitos:
- RF05004

Ator:
- Tesoureiro

Responsável pela elaboração: Ludmilla Judaico
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de cooperados inadimplentes e seleciona um
# cooperado.

# O ator seleciona a opção "Criar acordo". [E1]

# O sistema exibe a página de acordo com os campos:
# - Cooperado
# - Parcelas em atraso incluídas
# - Valor negociado (R$)
# - Número de parcelas
# - Intervalo (dias)
# - Data do primeiro vencimento
# - Validade da proposta
# - Observações
# - Opções
# -- Botão "Enviar proposta"
# -- Botão "Cancelar"

# O sistema exibe uma sugestão de acordo com base no tempo de
# inadimplência. [RN1]

# O ator mantém a sugestão ou a personaliza (valor, parcelas, intervalo
# e validade). [A1]

# O ator seleciona as parcelas em atraso que serão incluídas.

# O ator seleciona "Enviar proposta". [A2][E2][E3]

# O sistema verifica os dados [RN2]

# O sistema registra a proposta com status "Enviada" e a disponibiliza
# na área de negociações do cooperado.

# O sistema exibe mensagem de sucesso.


# 🟠 [A1] - PERSONALIZAR A PROPOSTA
# ---------------------------------------------------------------

# O ator altera valor, número de parcelas, intervalo ou validade
# sugeridos.

# O sistema recalcula o valor das parcelas do acordo e mantém a soma
# igual ao valor negociado.


# 🟠 [A2] - CANCELAR A CRIAÇÃO
# ---------------------------------------------------------------

# O ator seleciona "Cancelar".

# O sistema descarta os dados.


# 🔴 [E1] - COOPERADO NÃO INADIMPLENTE
# ---------------------------------------------------------------

# O ator tenta criar acordo para cooperado que não é inadimplente.

# O sistema bloqueia a operação e informa que o acordo é exclusivo
# para inadimplentes. [RN3]


# 🔴 [E2] - DADOS INVÁLIDOS
# ---------------------------------------------------------------

# O ator deixa campo obrigatório vazio, informa validade no passado ou
# inclui parcela que não está em atraso.

# O sistema destaca os campos e não envia a proposta. [RN2]


# 🔴 [E3] - JÁ EXISTE PROPOSTA ATIVA PARA AS PARCELAS
# ---------------------------------------------------------------

# Uma das parcelas já está em outra proposta ativa.

# O sistema impede o envio e informa o conflito. [RN4]


# 🟣 [RN1] SUGESTÃO DE ACORDO
# ---------------------------------------------------------------
# O sistema sugere condições com base no tempo de inadimplência. O
# tesoureiro pode personalizá-las antes de enviar.

# 🟣 [RN2] VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------
# Todos os campos são obrigatórios, exceto Observações. A validade
# deve ser uma data futura. Só podem ser incluídas parcelas em atraso.

# 🟣 [RN3] PERFIL E PÚBLICO
# ---------------------------------------------------------------
# Somente o Tesoureiro cria acordos, e apenas para inadimplentes.

# 🟣 [RN4] PARCELA EM UMA ÚNICA PROPOSTA
# ---------------------------------------------------------------
# Uma parcela não pode estar em duas propostas ativas ao mesmo tempo.

# 🔵 [DR] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------
# Entrada: 2 parcelas em atraso (R$ 500,00 cada), valor negociado
# R$ 900,00, 3 parcelas, intervalo 30 dias, validade em 15 dias.
# Saída: proposta "Enviada" visível ao cooperado e parcelas do acordo de
# R$ 300,00.
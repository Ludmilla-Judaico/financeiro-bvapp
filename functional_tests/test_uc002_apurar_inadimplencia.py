'''
UC002 - Apurar inadimplência de cooperados

Objetivo: Recalcular diariamente a condição de inadimplência dos
cooperados e exibi-la no histórico e na listagem de cooperados.

Requisitos:
- RF05003

Ator:
- Sistema (rotina agendada)
- Tesoureiro (consulta o resultado)

Responsável pela elaboração: Ludmilla Judaico
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: o cooperado possui duas mensalidades com parcelas
# atrasadas.

# O sistema executa a rotina diária de apuração.

# O sistema conta, para cada cooperado, as contas em atraso.

# O sistema identifica o cooperado com duas ou mais contas em
# atraso e o marca como inadimplente. [RN1]

# O sistema registra o início do período de inadimplência.

# O ator (tesoureiro) acessa a listagem de cooperados e verifica a
# indicação de inadimplência.

# O ator abre o histórico do cooperado e verifica o período de
# inadimplência registrado.


# 🟠 [A1] - COOPERADO REGULARIZA A SITUAÇÃO
# ---------------------------------------------------------------

# O cooperado tem uma das parcelas validadas como "Paga" e passa a ter
# menos de duas mensalidades em atraso.

# Na próxima execução, o sistema remove a condição de inadimplente e
# encerra o período de inadimplência no histórico.


# 🟠 [A2] - COOPERADO COM APENAS UMA MENSALIDADE EM ATRASO
# ---------------------------------------------------------------

# O sistema identifica uma única mensalidade em atraso.

# O cooperado não é marcado como inadimplente.


# 🟠 [A3] - PARCELAS RENEGOCIADAS
# ---------------------------------------------------------------

# Parcelas marcadas como renegociadas (UC007) não entram na contagem.

# O cooperado deixa de ser inadimplente se restarem menos de duas
# mensalidades em atraso. [RN2]


# 🔴 [E1] - FALHA NA ROTINA
# ---------------------------------------------------------------

# A rotina falha para um cooperado.

# O sistema continua com os demais e alerta o tesoureiro se 
# a rotina não concluir.


# 🟣 [RN1] CRITÉRIO
# ---------------------------------------------------------------
# Inadimplente: duas ou mais mensalidades em atraso. O critério deve
# ser parametrizável pelo tesoureiro.

# 🟣 [RN2] PARCELAS RENEGOCIADAS
# ---------------------------------------------------------------
# Parcelas renegociadas não são contadas em duplicidade.

# 🟣 [RN3] IDEMPOTÊNCIA
# ---------------------------------------------------------------
# A rotina pode ser reexecutada sem gerar duplicidade de períodos.

# 🔵 [DR] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------
# Entrada: cooperado A com 2 mensalidades atrasadas; cooperado B com 1.
# Saída: A marcado como inadimplente com período aberto; B adimplente.
# Após o pagamento de uma parcela de A, A volta a adimplente e o
# período é encerrado.
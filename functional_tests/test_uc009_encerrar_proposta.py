'''
UC009 - Encerrar propostas de acordo vencidas

Objetivo: Encerrar automaticamente as propostas de acordo cuja validade
expirou sem aceite.

Requisitos:
- RF05004

Ator:
- Sistema (rotina agendada)

Responsável pela elaboração: Ludmilla Judaico
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: existe proposta "Enviada" com validade anterior à data
# atual.

# O sistema executa a rotina diária.

# O sistema identifica as propostas "Enviadas" cuja validade expirou.
# [RN1]

# O sistema altera o status das propostas para "Encerrada".

# O sistema mantém as parcelas originais inalteradas, ainda em atraso.

# O cooperado acessa a sua área de negociações e verifica que a
# proposta está "Encerrada" e não pode mais ser aceita.


# 🟠 [A1] - NENHUMA PROPOSTA VENCIDA
# ---------------------------------------------------------------

# O sistema não encontra propostas vencidas.

# A rotina encerra sem erro.


# 🟠 [A2] - PROPOSTA ACEITA OU RECUSADA ANTES DO VENCIMENTO
# ---------------------------------------------------------------

# A proposta já foi aceita ou recusada.

# A rotina a ignora. [RN1]


# 🟠 [A3] - REEXECUÇÃO NO MESMO DIA
# ---------------------------------------------------------------

# A rotina roda novamente.

# Propostas já encerradas não são processadas de novo.


# 🔴 [E1] - FALHA NO ENCERRAMENTO DE UMA PROPOSTA
# ---------------------------------------------------------------

# Ocorre erro ao encerrar uma proposta.

# O sistema registra o erro em log técnico, segue com as demais e
# alerta o administrador se a rotina não concluir.


# 🟣 [RN1] CRITÉRIO DE ENCERRAMENTO
# ---------------------------------------------------------------
# Somente propostas com status "Enviada" e validade expirada são
# encerradas. O prazo de validade é definido na criação do acordo.

# 🟣 [RN2] IDEMPOTÊNCIA
# ---------------------------------------------------------------
# A rotina pode ser reexecutada sem efeitos duplicados.

# 🔵 [DR] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------
# Entrada: 2 propostas "Enviadas" vencidas e 1 dentro da validade.
# Saída: 2 propostas "Encerradas" com registro de auditoria; a
# terceira permanece "Enviada".
'''
UC007 - Responder proposta de acordo

Objetivo: Permitir que o cooperado aceite ou recuse uma proposta de
acordo recebida.

Requisitos:
- RF05004

Ator:
- Cooperado

Responsável pela elaboração: Ludmilla Judaico
'''

# 🟢 [FP] - FLUXO PRINCIPAL (ACEITAR)
# ---------------------------------------------------------------

# O ator acessa a sua área de negociações.

# O sistema exibe as propostas recebidas, com valor negociado, número
# de parcelas, intervalo, primeiro vencimento e validade.

# O ator seleciona uma proposta com status "Enviada" e dentro da
# validade. [E1]

# O ator seleciona "Aceitar". [A1]

# O sistema exibe confirmação e o ator confirma.

# O sistema registra o acordo como uma nova cobrança parcelada no
# perfil do cooperado. [RN1]

# O sistema marca as parcelas originais incluídas como "renegociadas",
# para não serem contadas em duplicidade. [RN2]

# O sistema atualiza a proposta para "Aceita" e registra no log de
# auditoria o usuário, a data e a hora.

# O ator verifica a nova cobrança em seu histórico financeiro (UC005).


# 🟠 [A1] - RECUSAR PROPOSTA
# ---------------------------------------------------------------

# O ator seleciona "Recusar" e confirma.

# O sistema atualiza a proposta para "Recusada", mantém as parcelas
# originais inalteradas e registra a recusa no log de auditoria.


# 🟠 [A2] - VISUALIZAR PROPOSTAS ENCERRADAS
# ---------------------------------------------------------------

# O ator filtra as propostas por status (Aceita, Recusada, Encerrada).

# O sistema exibe o histórico de propostas, somente leitura.


# 🔴 [E1] - PROPOSTA VENCIDA
# ---------------------------------------------------------------

# O ator tenta aceitar uma proposta fora da validade.

# O sistema bloqueia a ação e informa que a proposta foi encerrada.
# [RN3]


# 🔴 [E2] - ACESSO A PROPOSTA DE OUTRO COOPERADO
# ---------------------------------------------------------------

# O ator tenta acessar proposta de outro cooperado.

# O sistema nega o acesso (validação no backend).


# 🟣 [RN1] COBRANÇA DO ACORDO
# ---------------------------------------------------------------
# O aceite gera uma cobrança parcelada com os dados da proposta; a
# soma das parcelas é igual ao valor negociado.

# 🟣 [RN2] PARCELAS RENEGOCIADAS
# ---------------------------------------------------------------
# As parcelas originais passam a ser tratadas como renegociadas e
# deixam de contar como atraso.

# 🟣 [RN3] VALIDADE
# ---------------------------------------------------------------
# A proposta só pode ser aceita ou recusada dentro da validade.

# 🔵 [DR] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------
# Entrada: proposta "Enviada" de R$ 900,00 em 3 parcelas.
# Saída (aceite): proposta "Aceita", nova cobrança com 3 parcelas
# "Aberta" de R$ 300,00, parcelas originais "renegociadas" e registro
# de auditoria. Saída (recusa): proposta "Recusada", nada mais muda.
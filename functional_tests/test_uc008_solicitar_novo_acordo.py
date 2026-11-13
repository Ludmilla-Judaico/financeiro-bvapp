'''
UC009 - Solicitar nova negociação

Objetivo: Permitir que o cooperado solicite uma nova negociação ao
tesoureiro, limitada a uma solicitação ativa por cooperado.

Requisitos:
- RF05004

Ator:
- Cooperado
- Tesoureiro

Responsável pela elaboração: Ludmilla Judaico
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator (cooperado) acessa a sua área de negociações.

# O ator seleciona "Solicitar nova negociação". [E1][E2]

# O sistema abre uma solicitação para o tesoureiro com status
# "Ativa". [RN1]

# O sistema exibe mensagem de sucesso.

# O tesoureiro acessa a lista de solicitações e verifica a
# solicitação do cooperado. [A1]


# 🟠 [A1] - TESOUREIRO ATENDE A SOLICITAÇÃO
# ---------------------------------------------------------------

# O tesoureiro cria o acordo conforme o UC006 - A3.

# O sistema encerra a solicitação como "Atendida".


# 🟠 [A2] - TESOUREIRO RECUSA A SOLICITAÇÃO
# ---------------------------------------------------------------

# O tesoureiro seleciona "Recusar solicitação".

# O sistema encerra a solicitação, registra o evento no log e libera o
# cooperado para abrir nova solicitação.


# 🔴 [E1] - JÁ EXISTE SOLICITAÇÃO ATIVA
# ---------------------------------------------------------------

# O ator tenta abrir uma solicitação tendo outra ativa.

# O sistema impede a abertura e informa que já há uma solicitação em
# andamento. [RN1]


# 🔴 [E2] - COOPERADO NÃO INADIMPLENTE
# ---------------------------------------------------------------

# O ator não é inadimplente.

# O sistema não disponibiliza a opção de solicitar negociação. [RN2]


# 🟣 [RN1] UMA SOLICITAÇÃO ATIVA
# ---------------------------------------------------------------
# Não é permitido ter mais de uma solicitação ativa por cooperado.

# 🟣 [RN2] ELEGIBILIDADE
# ---------------------------------------------------------------
# A solicitação é destinada a cooperados inadimplentes (regra sugerida
# a validar).

# 🔵 [DR] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------
# Entrada: cooperado inadimplente sem solicitação ativa.
# Saída: solicitação "Ativa" visível ao tesoureiro e registro de
# auditoria. Segunda tentativa: bloqueada com mensagem.
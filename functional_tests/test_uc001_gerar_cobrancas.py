'''
UC001 - Gerar automaticamente parcelas de cobranças recorrentes

Objetivo: Gerar, por rotina diária, as parcelas das cobranças
recorrentes ativas na data de geração, sem duplicidade.

Requisitos:
- RF05001
- RF05002

Ator:
- Sistema (rotina agendada)
- Tesoureiro (consulta o resultado)

Responsável pela elaboração: Ludmilla Judaico
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Pré-condição: existe uma cobrança recorrente ativa cuja data de
# geração é o dia atual e o cooperado está ativo.

# Às 00:00, o sistema inicia a rotina de geração.

# O sistema identifica as cobranças recorrentes ativas que estão na
# data de geração. [RN1]

# Para cada cobrança, o sistema consulta a situação do cooperado e
# verifica que ele está ativo. [A2][E1]

# O sistema verifica que ainda não existe parcela gerada para o ciclo.
# [RN3] [A3]

# O sistema cria a nova parcela com os últimos dados registrados da
# cobrança, com status "Aberta". [RN2]

# O ator (tesoureiro) acessa o detalhe da cobrança e verifica a nova
# parcela com status "Aberta".


# 🟠 [A1] - NENHUMA COBRANÇA NO DIA
# ---------------------------------------------------------------

# O sistema não encontra cobranças na data de geração.

# A rotina encerra sem erro e sem gerar parcelas.


# 🟠 [A2] - COOPERADO INATIVO
# ---------------------------------------------------------------

# O sistema identifica que o cooperado está inativo.

# O sistema não gera a parcela.

# A rotina continua com as demais cobranças.


# 🟠 [A3] - REEXECUÇÃO NO MESMO DIA (IDEMPOTÊNCIA)
# ---------------------------------------------------------------

# A rotina é executada uma segunda vez no mesmo dia (automática ou
# manual).

# O sistema detecta que as parcelas do ciclo já existem e não gera
# duplicidade.


# 🟠 [A4] - ALTERAÇÃO DA COBRANÇA ANTES DO CICLO
# ---------------------------------------------------------------

# O ator edita o valor da cobrança recorrente (UC003 - A3).

# Na próxima geração, o sistema usa os últimos dados registrados, e a
# nova parcela nasce com o novo valor. As parcelas anteriores não
# mudam.


# 🔴 [E1] - FALHA NA CONSULTA DA SITUAÇÃO DO COOPERADO
# ---------------------------------------------------------------

# A consulta à situação do cooperado falha.

# O sistema não gera a parcela.
# A rotina continua com as demais cobranças e, se não concluir, é
# disparado alerta ao tesoureiro. [RN4]


# 🟣 [RN1] DATA DE GERAÇÃO
# ---------------------------------------------------------------
# A rotina roda diariamente às 00:00 (fuso de Brasília) e considera
# apenas cobranças recorrentes ativas na data de geração definida no
# cadastro.

# 🟣 [RN2] DADOS DA PARCELA
# ---------------------------------------------------------------
# A parcela é criada com os últimos dados registrados da cobrança e
# status "Aberta".

# 🟣 [RN3] IDEMPOTÊNCIA
# ---------------------------------------------------------------
# Executar a rotina duas vezes no mesmo dia não pode duplicar parcelas.

# 🟣 [RN4] TOLERÂNCIA A FALHAS
# ---------------------------------------------------------------
# Falhas em um registro não interrompem os demais.

# 🔵 [DR] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------
# Entrada: 3 cobranças recorrentes na data de geração (2 com
# cooperados ativos, 1 com cooperado inativo).
# Saída: 2 parcelas "Aberta" geradas, 2 registros de auditoria com usuário "Sistema". 
# Segunda execução no mesmo dia: 0 parcelas novas.
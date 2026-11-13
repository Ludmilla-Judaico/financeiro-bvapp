'''
UC004 - Consultar histórico financeiro de cooperados

Objetivo: Permitir que o tesoureiro consulte o histórico financeiro de
qualquer cooperado, com filtros, ordenação e exportação.

Requisitos:
- RF05003

Ator:
- Tesoureiro

Responsável pela elaboração: Ludmilla Judaico
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de cooperados e seleciona um cooperado.

# O sistema exibe o histórico financeiro do cooperado, paginado, com:
# - Períodos de inadimplência
# - Situação (ativo, inativo)
# - Pagamentos efetuados
# - Acordos firmados
# - Tempo de associação
# - Demais cobranças do cooperado
# [RN1]

# O ator verifica que os registros removidos não aparecem. [RN2]

# O ator verifica a indicação de situação (adimplente ou inadimplente).
# [RN3]


# 🟠 [A1] - FILTRAR O HISTÓRICO
# ---------------------------------------------------------------

# O ator utiliza os filtros: nome, status, recorrência, valor mínimo e
# máximo, período de lançamento, ativas/inativas, intervalo e ano.

# O sistema atualiza a listagem respeitando os filtros.


# 🟠 [A2] - ORDENAR O HISTÓRICO
# ---------------------------------------------------------------

# O ator seleciona o cabeçalho de uma coluna (ou "proximidade do
# vencimento") e define ordem crescente ou decrescente.

# O sistema reordena a listagem.


# 🟠 [A3] - EXPORTAR O HISTÓRICO
# ---------------------------------------------------------------

# O ator aplica filtros e seleciona "Exportar" em PDF ou CSV.

# O sistema gera o arquivo respeitando os filtros aplicados e exibe
# feedback ao término. [RN4]


# 🟠 [A4] - HISTÓRICO SEM REGISTROS
# ---------------------------------------------------------------

# O cooperado não possui registros para os filtros aplicados.

# O sistema exibe mensagem informativa.


# 🔴 [E1] - USUÁRIO SEM PERMISSÃO
# ---------------------------------------------------------------

# Um usuário sem perfil de Tesoureiro ou Administrador tenta acessar
# o histórico de outro cooperado.

# O sistema nega o acesso (validação no backend). [RN5]


# 🟣 [RN1] CONTEÚDO DO HISTÓRICO
# ---------------------------------------------------------------
# Períodos de inadimplência, situação, pagamentos, acordos, tempo de associação
# e demais cobranças.

# 🟣 [RN2] REGISTROS REMOVIDOS
# ---------------------------------------------------------------
# A listagem oculta registros removidos.

# 🟣 [RN3] INADIMPLÊNCIA
# ---------------------------------------------------------------
# Cooperado inadimplente é o que possui duas ou mais mensalidades em
# atraso (UC002).

# 🟣 [RN4] EXPORTAÇÃO
# ---------------------------------------------------------------
# PDF e CSV respeitam os filtros e são processados sem bloquear a
# interface.

# 🟣 [RN5] PERMISSÕES
# ---------------------------------------------------------------
# Tesoureiro e Administrador acessam o histórico de qualquer
# cooperado.

# 🔵 [DR] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------
# Entrada: cooperado com 12 cobranças, 2 em atraso, 1 acordo; filtro
# "Atrasada".
# Saída: lista paginada com as 2 parcelas em atraso, indicação
# "inadimplente" e arquivo exportado com os mesmos registros.
'''
UC005 - Consultar o próprio histórico financeiro

Objetivo: Permitir que o cooperado consulte somente o seu histórico
financeiro, a partir do seu painel.

Requisitos:
- RF05003

Ator:
- Cooperado

Responsável pela elaboração: Ludmilla Judaico
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa o seu painel e seleciona "Meu histórico financeiro".

# O sistema exibe somente os dados vinculados ao cadastro do ator:
# períodos de inadimplência, pagamentos efetuados, acordos firmados,
# tempo de associação e demais cobranças. [RN1]

# O ator verifica que os registros removidos não aparecem.

# O ator verifica a sua situação (adimplente ou inadimplente).


# 🟠 [A1] - FILTRAR E ORDENAR
# ---------------------------------------------------------------

# O ator aplica filtros (status, período, valor, ano etc.) e ordena
# por qualquer campo exibido.

# O sistema atualiza a listagem paginada.


# 🟠 [A2] - EXPORTAR O PRÓPRIO HISTÓRICO
# ---------------------------------------------------------------

# O ator seleciona "Exportar" em PDF ou CSV.

# O sistema gera o arquivo com os dados do ator, respeitando os
# filtros.


# 🔴 [E1] - TENTATIVA DE ACESSAR DADOS DE OUTRO COOPERADO
# ---------------------------------------------------------------

# O ator altera o identificador na URL ou na requisição para acessar
# o histórico de outro cooperado.

# O sistema nega o acesso, sem exibir dado algum. [RN1]


# 🟣 [RN1] ACESSO RESTRITO
# ---------------------------------------------------------------
# O cooperado só visualiza dados do seu próprio cadastro. A regra é
# validada no backend e os dados são tratados conforme a LGPD.

# 🔵 [DR] DADOS E RESULTADOS ESPERADOS
# ---------------------------------------------------------------
# Entrada: cooperado autenticado.
# Saída: apenas as cobranças, pagamentos e acordos do próprio
# cooperado. Acesso a outro cooperado retorna negação.
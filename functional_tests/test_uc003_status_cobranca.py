# UC003 - Informar o status de uma cobrança

# Objetivo:
# Apresentar o status correspondente a uma cobrança, permitindo
# identificar sua situação.

# Requisitos relacionados:
# CA 23946 - O sistema deve informar o status da cobrança.

# Ator:
# Sistema

# Fluxo principal:
# 1. Todo dia, o sistema checa as cobranças cadastradas.
# 2. O sistema verifica as informações necessárias para determinar sua situação.
# 3. O sistema associa o status correspondente à cobrança.
# 4. O sistema disponibiliza o status para consulta.

# Fluxos alternativos:
# A1 - Cobrança a pagar:
# Caso a cobrança esteja pendente e dentro do prazo de pagamento,
# o sistema informa o status "A pagar".
#
# A2 - Cobrança paga:
# Caso a cobrança tenha sido quitada, o sistema informa o status "Paga".
#
# A3 - Cobrança atrasada:
# Caso a cobrança esteja vencida e não tenha sido paga,
# o sistema informa o status "Atrasada".
#

# Regras de negócio:
# RN1 - Os status previstos para as cobranças são:
# A pagar, Paga e Atrasada.
# RN2 - Os critérios de transição entre os status devem ser respeitados.
# RN3 - Cobranças sempre recebem status "A pagar" no momento em que são criadas
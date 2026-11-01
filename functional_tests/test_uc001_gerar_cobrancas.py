# UC001 - Gerar cobranças automaticamente

# Objetivo:
# Descrever o processo de geração automática de cobranças relacionadas
# aos cooperados da cooperativa.

# Requisitos relacionados:
# CA 23941 - O sistema deve gerar automaticamente cobranças relacionadas
# aos associados da cooperativa.
# US 25549 - US - Geração automática de cobrança.

# Ator:
# Sistema

# Fluxo principal:
# 1. O sistema inicia o processo de geração automática de cobranças.
# 2. O sistema identifica os cooperados que possuem cobranças a serem geradas.
# 3. O sistema verifica os tipos de cobranças aplicáveis:
#    - Mensais recorrentes;
#    - Contas parceladas ativas;
#    - Acordos ativos.
# 4. O sistema verifica as condições necessárias para gerar cada cobrança.
# 5. O sistema gera as cobranças correspondentes.
# 6. O sistema registra as cobranças geradas.

# Fluxos alternativos:
# A1 - Cooperado sem cobranças pendentes:
# Caso não existam cobranças a serem geradas para determinado cooperado,
# o sistema não gera novas cobranças para ele.
#
# A2 - Nenhum cooperado elegível:
# Caso nenhum cooperado atenda às condições de geração,
# o processo é encerrado sem gerar cobranças.

# Regras de negócio:
# RN1 - O sistema deve contemplar cobranças mensais recorrentes,
# contas parceladas ativas e acordos ativos.
# RN2 - As condições específicas de geração de cada tipo de cobrança
# devem ser respeitadas.
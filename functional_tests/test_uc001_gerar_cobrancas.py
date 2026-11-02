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
# 1. Diariamente, o sistema inicia o processo de geração automática
# 2. O sistema identifica os cooperados elegíveis.
# 3. O sistema identifica as cobranças recorrentes que estão na data de serem geradas.
# 4. O sistema checa se a cobrança está ativa.
# 5. O sistema verifica se as cobranças já foram geradas.
# 6. O sistema registra as novas cobranças.

# Fluxos alternativos:
# A1 - Cooperado sem cobranças pendentes:
# Caso não existam cobranças a serem geradas para determinado cooperado,
# o sistema não gera novas cobranças para ele.
#
# A2 - Nenhum cooperado elegível:
# Caso nenhum cooperado atenda às condições de geração,
# o processo é encerrado sem gerar cobranças.

# Regras de negócio:
# RN1 - O sistema deve contemplar cobranças mensais recorrentes e
# contas parceladas ativas.
# RN2 - Cobranças recorrentes são geradas na frequência definida no momento do cadastro
# RN3 - Parcelas de cobranças parceladas são criadas imediatamente após o cadastro da cobrança
# RN4 -  A soma de cada parcela de uma cobrança parcelada deve ser o total da cobrança definido no momento do cadastro
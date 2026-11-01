# UC002 - Verificar situação do cooperado antes da geração de cobrança

# Objetivo:
# Garantir que novas cobranças sejam geradas somente para cooperados
# que permaneçam ativos na cooperativa.

# Requisitos relacionados:
# CA 25545 - O sistema deve sempre verificar se cooperado continua ativo
# antes de realizar uma nova cobrança.
# CA 23941 - O sistema deve gerar automaticamente cobranças relacionadas
# aos associados da cooperativa.

# Ator:
# Sistema

# Fluxo principal:
# 1. O sistema identifica um cooperado que possui uma cobrança a ser gerada.
# 2. O sistema consulta a situação cadastral do cooperado.
# 3. O sistema verifica se o cooperado está ativo.
# 4. Caso esteja ativo, o sistema prossegue com a geração da cobrança.
# 5. O sistema registra a nova cobrança.

# Fluxos alternativos:
# A1 - Cooperado inativo:
# Caso o cooperado esteja inativo, o sistema não gera a cobrança.
#
# A2 - Falha na consulta:
# Caso o sistema não consiga consultar a situação do cooperado,
# a geração da cobrança não deve prosseguir até que a situação
# possa ser verificada.

# Regras de negócio:
# RN1 - A situação do cooperado deve ser verificada antes de cada
# nova cobrança.
# RN2 - Cooperados inativos não devem receber novas cobranças.
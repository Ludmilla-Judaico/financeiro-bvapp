# UC004 - Exibir indicadores gerais de Contas e Cobranças

# Objetivo:
# Apresentar indicadores gerais de contas e cobranças na listagem
# unificada do módulo.

# Requisitos relacionados:
# Feature 28813 - Dashboard de indicadores gerais de Contas e Cobranças.
# US 28814 - Exibir indicadores gerais de Contas e Cobranças
# na listagem unificada.

# Ator:
# Funcionário da cooperativa

# Fluxo principal:
# 1. O funcionário acessa o módulo Contas e Cobranças.
# 2. O sistema apresenta a listagem unificada.
# 3. O sistema recupera as informações necessárias para compor
#    os indicadores gerais.
# 4. O sistema apresenta os indicadores na listagem unificada.
# 5. O funcionário visualiza os indicadores apresentados.

# Fluxos alternativos:
# A1 - Ausência de registros:
# Caso não existam contas ou cobranças para compor os indicadores,
# o sistema apresenta uma indicação de ausência de dados.
#
# A2 - Falha ao carregar os indicadores:
# Caso ocorra uma falha na obtenção dos dados, o sistema informa
# que não foi possível carregar os indicadores.

# Regras de negócio:
# RN1 - Os indicadores devem estar relacionados às contas e cobranças
# exibidas na listagem unificada.
# RN2 - Os indicadores e seus critérios de cálculo devem seguir
# as definições do módulo.
# RN3 - Apenas funcionários com permissão de tesoureiro ou administrador
# devem poder visualizar todas as contas e cobranças
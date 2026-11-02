# UC005 - Consultar balanço de contas

# Objetivo:
# Permitir que o funcionário visualize o balanço de contas
# disponibilizado pelo sistema.

# Requisitos relacionados:
# Feature 28813 - Dashboard de indicadores gerais de Contas e Cobranças.
# US 29527 - Balanço de contas.

# Ator:
# Funcionário da cooperativa

# Fluxo principal:
# 1. O funcionário acessa o módulo Contas e Cobranças.
# 2. O sistema recupera a soma dos valores das cobranças pagas (entrada)
# 3. O sistema recupera a soma dos valores das contas pagas (saída)
# 4. O sistema apresenta o balanço de valores ao funcionário
# em forma de Dashboard.

# Fluxos alternativos:
# A1 - Ausência de informações:
# Caso não existam dados para compor o balanço, o sistema apresenta
# uma indicação de ausência de informações.
#
# A2 - Falha ao carregar o balanço:
# Caso ocorra uma falha na recuperação dos dados, o sistema informa
# que não foi possível apresentar o balanço.

# Regras de negócio:
# RN1 - O balanço deve ser composto por informações referentes às contas/cobranças PAGAS.
# RN2 - A soma das cobranças (pertence aos cooperados) pagas representa
# o valor recebido pela cooperativa no período definido
# RN3 - A soma das contas (pertence à cooperativa) pagas representa
# o valor gasto pela cooperativa no período definido
# UC006 - Visualizar histórico de uma conta

# Objetivo:
# Permitir que o funcionário consulte o histórico de uma conta
# cadastrada no sistema.

# Requisitos relacionados:
# Feature 29703 - Histórico de Contas e Cobranças.
# US 29704 - Implementar histórico de Contas e Cobranças.
# US 29705 - Visualização do histórico de Contas e Cobranças.
# Tarefa 29711 - Adicionar aba de histórico no popup de detalhamento
# de conta.

# Ator:
# Funcionário da cooperativa

# Fluxo principal:
# 1. O funcionário acessa a listagem de contas.
# 2. O funcionário seleciona uma conta.
# 3. O sistema apresenta os detalhes da conta selecionada.
# 4. O funcionário acessa a aba de histórico.
# 5. O sistema recupera os registros de histórico relacionados à conta.
# 6. O sistema apresenta o histórico ao funcionário.

# Fluxos alternativos:
# A1 - Conta sem histórico:
# Caso não existam registros de histórico para a conta selecionada,
# o sistema informa que não há registros disponíveis.
#
# A2 - Falha ao carregar o histórico:
# Caso ocorra uma falha na recuperação dos registros, o sistema informa
# que não foi possível carregar o histórico.

# Regras de negócio:
# RN1 - O histórico apresentado deve corresponder à conta selecionada.
# RN2 - Os registros devem apresentar informações relacionadas
# aos eventos ocorridos na conta.
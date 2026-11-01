# UC008 - Registrar eventos no histórico de contas e cobranças

# Objetivo:
# Registrar os eventos relacionados às contas e cobranças
# para permitir o acompanhamento de seu histórico.

# Requisitos relacionados:
# Feature 29703 - Histórico de Contas e Cobranças.
# US 29704 - Implementar histórico de Contas e Cobranças.

# Ator:
# Sistema

# Fluxo principal:
# 1. O sistema identifica a ocorrência de um evento relacionado
#    a uma conta ou cobrança.
# 2. O sistema identifica o registro ao qual o evento está associado.
# 3. O sistema registra as informações do evento no histórico.
# 4. O sistema disponibiliza o registro para consultas posteriores.

# Fluxos alternativos:
# A1 - Registro não identificado:
# Caso não seja possível identificar a conta ou cobrança relacionada,
# o sistema não deve associar o evento a um registro incorreto.
#
# A2 - Falha ao registrar o evento:
# Caso ocorra uma falha no registro, o sistema informa
# que não foi possível registrar o evento.

# Regras de negócio:
# RN1 - Os eventos registrados devem estar associados
# à conta ou cobrança correspondente.
# RN2 - Os tipos de eventos e as informações armazenadas
# devem seguir as definições do histórico.
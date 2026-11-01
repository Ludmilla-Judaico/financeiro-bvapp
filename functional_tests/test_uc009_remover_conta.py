# UC009 - Remover uma conta

# Objetivo:
# Permitir que o funcionário solicite a remoção de uma conta
# cadastrada no sistema.

# Requisitos relacionados:
# Feature 25929 - Remoção de Contas/Cobranças.
# US 25930 - Deletar conta/cobrança.
# US 27022 - Deleção visual de conta/cobrança.

# Ator:
# Funcionário da cooperativa

# Fluxo principal:
# 1. O funcionário acessa a listagem de contas.
# 2. O funcionário seleciona a conta que deseja remover.
# 3. O sistema apresenta os detalhes da conta selecionada.
# 4. O funcionário solicita a remoção.
# 5. O sistema solicita a confirmação da operação.
# 6. O funcionário confirma a solicitação.
# 7. O sistema realiza a operação de remoção.
# 8. O sistema atualiza a listagem.
# 9. O sistema informa que a operação foi concluída.

# Fluxos alternativos:
# A1 - Cancelamento da remoção:
# Caso o funcionário cancele a operação, a conta permanece
# disponível no sistema.
#
# A2 - Falha na remoção:
# Caso ocorra uma falha durante a operação, o sistema informa
# que não foi possível remover a conta.

# Regras de negócio:
# RN1 - A remoção deve respeitar as condições definidas
# para contas.
# RN2 - Deve ser definido se a remoção é definitiva
# ou apenas visual.
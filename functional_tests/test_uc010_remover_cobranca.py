# UC009 - Remover uma cobrança

# Objetivo:
# Permitir que o funcionário solicite a remoção de uma cobrança
# cadastrada no sistema.

# Requisitos relacionados:
# Feature 25929 - Remoção de contas/Cobranças.
# US 25930 - Deletar conta/cobrança.
# US 27022 - Deleção visual de cobrança/cobrança.

# Ator:
# Funcionário da cooperativa

# Fluxo principal:
# 1. O funcionário acessa a listagem de cobranças.
# 2. O funcionário seleciona a cobrança que deseja remover.
# 3. O sistema apresenta os detalhes da cobrança selecionada.
# 4. O funcionário solicita a remoção.
# 5. O sistema solicita a confirmação da operação.
# 6. O funcionário confirma a solicitação.
# 7. O sistema realiza a operação de remoção.
# 8. O sistema atualiza a listagem.
# 9. O sistema informa que a operação foi concluída.

# Fluxos alternativos:
# A1 - Cancelamento da remoção:
# Caso o funcionário cancele a operação, a cobrança permanece
# disponível no sistema.
#
# A2 - Falha na remoção:
# Caso ocorra uma falha durante a operação, o sistema informa
# que não foi possível remover a cobrança.

# Regras de negócio:
# # RN1 - Apenas cobranças com status "A pagar" ou "Atrasada" podem ser deletadas.
# RN2 - A cobrança não deve ser permanentemente excluída do banco de dados. Apenas o atributo "excluida" passa a ser true
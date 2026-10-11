<<<<<<< HEAD
from src.Engine.Phase import Phase
from src.Character.Character import Character

from src.utils.inputs import wait_user
from src.utils.terminal import clear_terminal
from src.utils.time import delay

class Phase3(Phase):
    def __init__(self):
        pass

    def run(self, player: Character):
        clear_terminal()
        
        print("Fase 3 rodando")
        print(player)
        print('')

=======
from src.Engine.Phase import Phase
from src.Character.Character import Character
from src.utils.inputs import wait_user

class Phase3(Phase):
    def __init__(self):
        pass

    def run(self, player: Character):
        print("Fase 3 rodando")
        print(player)
        print('')

>>>>>>> 1423d12 (Atualizando projeto com mudnaças feitas em camaragibe)
        wait_user()
<<<<<<< HEAD
from src.Character.Character import Character
from src.Character.Role.Warrior import Warrior

from src.Engine.Phase import Phase

from src.Phases.Phase1 import Phase1
from src.Phases.Phase2 import Phase2
from src.Phases.Phase3 import Phase3

from src.utils.time import delay


class Engine():

    def __init__(self):
        self.phases: list[Phase] = []

        self.phases.append(Phase1())
        self.phases.append(Phase2())
        self.phases.append(Phase3())

        character_name = input("Escolha o nome do seu personagem:\n")
        player_class = Warrior()
        player: Character = Character(player_class, character_name)
        player.playable = True

        delay()

        self.run(player)
        
    def run(self, player: Character):
        for phase in self.phases:
            phase.run(player)
            
            if player.is_dead():
                print("GAME OVER")
=======
from src.Character.Character import Character

from src.Character.Role import Role
from src.Character.Role.Warrior import Warrior
from src.Character.Role.Assassin import Assassin
from src.Character.Role.Mage import Mage

from src.Engine.Phase import Phase
from src.Phases.Phase1 import Phase1
from src.Phases.Phase2 import Phase2
from src.Phases.Phase3 import Phase3

from src.utils.inputs import input_option


class Engine():

    def __init__(self):
        self.phases: list[Phase] = []

        self.phases.append(Phase1())
        self.phases.append(Phase2())
        self.phases.append(Phase3())

        character_name = input("Escolha o nome do seu personagem:\n")
        player_class = self.choose_class()
        player: Character = Character(player_class, character_name)

        self.run(player)

    def choose_class(self)->Role:
        role_list: list = [
            Warrior(),
            Mage(),
            Assassin()
        ]

        role_index = input_option(role_list, "Escolha sua classe:")
        return role_list[role_index]

        
    def run(self, player: Character):
        for phase in self.phases:
            phase.run(player)
            
            if player.is_dead():
                print("GAME OVER")
>>>>>>> 1423d12 (Atualizando projeto com mudnaças feitas em camaragibe)
                break
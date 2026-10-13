from src.Character.Character import Character
from src.Character.Role.Warrior import Warrior

from src.Engine.Phase import Phase

from src.Phases.Phase1 import Phase1
from src.Phases.Phase2 import Phase2
from src.Phases.Phase3 import Phase3

from src.utils.time import delay
from src.utils.terminal import clear_terminal
from src.utils.inputs import input_option


class Engine():

    def __init__(self):
        self.phases: list[Phase] = []
        self.load_phases()
        self.run_start_menu()
        
    def run_game(self, player: Character):
        for phase in self.phases:
            phase.run(player)
            
            if player.is_dead():
                print("GAME OVER")
                delay(2000)
                clear_terminal()
                break

    def run_start_menu(self):
        while True:
            clear_terminal()
            print("PYTHON RPG")
            option:int = input_option(["New Game", "Load Game", "Settings", "Exit"], "")

            match option:
                case 0:
                    player:Character = self.generate_player()
                    self.run_game(player)

                case 1:
                    player:Character = self.generate_player()
                    self.load_save(player)
                    self.run_game(player)

                case 2:
                    self.settings()

                case 3:
                    print("Exiting...")
                    delay(500)
                    clear_terminal()
                    break


    def load_phases(self)->None:
        self.phases.append(Phase1())
        self.phases.append(Phase2())
        self.phases.append(Phase3())

    def load_save(self, playable_character:Character)->None:
        pass

    def settings(self)->None:
        pass

    def generate_player(self)->Character:
        clear_terminal()
        
        character_name = input("Escolha o nome do seu personagem:\n")
        player_class = Warrior()
        player: Character = Character(player_class, character_name)
        player.playable = True

        return player

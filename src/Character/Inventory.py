from src.Items.Item import Item

INVENTORY_MAX_SIZE = 10

class Inventory():

    def __init__(self):
        self._spaces: list = []

    def store_item(self, item:Item)->None:
        if self.have_enough_space():
            self._spaces.append(item)

        print("Não há espaço suficiente no inventário")

    def remove_item(self, item_index:str)->None:
        item_removed:Item = self._spaces[item_index].pop()
        print(f"{item_removed.name} foi removido do inventário")

    def have_enough_space(self)->True:
        for i in range(INVENTORY_MAX_SIZE):
            if self._spaces[i] == None:
                return True
            
        return False
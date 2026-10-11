import os

<<<<<<< HEAD
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def set_color_white():
    return "\033[30m"

def set_color_red():
    return "\033[31m"

def set_color_yellow():
    return "\033[33m"

def set_color_green():
    return "\033[32m"

def set_color_blue():
    return "\033[34m"

def print_square():
    return "\u25A0"

def print_empty_square():
    return "\u25A1"
=======
# Limpa a tela no Windows ('cls') ou Linux/Mac ('clear')
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == "__main__":
    print("ababa")
    input()

    clear_terminal()
    input()
>>>>>>> 1423d12 (Atualizando projeto com mudnaças feitas em camaragibe)


from game import Game

def get_user_menu_choice():
    menu = ['play a new game','show score','quit']
    
    menu_action = input(f'enter N for-{menu[0]} ,P for -{menu[1]},Q for-{menu[2]}\n').upper()
    return menu_action


    # if menu_action == menu[0]:
    #     result = Game().play()
    #     return result


def main():
    results = {'win': 0,'loss': 0,'draw': 0}
    choice = get_user_menu_choice()

    while choice !=  'Q':

        if choice == 'N':
            result = Game().play()
            if result == 'win':
                results['win'] += 1
            if result == 'lose':
                results['loss'] += 1
            if result == 'draw':
                results['draw'] += 1
        if choice == 'P':
            print_results(results)
        choice = get_user_menu_choice()

def print_results(results):
    print(results)
main()
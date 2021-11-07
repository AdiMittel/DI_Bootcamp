import random
class Game:
    def get_user_item(self):
        '''Ask the user to select an item (rock/paper/scissors).'''
        while True:
            user_item = input('Choose (r)ock , (p)aper, (s)cissors\n')
            if user_item.upper() in 'RPS' :
                return user_item

    def get_computer_item(self):
        items = ['r','p','s']
        comp_item = random.choice(items)
        print(f'computer chose {comp_item}')
        return comp_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'Draw'
        elif user_item == 's':
            if computer_item == 'r':
                return 'Lose'
            else:
                return 'Win'
        elif user_item == 'r':
            if computer_item == 'p':
                'Lose'
            else:
                'Win'
        elif user_item == 'p':
            if computer_item == 's':
                return 'Lose'
            else:
                return 'Win'
        
    def play(self):
        user_action = self.get_user_item()
        comp_action = self.get_computer_item()
        if game.get_game_result(user_action,comp_action) == 'Win':
            print(f'You chose {user_action} and computer has {comp_action},you won!')
            return 'win'
        elif game.get_game_result(user_action,comp_action) == 'Lose':
            print(f'You chose {user_action} and computer has {comp_action},you lost!')
            return 'lose'
        elif game.get_game_result(user_action,comp_action) == 'Draw':
            print(f'You and the computer chose {user_action}, it\'s a draw!')
            return 'draw'

    

game = Game()
game.play()
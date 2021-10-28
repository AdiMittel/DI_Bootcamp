board_slots = {
    '1':' ',
    '2':' ',
    '3':' ',
    '4':' ',
    '5':' ',
    '6':' ',
    '7':' ',
    '8':' ',
    '9':' '
}

def build_board(board):
    print('*'*13)
    print('*' + ' ' + board_slots['1'] + (' |' + ' ') + board_slots['2'] + (' |' + ' ')  + board_slots['3'] + ' ' + '*')
    print('-'*13)
    print('*' + ' ' + board_slots['4'] + (' |' + ' ') + board_slots['5'] + (' |' + ' ')  + board_slots['6'] + ' ' + '*')
    print('-'*13)
    print('*' + ' ' + board_slots['7'] + (' |' + ' ') + board_slots['8'] + (' |' + ' ')  + board_slots['9'] + ' ' + '*')
    print('-'*13)
build_board(board_slots)

def play_game():
    turn = 'X'
    count = 0
    for i in range(10):
        build_board(board_slots)
        print(f'It\'s {turn} turn to play: ')
        move = input('Where would you like to mark?(1-9) ')
        if board_slots[move] == ' ':
            board_slots[move] = turn
            count += 1
        else:
            print(f'Your move {move} has already been selected. Chose another spot')
            continue
        if count >= 5:
            if board_slots['1'] == board_slots['2'] == board_slots['3'] != '': #top line
                build_board(board_slots)
                print('\n Game over..\n')
                print(f'{turn} won!! Best row to win!')
                break
            elif board_slots['4'] == board_slots['5'] == board_slots['6']  != '': #middle line
                build_board(board_slots)
                print('\n Game over..\n')
                print(f'{turn} is the WINNER!')
                break
            elif board_slots['7'] == board_slots['8'] == board_slots['9']  != '': #last line
                build_board(board_slots)
                print('\n Game over..\n')
                print(f'{turn} is the WINNER!')
                break
            elif board_slots['1'] == board_slots['4'] == board_slots['7']  != '': #left column
                build_board(board_slots)
                print('\n Game over..\n')
                print(f'{turn} is the WINNER!')
                break
            elif board_slots['2'] == board_slots['5'] == board_slots['8']  != '': #middle column
                build_board(board_slots)
                print('\n Game over..\n')
                print(f'{turn} is the WINNER!')
                break
            elif board_slots['3'] == board_slots['6'] == board_slots['9']  != '': #right column
                build_board(board_slots)
                print(f'{turn} is the WINNER!')
                break
            elif board_slots['1'] == board_slots['5'] == board_slots['9']  != '': # digonal right
                build_board(board_slots)
                print('\n Game over..\n')
                print(f'{turn} is the WINNER!')
                break
            elif board_slots['3'] == board_slots['5'] == board_slots['7']  != '': # digonal left
                build_board(board_slots)
                print('\n Game over..\n')
                print(f'{turn} is the WINNER!')
                break
            elif count == 9:
                build_board(board_slots)
                print('\nGAME OVER\n' + 'Welp.. I guess nobody lost')
                break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

play_game()





        







          

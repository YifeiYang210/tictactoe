# write your code here


def print_grid_state(stage):
    stage_list = list(stage)
    print("---------")
    for p in range(0, 9, 3):
        print(f"| {' '.join(stage_list[p:p + 3])} |")
    print("---------")


def check_player_wins(stage, player='X'):
    for i in range(0, 9, 3):  # in a row
        if stage[i] == stage[i + 1] == stage[i + 2] == player:
            return True
    for i in range(0, 3):  # in a column
        if stage[i] == stage[i + 3] == stage[i + 6] == player:
            return True
    if stage[0] == stage[4] == stage[8] == player:  # diag
        return True
    if stage[2] == stage[4] == stage[6] == player:  # reverse_diag
        return True
    return False


def analyze_game_state(stage):
    o_wins = check_player_wins(stage, 'O')
    x_wins = check_player_wins(stage, 'X')
    empty_cells = '_' in stage
    more_move = abs(stage.count('X') - stage.count('O')) > 1

    if (o_wins and x_wins) or more_move:
        print("Impossible")
        return False
    elif o_wins:
        print("O wins")
    elif x_wins:
        print("X wins")
    elif empty_cells:
        # print("Game not finished")
        return False
    elif not empty_cells:
        print("Draw")

    return True


def analyze_user_input(stage):
    while True:
        try:
            move_x, move_y = input().split()
        except ValueError:
            print("You should enter numbers!")
            continue
        else:
            if not (move_x.isdigit() and move_y.isdigit()):
                print("You should enter numbers!")
                continue
            move_x, move_y = int(move_x), int(move_y)
            if not (1 <= move_x <= 3 and 1 <= move_y <= 3):
                print("Coordinates should be from 1 to 3!")
                continue
            idx = (move_x - 1) * 3 + (move_y - 1)
            if stage[idx] != '_':
                print("This cell is occupied! Choose another one!")
                continue
            return idx


def system_init():
    previous_stage = '_' * 9
    print_grid_state(previous_stage)
    should_x_turn = True
    return previous_stage, should_x_turn


def move_state_core(previous_stage, should_x_turn, idx):
    previous_stage_list = list(previous_stage)

    if should_x_turn:  # move X
        previous_stage_list[idx] = 'X'
        should_x_turn = False
    else:  # move O
        previous_stage_list[idx] = 'O'
        should_x_turn = True
    current_stage = ''.join(previous_stage_list)
    print_grid_state(current_stage)

    previous_stage = current_stage

    return previous_stage, should_x_turn


def tic_tac_toe_play():
    previous_stage, should_x_turn = system_init()

    while True:
        # user part
        idx = analyze_user_input(previous_stage)

        # logic part
        previous_stage, should_x_turn = move_state_core(previous_stage, should_x_turn, idx)

        # judge part
        if analyze_game_state(previous_stage):
            break


if __name__ == '__main__':
    tic_tac_toe_play()

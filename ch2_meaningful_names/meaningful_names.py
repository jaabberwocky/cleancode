# 1. Use intention-revealing names

# Answers the following questions:
# 1. Why it exists
# 2. What it does
# 3. How it is used
# 4. Should not need a comment

d = 0 # elapsed time in days

# better variables
elapsed_time_in_days = 0
days_since_creation = 45
days_since_modification = 6

# functions should not be hard to decipher
def get_them(another_list):
    list1 = []
    for i in range(len(another_list)):
        for cell in range(len(another_list[i])):
            if another_list[i][j] == 4:
                list1.append(another_list[i][j])
    return list1


cell_status = {
    1: 'Empty'
    2: 'Occupied',
    3: 'Unused',
    4: 'Flagged'
}

def get_flagged_cells(game_board, cell_status):
    flagged_cells = []

    for row_index in range(len(game_board)):
        for col_index in range(len(another_list[row_index]))::
            if cell_status[game_board[row_index][col_index]] == 'Flagged':
                flagged_cells.append(game_board[row_index][col_index])
    return flagged_cells

# 2. Avoid disinformation

def gets_max_of_list(arr):
    maximum = None
    for a in arr:
        if maximum is None or a > maximum:
            maximum = a
    arr.append(maximum)
    return maximum

# 3. Meaningful distinctions

# dont rely on misspellings
maxx = min
arr = [1,2,3,4]
maxx(arr)

# what is the difference?
get_active_account()
get_active_accounts()
get_active_accounts_all()

# 4. Class names should be nouns 

class Person =
{...}

class Walking = 
{...}# bad

# 5. Method names should be verbs
Person.get_name()
Person.walk(x = 1, y = 5)

# 6. Don't be cute
Person.use_holy_hand_grenade()

# 7. Pick one word per concept
fetch()
retrieve()
get()




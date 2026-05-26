# AI gets 4 in a row
# AI has 3 in a row and one empty
# AI has 2 in a row and 2 empty
# Human has 4 in a row
# Human has 3 in a row and 1 empty
# Human has 2 in a row and 2 empty

empty = 0
ai = 2
human = 1

def evaluate_window(window):
    evaluation = 0
    ai_count = window.count(ai)
    human_count = window.count(human)
    empty_count = window.count(empty)

    if ai_count == 4:
        evaluation += 100000
    elif ai_count == 3 and empty_count == 1:
        evaluation += 40
    elif ai_count == 2 and empty_count == 2:
        evaluation +=20
    elif human_count == 4:
        evaluation -= 100000
    elif human_count == 3 and empty_count == 1:
        evaluation -= 80
    elif human_count == 2 and empty_count == 2:
        evaluation -= 40

    return evaluation


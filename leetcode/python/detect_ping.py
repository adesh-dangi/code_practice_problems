from itertools import combinations_with_replacement
from itertools import permutations

def unique_combinations(input_list, size):
    input_list = sorted(set(input_list))  # remove duplicates, sort for consistent output
    result = set()
    
    for combo in combinations_with_replacement(input_list, size):
        # Create all unique permutations of each combo
        perms = set(permutations(combo))
        for p in perms:
            result.add(''.join(map(str, p)))
    
    return sorted(result, key=int)

def solution1(pin):
    """
        1   2   3
        4   5   6
        7   8   9
            0
    """
    pin_side_map = {
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [5, 7, 8, 9, 0],
        9: [6, 8, 9],
        0: [0, 8]
    }
    def get_pins(pin):
        if len(pin) == 1:
            return pin_side_map[int(pin)]
        else:
            pins = []
            for p in pin:
                pins.extend(pin_side_map[int(p)])
            return unique_combinations(set(pins), len(pin))
    return get_pins(pin)


from itertools import product

def solution(pin):
    pin_side_map = {
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [5, 7, 8, 9, 0],
        9: [6, 8, 9],
        0: [0, 8]
    }

    # Get list of lists of possible digits per original digit
    options = [pin_side_map[int(d)] for d in pin]

    # Cartesian product of those options
    combos = product(*options)

    # Return as strings
    return sorted([''.join(map(str, combo)) for combo in combos])

print(solution("8"))
print(solution("11"))
print(solution("1357"))



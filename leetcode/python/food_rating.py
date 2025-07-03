def solution(N, ratings):
    from collections import defaultdict

    food_ratings = defaultdict(list)

    # Step 1: group all ratings by food_code
    for food_code, rate in ratings:
        food_ratings[food_code].append(rate)

    best_food = None
    best_avg = -1

    for food_code in food_ratings:
        avg = sum(food_ratings[food_code]) / len(food_ratings[food_code])
        if avg > best_avg:
            best_avg = avg
            best_food = food_code
        elif avg == best_avg:
            best_food = min(best_food, food_code)

    return best_food

N=4
ratings = [[512,3], [123,3], [897,4], [123,5]]
print(solution(N, ratings))

ratings = [[512,5], [123,5], [897,1], [123,5]]
print(solution(N, ratings))
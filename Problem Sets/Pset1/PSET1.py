cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
limit = 10

def max_weight_cow(cow_list:dict):
    '''''''''
    assumes cow_list is not empty
    return name of max weight cow
    '''''''''
    value = max(cow_list.values())
    return [name for name,weight in cow_list.items() if weight == value][0]


def pick_cow(cow_list:dict):
    cow_name = max_weight_cow(cow_list)
    cow_weight = cow_list[cow_name]
    del(cow_list[cow_name])
    return (cow_name, cow_weight)

def move_cows(cow_list: dict, weight):
    result = []
    cows_left = cow_list.copy()
    while len(cows_left) != 0:
        race = []
        weight = 0
        while weight <= limit:
            race.append(pick_cow(cows_left)[0])
            weight += pick_cow(cows_left)[1]

print(move_cows(cows, limit))

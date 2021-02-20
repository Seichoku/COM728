def sum_weight(beep_weight, boop_weight):
    total_weight = beep_weight + boop_weight
    return total_weight

def calc_avg_weight(beep_weight, boop_weight):
    avg_weight = (beep_weight+boop_weight)/2
    return avg_weight

def run():
    print("Ener beep weight")
    beep_weight = float(input())
    print("Enter Bop Weight")
    boop_weight = float(input())

    print("What action would you like to carry out\n Sum or Average")
    action = str(input())
    if action == 'sum':
        answer = sum_weight(beep_weight, boop_weight)
        print(f"The Total weight of both bots is {answer}")
    elif action == 'average':
        answer = calc_avg_weight(beep_weight, boop_weight)
        print(f"The average weight of both bots is {answer}")
    else:
        print("select an option from the options stated above")

run()
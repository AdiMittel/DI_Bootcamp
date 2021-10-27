import random
def throw_dice():
    return random.randint(1,6)

def throw_untill_double():
    d1 = throw_dice()
    d2 = throw_dice()
    count = 0
    while d1 != d2:
        print(f'cubes are {d1} {d2}')
        count += 1
        d1 = throw_dice()
        d2 = throw_dice()
    print(f'cubes are {d1} {d2}')
    return count

def results_avg(res_list):
    return sum(res_list)/len(res_list)

def main():
    results = []
    for num in range(0,100):
        results.append(throw_untill_double())
    print(f'it took {sum(results)} tries to get 100 doubles!')
    print(f'Average of throw\'s : {results_avg(results)}')

main()
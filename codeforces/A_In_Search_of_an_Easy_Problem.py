n = int(input())
persons_opinion = str(input())


def in_search_of_easy_problem(n, persons_opinion):
    for op in persons_opinion:
        if op == '1':
            return 'HARD'   
    return 'EASY'

print(in_search_of_easy_problem(n, persons_opinion))
    
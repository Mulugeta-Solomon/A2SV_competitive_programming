if __name__ == '__main__':
    data = []
    
    for _ in range(int(input())):   
        name = input()
        score = float(input())
        data.append([name, score])

def second_lowest_score(data):
    sorted_data = sorted(data, key = lambda x: [x[1], x[0]]) 
    unique_score = sorted(set(score for _, score in sorted_data))
    second_low_score = unique_score[1]
    second_lowest_score_names = [names for names, score in sorted_data if score == second_low_score]
    
    for name in second_lowest_score_names:
        print(name)
    
second_lowest_score(data)
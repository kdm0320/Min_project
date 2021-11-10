from collections import Counter
def solution(genres, plays):
    answer = []
    count = Counter(genres)
    all_list = []
    new_hash = {}
    for genre, play in zip(genres, plays):
        all_list.append((genre, play))
    for genre_key in count:
        temp = 0
        for genre, play in all_list:
            if genre == genre_key:
                temp += play
                new_hash[genre] = temp

    new_hash = dict(sorted(new_hash.items(), key=lambda x: x[1], reverse=True))
    temp = 0
    temp_list = []
    for bigger_genre in new_hash:
        for order, element in enumerate(all_list):
            if element[0] == bigger_genre:
                temp_list.append([element[1], order])
        temp_list.sort(reverse=True,key=lambda temp_list: temp_list[0])
        for i in temp_list:
            if temp < 2:
                answer.append(i[1])
                temp += 1

        temp = 0
        temp_list = []
    return answer

genres = ["classic", "pop", "classic", "pop", "classic", "classic"]
plays =[400, 600, 150, 600, 500, 500]
print(solution(genres,plays))



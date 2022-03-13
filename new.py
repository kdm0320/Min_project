def solution(money, costs):
    answer = 0
    cost_hash = {}
    coins = [1,5,10,50,100,500]
    use = [1]
    for i in range(6):
        cost_hash[coins[i]] = costs[i]
    for i in range(1,6):
        if cost_hash[1]*coins[i] >= cost_hash[coins[i]]:
            use.append(coins[i])
    use.sort(reverse=True)
    cnt = 0
    for coin in use:
        cnt+=money//coin
        answer+=cost_hash[coin]*cnt
        cnt=0
        money%=coin

    print(use)

    return answer


money = 1999
costs = 	[2, 11, 20, 100, 200, 600]


print(solution(money,costs))
def playerRank(rankedScore, playerScore):
    unioque_score = list(reversed(sorted(set(rankedScore))))
    i = len(unique_score)
    result = []
    
    for player in playerScore:
        while (i > 0) and (player >= unique_score[i-1]):
            i -= 1
        result.append(i+1)
    return result


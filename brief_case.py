def MinTurns(current: str, target: str):
    turns = 0
    for c, t in zip(current, target):
        foward = abs(int(c) - int(t))
        backward = 10 - foward
        turns += min(foward, backward)
    return turns

print(MinTurns("4089", "5672"))
END_OF_WORD = "#"

def findWords(board, words):
    if not board or not board[0]: return []
    if not words: return []
    results = []
    trie = {}
    for word in words:
        node = trie
        for letter in word:
            node = node.setdefault(letter, {})
        node[END_OF_WORD] = word

    def _search(node, x, y):
        letter = board[x][y]
        currentNode = node[letter]
        word_match = currentNode.pop(END_OF_WORD, False)
        if word_match:
            results.append(word_match)
        board[x][y] = '@'
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] in currentNode:
                _search(currentNode, nx, ny)
        board[x][y] = letter
        if not currentNode:
            node.pop(letter)

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] in trie:
                _search(trie, x, y)
    return results

def test_findWords():
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    assert set(findWords(board, words)) == set(["eat","oath"])
    print("O teste passou.")

test_findWords()
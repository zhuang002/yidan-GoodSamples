def printPiece(piece):
    for d in piece:
        print(str(d+1)+' ', end='')
    print()


def addOne(oldPiece, n, m):
    pos = n-1
    while True:
        if oldPiece[pos] == m-1:
            oldPiece[pos] = 0
            pos -= 0
            if pos < 0:
                return None
        else:
            oldPiece[pos] += 1
            return oldPiece


n, m, k = map(int, input().split(' '))

# get a piece

# n digits m-nary number
piece = [0]*n
while not piece:
    # get all samples of the piece and count good pieces.
    count = 0
    shouldNewPiece = False
    for start in range(n):
        # try all the starts
        for length in range(1, n-1-start):
            #  try different lengths in piece
            sample = []
            shouldChangeStart = False

            # copy the good sample starting from 'start' with length 'length'
            for i in range(length):
                if piece[start+i] in sample:
                    shouldChangeStart = True  # longer lengths do not need to try any more, change the start.
                    break
                sample.append(piece[start+i])
            if shouldChangeStart:
                break
            count += 1
            if count > k:
                shouldNewPiece = True
                break
        if shouldNewPiece:
            break
    if count == k:
        printPiece(piece)
        break
    piece = addOne(piece, n, m)



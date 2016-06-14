# Original Java code:
# http://codegolf.stackexchange.com/questions/5418/brainfuck-golfer/5440#5440

def repetitions():
    G = []
    for x in range(256):
        G.append([])
        for y in range(256):
            delta = y - x
            if delta > 128:
                delta -= 256
            if delta < -128:
                delta += 256

            if delta >= 0:
                G[x].append("+" * delta)
            else:
                G[x].append("-" * -delta)
    return G

def multiplications(G):
    for x in range(256):
        for n in range(1, 40):
            for d in range(1, 40):
                for _ in [(-1, 1, 256, 0), (1, -1, 0, 256)]:
                    j = x
                    y = 0

                    for i in range(256):
                        if j == 0:
                            s = "[{0}>{1}<]>".format("-" * d, "+" * n)

                            if len(s) < len(G[x][y]):
                                G[x][y] = s
                            break
                        j = (j + _[0] * d + _[2]) & 255
                        y = (y + _[1] * n + _[3]) & 255
    return G


def concatenation(G):
    for x in range(256):
        for y in range(256):
            for z in range(256):
                if len(G[x][z]) + len(G[z][y]) < len(G[x][y]):
                    G[x][y] = G[x][z] + G[z][y]
    return G


if __name__ == "__main__":
    import pickle
    G = repetitions()
    G = multiplications(G)
    G = concatenation(G)
    with open("table.pkl", "wb") as f:
        pickle.dump(G, f)

import math

MAX = 1000
MIN = -1000

scores = [3, 5, 6, 9, 1, 2, 0, -1]

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:

        best = MIN

        for i in range(2):
            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            False,
                            values,
                            alpha,
                            beta)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:

        best = MAX

        for i in range(2):
            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            True,
                            values,
                            alpha,
                            beta)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

print("Optimal Value:",
      alphabeta(0, 0, True, scores, MIN, MAX))

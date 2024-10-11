def minmax(depth, node_index, is_max_turn, scores, height):
    if depth == height:
        return scores[node_index]

    if is_max_turn:
        return max(minmax(depth + 1, node_index * 2, False, scores, height),
                   minmax(depth + 1, node_index * 2 + 1, False, scores, height))
    else:
        return min(minmax(depth + 1, node_index * 2, True, scores, height),
                   minmax(depth + 1, node_index * 2 + 1, True, scores, height))

def calculate_height(length):
    import math
    return math.log2(length)
scores = [3, 5, 6, 9, 1, 2, 0, -1]
height = calculate_height(len(scores))

result = minmax(0, 0, True, scores, height)
print("Optimal value:", result)

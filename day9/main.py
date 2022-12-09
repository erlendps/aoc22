# y grows downwards, x towards right
sign_map = {"U": -1, "R": 1, "D": 1, "L": -1}

head = [0, 0]
tails = [[0, 0] for _ in range(9)]
tail_visited = set([])

# order is basically if we are moving along a column or row
# order = (0, 1) = column
# order = (1, 0) = row


def is_neighbor(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def update_tail(order: tuple, sign: int):
    curr_head = head
    for i in range(len(tails)):
        curr_tail = tails[i]
        if is_neighbor(curr_head, curr_tail):
            pass
        elif curr_head[order[0]] == curr_tail[order[0]]:
            curr_tail[order[1]] += sign
        elif curr_head[order[0]] != curr_tail[order[0]]:
            if curr_head[order[0]] - curr_tail[order[0]] < 0:
                to_add = max(curr_head[order[0]] - curr_tail[order[0]], -1)
            else:
                to_add = min(curr_head[order[0]] - curr_tail[order[0]], 1)
            curr_tail[order[0]] += to_add
            curr_tail[order[1]] += sign
        curr_head = tails[i]


with open("test2.txt", "r") as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        sign = sign_map[line[0]]
        if line[0] == "U" or line[0] == "D":
            order = (0, 1)  # move along column
        else:
            order = (1, 0)  # move along row

        for _ in range(int(line[1])):
            head[order[1]] += sign
            update_tail(order, sign)
            tail_visited.add(tuple(tails[-1]))


print(len(tail_visited))

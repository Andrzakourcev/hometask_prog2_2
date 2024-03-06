n = int(input())
s = []
for i in range(n):
    a, b = map(int, input().split())
    s.append([a, b])
s.sort(key=lambda x: x[1])


def Points(s):
    marked_points = []
    current_right = s[0][1]
    marked_points += [current_right]
    for i in s[1:]:

        if i[0] <= current_right:
            continue
        else:
            current_right = i[1]
            marked_points += [i[1]]

    return len(marked_points), marked_points


n, points = Points(s)
print(n)
print(*points)

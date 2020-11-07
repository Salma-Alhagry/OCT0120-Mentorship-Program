def cumsum(li):
    result = []
    total = 0
    for elem in li:
        total += elem
        result.append(total)
    return result


t = [1, 2, 3]
print(cumsum(t))

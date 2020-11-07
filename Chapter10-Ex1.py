def nested_sum(li):
    result = 0
    for elem in li:
        result += sum(elem)
    return result


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

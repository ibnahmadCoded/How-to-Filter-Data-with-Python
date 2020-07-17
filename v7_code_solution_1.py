def filter_list(l):
    'return a new list with the strings filtered out'

    output = []
    for item in l:
        if type(item) == int:
            output.append(item)
    return output

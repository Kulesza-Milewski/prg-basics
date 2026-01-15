def f(d):
    avg = 0
    for data in d:
        avg += d[data]
    avg = avg/len(d)

    count = 0
    for data in d:
        if avg < d[data]:
            count += 1
    return count


print(f({"LO231":150,"BA787":120,"NZ15":30}))
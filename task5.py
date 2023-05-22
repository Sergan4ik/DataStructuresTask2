import random

def linear_find(container, count):
    res_idx = []
    res = []
    for j in range(count):
        cur_min = 0

        for i in range(len(container)):
            if res_idx.count(i) > 0:
                continue
            if container[cur_min] > container[i]:
                cur_min = i

        res_idx.append(cur_min)
        res.append(container[cur_min])

    res.sort()
    return res

keys = random.sample(range(101), 15)
k = 5

mins = linear_find(keys , k)
print(keys)
print(mins)

keys.sort()

print(keys)
print(keys[0:k])

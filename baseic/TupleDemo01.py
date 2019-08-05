
def args(kv):
    if len(kv) == 3:
        locator = kv[0:2]
        index = kv[2]
        print(locator)
        print(index)
    else:
        print(*kv)

test=("A","aaaaaa")
args(test)

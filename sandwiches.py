from itertools import islice
import collections
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

def ArrayChallenge(arr):
    ## convert to list becasuse my IDE thinks it's getting a string
    #arr = list(map(int, arr))
    arr = [4,5,2,3,1,0]
    print(type(arr), arr)
    sandwiches = arr.pop(0)
    arra = list(sliding_window(arr,2))
    print(sandwiches, arr)
    hungerDiffs = [abs(i[0]-i[1]) for i in arra]

    return arr

print(ArrayChallenge(input()))


# if __name__ == '__main__':
#     print(ArrayChallenge(list([4,5,2,3,1,0])))
# #arr=[4,5,2,3,1,0]

# Different type of problem, given a snippet of code, debug it to see why it's not working
# original code in comments, fixed code ready to run

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2) # was declared as int((n + 1)/2) which is wrong index for starting at 0
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # shifted over same as line 7, was indexed wrong at ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # was ed = ed + 1 which is moving the wrong way along the array

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)

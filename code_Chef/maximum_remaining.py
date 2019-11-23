def maxrem(num):
    rem=0
    nu = max(num)
    num.remove(nu)

    x=max(num)
    if((x%nu)>rem):
        rem=x%nu
        return rem
    num.remove(x)
    return rem

if __name__ == '__main__':
    N = int(input())
    numstr = input()
    nums = set(map(int, numstr.split()))
    r = maxrem(nums)
    print(r)



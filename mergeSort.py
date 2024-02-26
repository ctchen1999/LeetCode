def merge_sort(L: list):
    if len(L) == 0:
        return []
    elif len(L) == 1:
        return L
    
    midPoint = len(L) // 2
    left, right = L[:midPoint], L[midPoint:]
    left, right = merge_sort(left), merge_sort(right)
    return merge(left, right)

def merge(l1, l2):
    result = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))
    if l1 != None:
        result.extend(l1)
    if l2 != None:
        result.extend(l2)
    return result
            

if __name__ == '__main__':
    aList = [8,2,5,3,4,1,2,6,7]
    ans = merge_sort(aList)
    print(ans)
    
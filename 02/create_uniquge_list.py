def merge(lst1, lst2): #O(n)
    p1, p2 = 0, 0
    answer = []
    current_elem = None

    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] == lst2[p2] and lst1[p1] != current_elem:
            current_elem = lst1[p1]
            answer.append(current_elem)
            p1 += 1
            p2 += 1
        elif lst1[p1] == lst2[p2] and lst1[p1] == current_elem:
            p1 += 1
            p2 += 1
        elif lst1[p1] > lst2[p2]:
            p2 += 1
        else:
            p1+=1
    return answer
            
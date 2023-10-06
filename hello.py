# 8줄 4칸 뾰족한 중간이 빈
# * 
# *
# **
# **
# * *
# * *
# *  *
# ****

ROWS = 8

def isBoundary(row, col) :
    return row == 0 or row == ROWS -1 or col == 0 or col == row // 2

output = ""
for row in range(ROWS) :
    for col in range(row // 2 + 1) :
        if isBoundary(row, col) :
            output += "*"
        else :
            output += " "
    output += "\n"
print(output)    

"""
1 ~ 100 숫자 중 이진 표현에서 0이 하나만 들어 있는 요소와 그 합을 구하시오.
"""
output = []
for num in range(1, 101) :
    if "{:b}".format(num).count('0') == 1 : 
        print(num)
        output.append(num)
print(output)     #[2, 5, 6], <>
print(sum(output)) #[2, 5, 6] <>

output = [num for num in range(1, 101) if "{:b}".format(num).count('0') == 1]
for i in output :
    print("{} : {}".format(i, "{:b}".format(i)))
print(sum(output)) # [2, 3, 6]

""" 배열 원소 개수 출력 """
items = [65, 3, 4, 5, 3, 2, 2, 6, 5, 6, 54, 34]
#딕셔너리 활용
원소집합 = set()
print(type(원소집합))

#반복
for 요소 in items :
    원소집합.add(요소)
#key 개수 출력
print(len(원소집합))

ele_count = {'a':0, 'g':0, 't':0, 'c':0}
dna = "agtcagttgca"
for i in range(0, len(dna)) :
    ele_count[dna[i]] += 1
for key, val in ele_count.items() :
    print("{}는 {}개".format(key, val))

def myFunc(x) :
    return x * x * x + x * x + 2 * x + 1
def myFunc2(x) :
    return x ** 3 + x ** 2 + 2 * x + 1

def mul(*vals) :
    ret = 1
    for val in vals:
        ret *= val
    return ret
print(mul(3, 5, 2, 1))

""" 재귀함수로 피보나치 구현 """
count = 0
calced = {1 : 1, 2 : 1}
def fibo(nth) :
    global count
    global calced
    count += 1
    if nth in calced.keys() :
        return calced[nth]
    if nth == 1 or nth == 2 :
        return 1
    cur_res = fibo(nth - 1) + fibo(nth - 1)
    calced[nth] = cur_res
    return cur_res

print(fibo(1000))
print(str(count) + "번 계산")
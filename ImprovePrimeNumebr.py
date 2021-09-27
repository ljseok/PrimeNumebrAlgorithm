import math

def is_prime_number(x): # 소수 판별 함수 정의
    for i in range(2,int(math.sqrt(x))+1): # 2부터 x의 제곱근 까지 모든 수를 확인한다
        if x % i == 0: # 해당수로 나누어 떨어진다면
            return False # 소수가 아님
    return True # 소수

print(is_prime_number(4))
print(is_prime_number(17))
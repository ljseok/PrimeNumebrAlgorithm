def is_prime_number(x): # 소수 판별 함수 정의
    for i in range(2, x): # 2부터 x-1 까지 모든 수를 확인
        if x % i == 0: # 해당하는 수로 나누어 떨어진다면
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(17))
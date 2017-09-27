# 변수 이름은 문자, 숫자, '_'로 구성해야 한다.
import keyword

friend = 1
a = 10
my_name = '노태훈'
_your_name = '박보영'
member1 = '이보영'

# 에러
# $friend = 2
# a! = 1
# 1abc = 10

# 에러 : 예약어는 사용할 수 없다.
# def = 10
print(keyword.kwlist)
print(len(keyword.kwlist))

# 한글이름의 변수도 가능하다.
가격1 = 2000
print(가격1 - 200)
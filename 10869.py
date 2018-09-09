#두 자연수 A와 B가 주어진다. 이 때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.


x,y=input().split()

print(int(x)+int(y)) #split()은 string type으로 받기 때문에 int로 형변환 후 출력
print(int(x)-int(y))
print(int(x)*int(y))
print(int(x)//int(y))
print(int(x)%int(y))
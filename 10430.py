#(A+B)%C는 (A%C + B%C)%C 와 같을까?
#(A×B)%C는 (A%C × B%C)%C 와 같을까?
#세 수 A, B, C가 주어졌을 때, 위의 네가지 값을 구하는 프로그램을 작성하시오.

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
print((a+b)%c) #split()은 string type으로 받기 때문에 int로 형변환 후 출력
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

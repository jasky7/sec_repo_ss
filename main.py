import add
import sub
import mul
import div
import exp
import sqrt

a = int(input("a-> "))
b = int(input("b-> "))
print("a+b")
print(add.add(a, b))
print("a-b")
print(sub.sub(a, b))
print("a*b")
print(mul.mul(a, b))
print("a/b")
print(div.div(a, b))
print("a^(b)")
print(exp.exp(a, b))
print("sqrt(a)")
print(sqrt.sqrt(a))

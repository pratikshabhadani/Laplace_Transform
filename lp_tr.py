import sympy as sp
def traprule(a, b, expr):
    n = int(b * 100)
    a= float(a)
    b= float(b)
    h= float((b-a)/n)
    p= [0.0]*(n+1)
    y= [0.0]*(n+1)
    x = sp.symbols('x')
    expr = sp.sympify(expr)
    for i in range(0, n+1):
        p[i]= a+ i*h
    for i in range(0, n+1):
        y[i]= expr.subs(x, p[i]).evalf()
    ans= (y[0]+y[n])/2
    for i in range(1, n):
        ans= ans+ y[i]
    ans= ans*h
    return ans


def upperbound(expr, l):
    upp_bd= 10
    x = sp.symbols('x')
    while upp_bd<=1000000:
        val= expr.subs(x, upp_bd)
        if abs(val-l)<= 0.000001:
            return upp_bd
        else:
            upp_bd= upp_bd*10
    return "non- computable"


def lap_transform(expr_str, s):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    lap_expr= sp.exp(-s*x)*expr
    limit_at_infinity = sp.limit(lap_expr, x, sp.oo)
    if limit_at_infinity == sp.oo:
        print("Laplace transform is not possible as function doesn't coverge at infinity.")
        return
    limit_at_infinity = float(limit_at_infinity)
    upp_bd= upperbound(lap_expr, limit_at_infinity)
    if upp_bd!="non- computable": 
        upp_bd= float(upp_bd)
        x= traprule(0.0, upp_bd, lap_expr)
        print(f"the output is:{x} ")
        return
    else:
        print("Laplace transform could not be calculated due to system limitations.")

    
expr_str = input("Enter the function f(x): ")
s = float(input("Enter the value of s: "))
lap_transform(expr_str, s)

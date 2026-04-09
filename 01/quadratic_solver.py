def solve_quadratic_equation(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print('x - любое число')
        return None
        
    if a == 0 and b == 0 and c != 0:
        return None
        
    if a == 0 and b != 0:
        return tuple([-c / b])
        
    disc = b**2 - 4 * a * c
    
    if disc < 0:
        return None
          
    if disc == 0:
        return tuple([-b/(2*a)])
        
    return tuple([(-b - disc**0.5) / (2 * a), (-b + disc**0.5) / (2 * a)])
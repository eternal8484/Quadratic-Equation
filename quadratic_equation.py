import random 

''' 
      !TO
        MAKE
            QUADRATIC
                    EXPRESSION!
'''
l_var = ['x','y','s','t','z','p','q']
var = random.choice(l_var)
uc = f"{var}\u00B2"

a = int(input("Enter any integer for coefficient for 'a': "))
if(a == 0):
  raise ValueError("You cannot set a = 0 in a quadratic expression")

b = int(input("Enter any integer for coefficient for 'b': "))
c = int(input("Enter any integer for coefficient for 'c': "))

sign_b = '+' if b > 0 else ''
sign_c = '+' if c > 0 else ''

quadratic_expression = f"{a}{uc}{sign_b}{b}{var}{sign_c}{c}"
print("The quadratic expression is:", quadratic_expression)

''' 
    !TO 
      SOLVE
          QUADRATIC
                    EXPRESSION!
'''

# Calculate the roots using the quadratic formula
discriminant = b**2 - 4*a*c

# Check if the discriminant is non-negative for real roots
if discriminant >= 0:
    root1 = (-b + (discriminant)**0.5) / (2 * a)
    root2 = (-b - (discriminant)**0.5) / (2 * a)
    roots = (root1, root2)
    print("The roots of the quadratic expression are:", roots)
else:
    print("The roots are complex numbers.")

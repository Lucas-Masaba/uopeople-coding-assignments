import math # Import the math module to use the sqrt function(square root function)

def hypotenuse(leg1, leg2):
    # Pythagorean theorem: a^2 + b^2 = c^2
    # Substituting the values of a and b, we get:
    hypotenuse_length = math.sqrt(leg1**2 + leg2**2)
    return hypotenuse_length
  
print(hypotenuse(3, 4))  # Expecting a float, 5.0 to be returned
print(hypotenuse(5, 12))  # Expected output: 13.0
print(hypotenuse(7, 24))  # Expected output: 25.0
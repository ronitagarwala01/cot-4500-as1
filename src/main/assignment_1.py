import numpy as np

#Helper function to normalize a floating point number
#Returns tuple containing normalized x and exponent
def normalize(x):
    exp = 0
    x_str = str(x)
    dec_idx = x_str.find('.')
    for i in range(0, len(x_str)):
        if x_str[i] != '0' and x_str[i] != '.':
            if i < dec_idx:
                exp = i-dec_idx
            else:
                exp = i-(dec_idx+1)
            break
            
    x *= (10**exp)
    return (x, -exp)

# Helper function to evaluate function for problem 6
def func(x):
    return (x**3) + (4 * (x**2)) - 10

# Helper function to evaluate derivative of function for problem 6
def d_func(x):
    return (3 * (x**2)) + (8 * x)

if __name__ == "__main__":
    b_str = "010000000111111010111001"
    
    while(len(b_str) < 64):
        b_str += '0'

    s = int(b_str[0])
    c = 0
    f = 0

    for i in range(1, 12):
        c += int(b_str[i])*(2**(11-i))

    for i in range(12, 64):
        f += int(b_str[i])*(0.5**(i-11))

    ans_1 = ((-1)**s)*(2**(c-1023))*(1+f)
    print(ans_1)
    print()

    (f, exp_f) = normalize(f)
    
    # Chop 3
    f_chop = float((str(f)[0:5]))

    #Obtain chop 3 answer 
    ans_2 = ((-1)**s)*(2**(c-1023))*(1+f_chop)
    (ans_2, exp_ans_2) = normalize(ans_2)
    ans_2 = float((str(ans_2)[0:5]))
    ans_2 *= 10**exp_ans_2
    
    print(ans_2)
    print()

    # Round 3
    f_round = f + 0.0005
    f_round = float((str(f_round)[0:5]))

    #Obtain round 3 answer 
    ans_3 = ((-1)**s)*(2**(c-1023))*(1+f_round)
    (ans_3, exp_ans_3) = normalize(ans_3)
    ans_3 += 0.0005
    ans_3 = float((str(ans_3)[0:5]))
    ans_3 *= 10**exp_ans_3

    print(ans_3)
    print()

    #Absolute  and relative errors
    ans_4_abs = abs(ans_1 - ans_3)
    ans_4_rel = ans_4_abs / abs(ans_1)

    print(ans_4_abs)
    print(ans_4_rel)
    print()

    # Minimimum term problem
    k = 1
    term = 0
    while(True):
        term = ((-1)**k) * (1 / (k**3))
        if abs(term) < 10**(-4):
            break
        k += 1

    ans_5 = k-1
    print(ans_5)
    print()

    # Bisection
    tol = 10**(-4)
    left = -4.0
    right = 7.0
    i = 0 # iteration counter
    diff = abs(right - left)

    while diff > tol:
        mid = (left + right) / 2
        if (func(left) < 0 and func(mid) > 0) or (func(left) > 0 and func(mid) < 0):
            right = mid
        else:
            left = mid
        i = i+1
        diff = abs(right - left)
    
    ans_6_bi = i
    print(ans_6_bi)
    print()

    # Newton method
    p_prev = 7.0
    p_next = 0.0
    i = 1

    while(True):
        if d_func(p_prev) == 0:
            break
        else:
            p_next = p_prev - (func(p_prev) / d_func(p_prev))
            if abs(p_next - p_prev) < tol:
                break
            i += 1
            p_prev = p_next

    ans_6_new = i
    print(ans_6_new)
    print()

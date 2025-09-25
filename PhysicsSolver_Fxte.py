# PhysicsSolver_fxte.py
from sympy import symbols, Eq, solve, sqrt
import re

def mechanics_solver(inputs):
    # Try to solve
    v0 = inputs.get('v0')
    v1 = inputs.get('v1')
    a_val = inputs.get('a')
    s = inputs.get('s')
    t = inputs.get('t')
    m = inputs.get('m')
    F_val = inputs.get('F')

    print("\n=== Mechanics Solver ===")

    if s is not None and t is not None:
        # v = s/t
        v = symbols('v')
        eq = Eq(v, s/t)
        sol = solve(eq, v)
        print(f"v = s/t = {s}/{t} = {sol[0]} m/s")

    if v0 is not None and v1 is not None and t is not None:
        # a = (v1 - v0)/t
        a = symbols('a')
        eq = Eq(a, (v1 - v0)/t)
        sol = solve(eq, a)
        print(f"a = (v1 - v0)/t = ({v1}-{v0})/{t} = {sol[0]} m/s²")

    if m is not None and a_val is not None:
        # F = m*a
        F = symbols('F')
        eq = Eq(F, m*a_val)
        sol = solve(eq, F)
        print(f"F = m*a = {m}*{a_val} = {sol[0]} N")

    if v0 is not None and a_val is not None and s is not None:
        # v = sqrt(v0^2 + 2*a*s)
        v = symbols('v')
        eq = Eq(v, sqrt(v0**2 + 2*a_val*s))
        sol = solve(eq, v)
        print(f"v = sqrt(v0² + 2*a*s) = {sol[0]} m/s")

def waves_solver(inputs):
    f = inputs.get('f')
    λ = inputs.get('lambda') or inputs.get('λ')

    if f is None or λ is None:
        print("Insufficient inputs for Waves Solver.")
        return

    v = symbols('v')
    eq = Eq(v, f*λ)
    sol = solve(eq, v)
    print(f"v = f*λ = {f}*{λ} = {sol[0]} m/s")

def optics_solver(inputs):
    u = inputs.get('u')
    v_input = inputs.get('v')

    if u is None or v_input is None:
        print("Insufficient inputs for Optics Solver.")
        return

    f = symbols('f')
    eq = Eq(1/f, 1/v_input - 1/u)
    sol = solve(eq, f)
    print(f"1/f = 1/v - 1/u → f = {sol[0]} cm")

def electricity_solver(inputs):
    V = inputs.get('V')
    R = inputs.get('R')

    if V is None or R is None:
        print("Insufficient inputs for Electricity Solver.")
        return

    I = symbols('I')
    eq = Eq(V, I*R)
    sol = solve(eq, I)
    print(f"I = V/R = {V}/{R} = {sol[0]} A")

def detect_topic(user_input):
    user_input = user_input.lower()
    inputs = {}

    # Extract numbers and assign to possible variables
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", user_input)
    numbers = [float(num) for num in numbers]

    # Simple keyword-based detection
    if any(k in user_input for k in ['distance', 'velocity', 'acceleration', 'mass', 'force', 'time', 'displacement']):
        topic = 'mechanics'
        # Assign numbers to variables 
        if 'v0' in user_input: inputs['v0'] = numbers.pop(0)
        if 'v1' in user_input: inputs['v1'] = numbers.pop(0)
        if 'a' in user_input: inputs['a'] = numbers.pop(0)
        if 's' in user_input: inputs['s'] = numbers.pop(0)
        if 't' in user_input: inputs['t'] = numbers.pop(0)
        if 'm' in user_input: inputs['m'] = numbers.pop(0)
        if 'F' in user_input: inputs['F'] = numbers.pop(0)

    elif any(k in user_input for k in ['wavelength', 'frequency', 'wave']):
        topic = 'waves'
        if numbers: inputs['f'] = numbers.pop(0)
        if numbers: inputs['lambda'] = numbers.pop(0)

    elif any(k in user_input for k in ['focal', 'image', 'object']):
        topic = 'optics'
        if numbers: inputs['u'] = numbers.pop(0)
        if numbers: inputs['v'] = numbers.pop(0)

    elif any(k in user_input for k in ['voltage', 'resistance', 'current', 'ohm']):
        topic = 'electricity'
        if numbers: inputs['V'] = numbers.pop(0)
        if numbers: inputs['R'] = numbers.pop(0)

    else:
        topic = None

    return topic, inputs

def main():
    print("=== PhysicsSolver_fxte ===")
    print("Expect bugs! its recommended to recheck the answer.")
    while True:
        user_input = input("\nEnter your problem (or type 'exit' to quit):\n")
        if user_input.lower() == 'Exit':
            break

        topic, inputs = detect_topic(user_input)
        if topic == 'mechanics':
            mechanics_solver(inputs)
        elif topic == 'waves':
            waves_solver(inputs)
        elif topic == 'optics':
            optics_solver(inputs)
        elif topic == 'electricity':
            electricity_solver(inputs)
        else:
            print("not added yet!. More topics will be added soon..")

if __name__ == "__main__":
    main()
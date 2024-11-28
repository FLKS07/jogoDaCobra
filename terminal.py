def print_at(x,y, char):
    print(f"\033[{y}; {x}H{char}]")
    print(f"\033[0;0H", end="", flush=True) 
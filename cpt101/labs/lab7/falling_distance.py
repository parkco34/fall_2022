#!/usr/bin/env python
# Cory Parker
# CPT101
# 13 Falling Distance

def falling_distance(t):
    return G/2*t**2  # Distance

# Main function
def main():
    G = 9.8
    time = float(input("\nEnter time it takes for object to reach the ground:\n"))

    print(" \nFalling Distance")
    for count in range(10):
        time = count + 1

    print(f"Time : {time}\n Distance : , {main(): .2f}\n")
    return falling_distance(time)


if __name__ == "__main__":
    main()


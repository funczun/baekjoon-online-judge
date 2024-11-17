# https://www.acmicpc.net/problem/2588

n1 = int(input())
n2 = int(input())

# Convert n2 to str to easily access each digit.
n2_str = str(n2)

# Print the multiplication process using a loop for each digit.
for digit in n2_str[::-1]:
    result = n1 * int(digit)
    print(result)

# Finally, print the multiplication result.
print(n1 * n2)
Problem 2: Odd Number Series
Language: Python
Generate odd numbers series based on input a


a = int(input("Enter a number (a): "))
series = []
for i in range(a):
    series.append(str(2 * i + 1))
print("Output:", ", ".join(series))

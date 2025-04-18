# Name: Sai Ravi Teja Vudathala
# Program-2
''' With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
  Output: (examples)
    1) input a = 1, then output : 1
    2) input a = 2, then output : 1, 3
    3) input a = 3, then output : 1, 3, 5
    4) input a = 4, then output : 1, 3, 5, 7
    .
    .
    5) input a = x, then output : 1, 3, 5, 7, .......
'''

def series_generator(a):
    series = []
    for i in range(1, a*2):
        if i % 2 != 0:
            series.append(i)
    return series

a = int(input())
series = series_generator(a)
print(", ".join(map(str, series)))

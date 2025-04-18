# Program-4
''' Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
  (examples)
  input: [1,2,8,9,12,46,76,82,15,20,30]
  Output: 
    {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
'''
def count_multiples(input_list):
    multiples_count = {i: 0 for i in range(1, 10)}
    for i in input_list:
        for j in range(1, 10):
            if i % j ==0:
                multiples_count[j] += 1
    return multiples_count


list_input = list(map(int, input().split(',')))
print(count_multiples(list_input))
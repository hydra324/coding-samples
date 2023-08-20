arr = [4,5,2,2,5,5,5,2,5]
majority = (0,None) # count, majority element
# pass1 : find the majority element
for num in arr:
    count,elem = majority
    if count==0:
        majority = (1,num)
    elif elem==num:
        majority=(count+1,elem)
    else:
        majority=(count-1,elem)
count,elem = majority
# pass2: verify the majority element
freq = 0
for num in arr:
    if num==elem:
        freq += 1

print(f'Majority element is: {elem if freq>len(arr)//2 else None}')
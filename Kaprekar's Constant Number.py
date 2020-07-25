kaprekar_Numbers_Found = []
loop = 'loop'
def asc(n):
    # To get Ascending Order
    return int(''.join(sorted(str(n))))

def desc(n):
    # To get Descending order
    return int(''.join(sorted(str(n))[::-1]))

n = input("Specify a number: ")
n = int(n)


while True:
    # iterates, assigns the new diff
    print(desc(n), "-", asc(n), "=", desc(n)-asc(n))
    n = desc(n) - asc(n)

    if n not in kaprekar_Numbers_Found:
        # checks if already hit that number
        kaprekar_Numbers_Found.append(n)
    else:
        if kaprekar_Numbers_Found.index(n) == len(kaprekar_Numbers_Found)-1:
        # if found as the last, it is a constant...
            kaprekar_Numbers_Found = []
            kaprekar_Numbers_Found.append(n)
            loop = 'constant'
        else:
        # if not found, it is a loop
            kaprekar_Numbers_Found = kaprekar_Numbers_Found[kaprekar_Numbers_Found.index(n):]
        
        break

print('Kaprekar', loop, 'reached:', kaprekar_Numbers_Found)

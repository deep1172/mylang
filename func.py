# import math
# def logarithm(value, base):
#     result = math.log(value, base)
#     return result

def arrVal(arr, i):
    try:
        return arr[i]
    except IndexError:
        return 'null'
    

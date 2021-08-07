def find_product(list):
    product = 1
    i = 0
    output = [None] * len(list)
    while i < len(list):
        output[i] = product
        product *= list[i]
        print(output)
        i += 1
    print("==========================")
    product = 1
    i = len(list) - 1
    while i >= 0:
        output[i] *= product
        product *= list[i]
        print(output)
        i -= 1
    return output
print(find_product([1,2,3,4]))
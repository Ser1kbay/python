def grams_to_ounces(grams):
    ounces = grams * 28.3495231
    return ounces
grams = int(input())  
ounces = grams_to_ounces(grams)
print(f"{grams} grams is equal to {ounces} ounces")



# def is_even(num):
#    if num%2==0:
#       return True
#      #print("Even Number")
#    else:
#       return False
#       #print("Odd")
    
# is_even(5)

# def is_even(num):
#    return num%2==0
# print(is_even(3))


def count_vowel(word):
    count =0
    for char in word:
        if char in "aeiou":
            count+=1
    return count
print(count_vowel("ankit"))
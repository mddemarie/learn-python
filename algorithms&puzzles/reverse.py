def reverse(x):
    elements = list(x)
    num_letters = len(elements)
    count = 0
    reversed_word = []
    for e in elements:
        count += 1
        reversed_word.append(''.join(elements[num_letters - count:num_letters+1 - count]))
    return ''.join(reversed_word)

print reverse("marie")

def reverse(x):
    num_letters = len(x)
    count = 0
    reversed_word = ''
    for e in x:
      count += 1
      reversed_word += x[num_letters - count]
    return reversed_word

print reverse("abcd")
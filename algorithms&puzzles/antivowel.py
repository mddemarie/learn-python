def anti_vowel(text):
  vowels = "aeiouAEIOU"
  without_vow = ''
  num_loop = 20
  while num_loop > 0:
    num_loop -= 1
    for e in vowels:
      if e in text:
        text = text.replace(e, "")
    without_vow = text[:len(text)]
  return without_vow
print anti_vowel("Hey look words!")
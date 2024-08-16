lang1 = {'JavaScript', 'Python', 'C#', 'Java'}
lang2 = {'C++', 'Java', 'Python'}

lang_union = lang1 | lang2
lang_intersection = lang1 & lang2
lang_difference = lang1 - lang2

print("lang union: ", lang_union)
print("lang intersection: ", lang_intersection)
print("lang difference: ", lang_difference)
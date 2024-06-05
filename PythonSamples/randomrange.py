import random

chapter_list = [-1, 0, 1, 2, 3, 4, 5]
# using random.randrange() to get a random number
rand_idx = random.randrange(len(chapter_list))
random_num = chapter_list[rand_idx]

# printing random number
print("Random selected number is : " + str(random_num))

len_title=2
for i in range(1, len_title+1):
    print(i)

passw = "something123"
masked_pass = ''.join(map(lambda _: '*', passw))
print(masked_pass)
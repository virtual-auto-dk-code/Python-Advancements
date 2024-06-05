password = "something123"
masked_pass = ''.join(map(lambda _: '*', password))
print(masked_pass)
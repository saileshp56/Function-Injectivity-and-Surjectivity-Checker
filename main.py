domain = []
codomain = []
io = []
io_pairs = {}

f = open('sample_input.txt', 'r')

file_data = f.read()

file_data = file_data.strip().split('\n')
domain_string = file_data[0]
codomain_string = file_data[1]
io_string = file_data[2]

for char in domain_string.split(','):
    domain.append(char)

for char in codomain_string.split(','):
    codomain.append(char)

for char in io_string.split(','):
    io.append(char)
print(domain)
print(codomain)
print(io)
for s in io:
    _ = s.find('-')
    key = s[0:_]
    val = s[_+1:]
    if(key in io_pairs.keys()):
        print("Not a function at: ", key)
        quit()
    io_pairs[key] = val
print(io_pairs)

injected = []
for val in io_pairs.values():
    counter = 0
    for x in io_pairs.values():
        if val==x and val not in injected:
            counter+=1
    if counter > 1:
        print("Not injective at: ", val)
        injected.append(val)

for val in codomain:
    if val not in io_pairs.values():
        print("Not surjective at: ", val)


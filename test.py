from re import search
data = []

for i in range(0,14):
    
    num = chr(65+i)
    i=-1
    data.append(f"{num}")

print(data)

for x in data:
    y = data.index(x)
    print(f'{y}-{x}')

print(f"{data[3]}")

add_to = [3,4,8,9,13,14,18,19,23,24,26,27,29]

if 5 in add_to:
    print(True)

fullstring = "kazibwe julius junior"
substring = "junior"
if search('ds',fullstring) or search('ha',fullstring) :
    print(True)
else:
    print(False)
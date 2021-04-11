Items = [
    {'name':'chair','price':500},
    {'name':'phone','price':10000},
    {'name':'watch','price':1000}
]
print(list(filter(lambda x: x['name'] == 'chair', Items)))
l = Items[1]
for i in range (len(Items)):
    if Items[i]['name'] == 'chair':
        l = Items[i]
print(l)
if list(filter(lambda x: x['name'] == 'chair', Items)) !=
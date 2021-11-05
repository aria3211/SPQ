


def first(frots):
    counter = {}
    for f in frots:
        for i in f:
            if len(f) != 4:
                raise "You forget give (name or shape or mass or volume) for your fruit"
            else:
                if f[i] == "sphere" and 300<=f["mass"]<=600 and 100<=f["volume"]<=500:
                    c = f['name']
                    if c in counter:
                        counter[c]+=1
                    else:counter[c]=1
    return counter      
    






print(first(({'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 290},
    {'name':'orange', 'shape': 'sphere', 'mass': 500, 'volume': 400},
    )))

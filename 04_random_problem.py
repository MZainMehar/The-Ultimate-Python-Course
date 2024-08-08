# Name shortener function for a given name and maximum length

def name_shortener(name, max_Length):
    if(len(name) > max_Length):
        return name[:max_Length]
    else:
        return name
    
print(name_shortener("Siddharth", 5))



def name_shortener(name, max_Length):
    return name[:max_Length] if len(name) > max_Length else name

print(name_shortener("Siddharth", 5))


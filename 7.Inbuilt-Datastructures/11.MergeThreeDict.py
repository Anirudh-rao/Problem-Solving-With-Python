def merge_three_dictionaries(dict1, dict2, dict3):
    merged_dict = dict1.copy()

    # Add the key-vaue paris from dict2
    for key, value in dict2.items():
        merged_dict[key] = value
    
    # Add the key-vaue pairs from dict3
    for key,value in dict3.items():
        merged_dict[key] = value
    return merged_dict


a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4} 
c = {'e': 5, 'f': 6}
print(merge_three_dictionaries(a,b,c))
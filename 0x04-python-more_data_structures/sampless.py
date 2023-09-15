a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
def complex_delete(a_dictionary, value):
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary

new_dict = complex_delete(a_dictionary, 'C')
print(new_dict)

#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'Tony': 100, 'John': 12, 'Bob': 14, 'Mike': 14, 'joe': 180, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

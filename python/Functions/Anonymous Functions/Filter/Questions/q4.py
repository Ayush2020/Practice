
# //! WAP to get only positive values from a given collection using filters

ls = [-10, 20, -30, 40, 50, -60]

print(list(filter(lambda x : x > 0, ls)))
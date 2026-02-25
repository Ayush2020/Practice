
#//! statements --> ['withdrawal : 5000', 'deposit : 20000', 'withdrawal : 10000', 'withdrawal : 4000', 'withdrawal : 40000'] fetch only withdrawals from the statements

statements = ['withdrawal : 5000', 'deposit : 20000', 'withdrawal : 10000', 'withdrawal : 4000', 'withdrawal : 40000']
print(list(filter(lambda x : 'withdrawal'.lower() in x, statements)))
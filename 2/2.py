import pandas as pd

df_pw = pd.read_table(r"input.txt", sep=" ", header=None)

df_pw[['low', 'high']] = df_pw[0].str.split('-', n=1, expand=True).astype('int')
df_pw['letter'] = df_pw[1].str.rstrip(':')
df_pw['pw'] = df_pw[2]

df_pw['valid'] = df_pw.apply(lambda x:
    list(x.pw).count(x.letter) in range(x.low, x.high+1), axis=1)

print(f"There are {df_pw.valid.sum()} valid passwords.")

df_pw['pos1'] = df_pw.apply(lambda x: x.pw[x.low - 1], axis=1)
df_pw['pos2'] = df_pw.apply(lambda x: x.pw[x.high - 1], axis=1)

df_pw['valid_new'] = df_pw.apply(lambda x:
    (x.pos1 == x.letter) ^ (x.pos2 == x.letter), axis=1)

print(f"There are {df_pw.valid_new.sum()} valid passwords according to new interpretation.")

import pandas as pd

f = open(r"input.txt", "r")

passports_raw = []
pp = []
for line in f.readlines() + ['\n']:
    if line == '\n':
        passports_raw.append(pp)
        pp = []
        continue
    line = line.rstrip('\n')
    pp.append(line)

def passport_to_dict(pp:list):
    pp_dict = {}
    for x in pp:
        k, v = x.split(":")
        pp_dict[k] = v
    return pp_dict

passports_clean = []
for i in passports_raw:
    pp = []
    for j in i:
         pp = pp + j.split(" ")
    pp_dict = passport_to_dict(pp)
    passports_clean.append(pp_dict)

df_passports = pd.DataFrame(passports_clean)

def valid_check(row, columns:list):
    return all(row[columns].notnull())

column_check = ['hgt', 'pid', 'eyr', 'iyr', 'ecl', 'hcl', 'byr']
df_passports['valid'] = df_passports.apply(lambda x: valid_check(x, column_check), axis=1)

print(f"There are {df_passports.valid.sum()} valid passports.")

def valid_check_new(row):
    try:
        byr = (int(row.byr) >= 1920) and (int(row.byr) <= 2002)
        iyr = (int(row.iyr) >= 2010) and (int(row.iyr) <= 2020)
        eyr = (int(row.eyr) >= 2020) and (int(row.eyr) <= 2030)
        if 'cm' in str(row.hgt):
            hgt = (int(row.hgt.strip('cm')) >= 150) and (int(row.hgt.strip('cm')) <= 193)
        elif 'in' in str(row.hgt):
            hgt = (int(row.hgt.strip('in')) >= 59) and (int(row.hgt.strip('in')) <= 76)
        else: 
            hgt = False
        hcl = (str(row.hcl)[0] == '#') and (len(str(row.hcl)) == 7)
        ecl = row.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        pid = (len(row.pid) == 9) and int(row.pid)
        return all([byr, iyr, eyr, hgt, hcl, ecl, pid])
    except:
        return False

df_passports['valid_new'] = df_passports.apply(lambda x: valid_check_new(x), axis=1)

print(f"There are {df_passports.valid_new.sum()} valid passports according to the stricter policy.")
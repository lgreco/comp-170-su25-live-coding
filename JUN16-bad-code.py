
# Temperatures during week 1 of 2
mon1 = 75
tue1 = 77
wed1 = 68
thu1 = 65
fri1 = 71
sat1 = 78
sun1 = 73

# Temperatures during week 2 of 2
mon2 = 56
tue2 = 66
wed2 = 68
thu2 = 65
fri2 = 83
sat2 = 84
sun2 = 78

# Sum of temperatures during both weeks
sum = mon1 + tue1 + wed1 + thu1 + fri1 + sat1 + sun1 + mon2 + tue2 + wed2 + thu2 + fri2 + sat2 + sun2

# 14-day average
avg = sum/14

# Formatted report
print(f"\n\nThe average temperature is {avg:.1f}\n\n")
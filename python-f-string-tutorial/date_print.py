import datetime
today = datetime.datetime.today()

# printing date extracted from today object
print(f"{today:%Y-%m-%d}")
# output: 2022-04-07
print(f"{today:%Y}")
# output: 2022

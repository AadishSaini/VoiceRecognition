from datetime import date

date = str(date.today())
print(type(date))

with open(date, "w+") as f:
    f.write("Today's Notes - ")

print("Made the file")

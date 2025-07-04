def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

print(is_leap_year(2004))  # This will print True
print(is_leap_year(2000))  # Adding another example to test, this will print True
print(is_leap_year(1900))  # Adding another example to test, this will print False


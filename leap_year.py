# Objective- To check if a given year is leap year
# Rules for leap year- divisible by 4, should not be divisible by 100 unless also divisible by 400, divisible by 400
def leap_year(Given_year):
    if Given_year % 4 == 0:
        if Given_year % 100 == 0:
            if Given_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# True if its leap year
# False if its not
print(leap_year(2000))

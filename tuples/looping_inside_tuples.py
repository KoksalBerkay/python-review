countries = ('Belgium', 'Germany', 'France', 'Netherland',
             'Poland', 'Bolivia', 'Brazil', 'Burgendia')

# Hint
# 1. Use for loop inside tuple
# 2. use slice [:] or index

countries_b = []
# loop inside tuple
for country in countries:

    # find first letter of each counrty
    first_letter = country[0]

    # Compare first_letter if it is 'B'
    if first_letter == 'B':
        # then push country to the list
        countries_b.append(country)

country = input(">")
country2capital = {'Singapore': 'Singapore',
                   'USA': 'Washington D. C.',
                   'UK': 'London',
                   'China': 'Beijing',
                   'Israel': 'Jerusalem',
                   'Mexico': 'Mexico De F. Mexico'
                   }
capital = country2capital.get(country, "unknown")
print("The capital of {0} is {1}".format(country, capital))
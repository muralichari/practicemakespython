people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
 {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'},
 {'first':'Barack', 'last':'Obama', 'email':'president@whitehouse.gov'}
 ]

lastnames = []
lastnames_x = {}
for i in people:
  lastnames.append(i['last'])
  lastnames_x[i['last']] = [i['first'], i['email']]
'''
print('After sorting')
print(lastnames)
'''

for i in lastnames:
    print(i +', ' + ": ".join(lastnames_x[i]))


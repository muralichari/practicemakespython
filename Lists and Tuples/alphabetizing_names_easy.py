people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
 {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'},
 {'first':'Barack', 'last':'Obama', 'email':'president@whitehouse.gov'}
 ]


for person in sorted(people, key=lambda person:  [person['last'], person['first']]):
 print(f"{person['last']}, {person['first']}: {person['email']}")

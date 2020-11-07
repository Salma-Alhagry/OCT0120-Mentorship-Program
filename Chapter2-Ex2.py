print("(1) The volume of a sphere with radius r is 4/3πr3. What is the volume of asphere with radius 5?")
r = 5 
radius = (4/3)*3.14*r**3
print('The volume of a sphere is ' ,radius)
print('-------------------------------------------------')

print('Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?')
bookpp = 24.95
discount = 0.40
dispp1 = 24.95*0.40
dispp2 = 24.95 - dispp1
print('The discount price of book after 40% is ', dispp2)
dispp = dispp2*60
shipping = 3
addcopy = 59*0.75
total_wholesalepp = dispp+shipping+addcopy
print('The total wholesale cost for 60 copies is,total_wholesalepp')
print('-----------------------------------------------')
print('(3) If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 permile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, whattime do I get home for breakfast?')
x=(6*60+52)*60
y = (8*60+15)*2
z= (7*60+12)*3
hour = (x+y+z)/(60*60)
reminder = (x+y+z)//(60*60)
minutes = (hour-reminder)*60
reminder = int(reminder)
minutes = int(minutes)
print('I will get home at',reminder,':',minutes,"AM.")





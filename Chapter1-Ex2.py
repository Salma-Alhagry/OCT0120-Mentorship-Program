print("1. How many seconds are there in 42 minutes 42 seconds \n ",(42*60)+42 )
print('---------------------------------------------------')

print("2. How many miles are there in 10 kilometers? ")
miles=(10/1.61)
miles=round(miles, 2)
print (str(miles) + " miles")
print('---------------------------------------------------')
      

print("If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)?What is your average speed in miles per hour?")


averagePaceMin=((42/60+42)//(10/1.61))

averagePaceSec=(((42*60+42)//(10/1.61))-int(averagePaceMin)*60)

print("average pace" + str(averagePaceMin) + " minutes "+str(averagePaceSec) + " seconds")
averageSpeed=(10/1.61)/(42/60+42/60/60)
value= round(averageSpeed, 2)

print("average speed " + str(averageSpeed) + " miles / hours")


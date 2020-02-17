# moonMass = 33
# everyYear = 2 #pounds converted from kilo
# newYear = moonMass

# for x in range(1, 16):
#     newYear = newYear + everyYear 
#     print('My moon weight each year will be %s pounds on year %s' % (newYear, x))




earth_now = int(input("your weight now: "))
moon_now = earth_now * 0.165
print(moon_now) 
for i in range(1,16):
    earth_now +=1
    moon_now = earth_now * 0.165
print(moon_now) 
    

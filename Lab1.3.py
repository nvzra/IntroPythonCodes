#Seconds to Hours
#Aimen Ahmed
#01292019

seconds = input("Enter time in seconds for conversion: ")
hr = int(seconds)//3600
min = int(seconds)% 3600//60
sec= int(seconds)% 3600% 60
print(str(seconds) + " seconds = " + str(hr) + " hours " + str(min) + " minutes " + str(sec) + " seconds ")

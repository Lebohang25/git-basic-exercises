def convert_time(x):
    
    hours = int(x // 60)
    mins  = int( x % 60)
    
    print(str(hours) + " hour and " + str(mins) + " minutes.")

convert_time(100)

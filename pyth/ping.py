import os, platform
hostname = "google.com" #example


#and then check the response...
if os.name == 'nt':
    response = os.system("ping -n 2 " + hostname)
    if response == 0:
        print (hostname,'is up!')
    else:
        print (hostname, 'is down!')

if os.name != 'nt':
    response = os.system("ping -c 2 " + hostname)
    if response == 0:
        print (hostname,"is up! ")
        print ("You are on ",platform.system('150.150.150.231'))
    else:
        print (hostname, "is down!")

import speedtest
s=speedtest.Speedtest()
print("What do you want to Test:\n1) Upload Speed\n2) Download Speed\n3) Ping\n")
option=int(input("Input:"))
if option==1:
    speed=str(s.upload())
    print("Upload Speed: {0} Mb/Sec".format(speed[:2]+"."+speed[9:11]))
elif option==2:
    speed=str(s.download())
    print("Download Speed: {0} Mb/Sec".format(speed[:2]+"."+speed[9:11]))
elif option==3:
    server=[]
    s.get_servers(server)
    print("Ping: {0}ms".format(s.results.ping))
else:
    print("Invalid Option")

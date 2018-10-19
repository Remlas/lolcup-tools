LolDir = "C:/Program Files/Riot Games/League of Legends/"



lockfile = open(LolDir + "lockfile", "r") #Open 'lockfile' inside LoL Directory as read-only

for line in lockfile: 
    fields = line.split(":")    #Split fields seperated by ":" in lockfile to array
    ClientPort = fields[2]      #Port number is 3rd information in lockfile
    ClientPass = fields[3]      #and Password is 4th

lockfile.close()                #Make memory FREE! :D 
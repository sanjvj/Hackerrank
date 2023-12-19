s = "12:40:03PM"


hour = s[0:2]
hourtimeinPM = int(hour)
hourtimeinAM = hour

for i in s[-2]:
    if i == "P":
       hourtimeinPM += 12
       if hourtimeinPM==24:
           hourtimeinPM = "12"
       word = str(hourtimeinPM)
       print(word+ s[2:-2])
    
    else:
       hour
       
       hourtimeinAM = int(hour)
       if hourtimeinAM == 12:
           hourtimeinAM = "00"
           word = str(hourtimeinAM)
           print(word+ s[2:-2])
       else:
           print(hour+s[2:-2])
       
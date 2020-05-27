from clockwork import clockwork
import time
 
api = clockwork.API("0a5b9f809d353f0404525a6a7a116909178991cb")
 
lyrics = open("lyrics.txt", "r").readlines()
 
for line in lyrics:
    payload = line.replace("\n", "")
    message = clockwork.SMS(from_name = "MICHHI PUTTU", to = "917754915707", message = payload)
    response = api.send(message)
    print(response)
    time.sleep(300)
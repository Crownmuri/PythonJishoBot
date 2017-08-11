### The only import you need!
import socket, requests, json

### Options (Don't edit)
SERVER = "irc.twitch.tv"  # server
PORT = 6667  # port
### Options (Edit this)
PASS = "oauth:"  # bot password can be found on https://twitchapps.com/tmi/
BOT = "bot"  # Bot name [NO CAPITALS]
CHANNEL = "channel"  # Channel name [NO CAPITALS]

### Functions

def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode())

def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user
def getMessage(line):
    global message
    try:
        message = (line.split(":", 2))[2]
    except:
        message = ""
    return message
def joinchat():
    readbuffer_join = "".encode()
    Loading = True
    while Loading:
        readbuffer_join = s.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        temp = readbuffer_join.split("\n")
        readbuffer_join = readbuffer_join.encode()
        readbuffer_join = temp.pop()
        for line in temp:
            Loading = loadingCompleted(line)
###    sendMessage(s, "Chat room joined!")
    print("Bot has joined " + CHANNEL + "'s Channel!")

def loadingCompleted(line):
    if ("End of /NAMES list" in line):
        return False
    else:
        return True
### Code runs
s_prep = socket.socket()
s_prep.connect((SERVER, PORT))
s_prep.send(("PASS " + PASS + "\r\n").encode())
s_prep.send(("NICK " + BOT + "\r\n").encode())
s_prep.send(("JOIN #" + CHANNEL + "\r\n").encode())
s = s_prep
joinchat()
readbuffer = ""

def Console(line):
    # gets if it is a user or twitch server
    if "PRIVMSG" in line:
        return False
    else:
        return True

def jisho(keyword):

    data = json.loads(requests.get(
            "http://jisho.org/api/v1/search/words?keyword=%s" % keyword).text)

    results = {}
    if len(data["data"]) == 0:
        return("No results... (´・ω・｀)")
    else:
        for result in range(len(data["data"])):
            results[result] = {"words": [], "readings": [], "senses": {}}

            for a in range(len(data["data"][result]["japanese"])):
            

                if "reading" in data["data"][result]["japanese"][a]:
                    if (data["data"][result]["japanese"][a]["reading"] not in results[result]["readings"]):
                        results[result]["readings"].append(data["data"][result]["japanese"][a]["reading"])
                if "word" in data["data"][result]["japanese"][a]:
                    if (data["data"][result]["japanese"][a]["word"] not in results[result]["words"]):
                        results[result]["words"].append(data["data"][result]["japanese"][a]["word"])

            for b in range(len(data["data"][result]["senses"])):
                results[result]["senses"][b] = \
                    {"english": [], "parts": []}

                for c in range(len(data["data"][result]["senses"][b]["english_definitions"])):
                    results[result]["senses"][b]["english"].append(
                        data["data"][result]["senses"][b]["english_definitions"][c])

                for d in range(len(data["data"][result]["senses"][b]["parts_of_speech"])):
                    results[result]["senses"][b]["parts"].append(
                        data["data"][result]["senses"][b]["parts_of_speech"][d])

    kanji = "、".join(str(i) for i in results[0]["words"])
    yomi = "、 ".join(str(i) for i in results[0]["readings"])
    katachi = ", ".join(str(i) for i in results[0]["senses"][0]["parts"])
    imi = ", ".join(str(i) for i in results[0]["senses"][0]["english"])    
#    imi =",".join(str(i) for i in results[0]["senses"])
#    print(results[0])
    return(kanji + " (" + yomi + ")" + " [" + katachi + "]: " + imi)


while True:
        try:
            readbuffer = s.recv(1024)
            readbuffer = readbuffer.decode()
            temp = readbuffer.split("\n")
            readbuffer = readbuffer.encode()
            readbuffer = temp.pop()
        except:
            temp = ""
        for line in temp:
            if line == "":
                break
            # So twitch doesn't timeout the bot.
            if "PING" in line and Console(line):
                msgg = "PONG tmi.twitch.tv\r\n".encode()
                s.send(msgg)
                print(msgg)
                break
            # get user
            user = getUser(line)
            # get message send by user
            message = getMessage(line)
            # for you to see the chat from CMD
            print(user + " > " + message)
            # sends private msg to the user (start line)
            PMSG = "/w " + user + " "

################################# Command ##################################
############ Here you can add as many commands as you wish of ! ############
############################################################################

            if  message.startswith("!jisho "):
                sendMessage(s, jisho(message.split(' ')[1]))
                break
            if  message.startswith("!j "):
                sendMessage(s, jisho(message.split(' ')[1]))
                break
############################################################################

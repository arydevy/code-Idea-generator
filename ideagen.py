import random
import os

languages=[
	"WebSite",
	"Bot",
	"Bridge",
	"Ai",
	"Game"
];

os.system("clear")
print("================IDEA GENERATOR==================")
for i in range(len(languages)):
    print(f"{i}.  {languages[i]}")
print("================================================")

id=int(input("Please chose a category by writing the number before it\n $ "))
times=int(input("How much ideas to generate? \n $"))
timeLimit=input("Do You Want A Time Limit?(y/n) \n $")
if timeLimit.upper()=="Y":timeLimit=True
elif timeLimit.upper()=="N":timeLimit=False
else :print("A Error Ocurred :( !")
os.system("exit")




#=========DATA==========#
Time=[
    "24Hours",
    "48Hours",
    "1 Week",
    "1 Month",
    "1Hour",
    "10Hours",
    str(999%5/100)+" Years"
]
#=========WEBDEV========#
website1=[
	"link shortener",
	"blog",
	"e-comerce",
	"portofolio",
    "Food delivery"
]
websiteType=[
	"simple",
	"colorfull",
	"black and white",
	"amazing",

]
websiteFor=[
	"Coffee",
	"Freelancers",
	"a Country",
	"Plannet"
]

# bot
botPatform=[
    "Discord",
    "Telegram",
    "Matrix.org",
    "Skype",
    "Web",
    "Twitter",
    "Mastadon",
    "Facebook",
    "Reddit"
]
botType=[
    "News",
    "Gambling",
    "RolePlay",
    "Economy",
    "Game",
    "Ranks",
    "Documentation"
]

# bridge
Bplatform=[
    "SmS",
    "Call",
    "Discord",
    "Telegram",
    "Website",
    "IRC",
    "Stack",
    "Youtube Feed",
    "Blog Feed",
    "Steam Chat",
    "WhatsApp",
    "LINE",
    "BBM",
    "FacebookMessenger",
    "Signal"
]

#AI
aiType=[
    "Chatbot",
    "ComputerVision",
    "Recognision",
    "Spam Filter",
    "Recomandation",
    "Translation"
]

#Game
genere=[
    "Action",
    "Aventure",
    "Exploratin",
    "Building",
    "Sandbox",
    "Shooting",
    "Educational"
]



# GENERATOR

def gen(id):
    #website
    if id == 0:
        timeL=random.choice(Time)
        wtype=random.choice(websiteType)
        b=random.choice(website1)
        wfor=random.choice(websiteFor)
        if timeLimit:
            return f"Code a {wtype} {b} website for {wfor}" + f" in {timeL}"
        else: return f"Code a {wtype} {b} website for {wfor}"
    
    #bot
    elif id==1:
        timeL=random.choice(Time)
        platform=random.choice(botPatform)
        btype=random.choice(botType)
        if timeLimit:
            return f"Code a {platform} {btype} Bot!" + f" in {timeL}"
        else: return f"Code a {platform} {btype} Bot!"
    
    #bridge
    elif id==2:
        timeL=random.choice(Time)
        platform1=random.choice(Bplatform)
        platform2=random.choice(Bplatform)
        if timeLimit:
            return f"Code a {platform1} To {platform2} Bridge!" + f" in {timeL}"
        else: return f"Code a {platform1} To {platform2} Bridge!"

    
    #AI
    elif id==4:
        timeL=random.choice(Time)
        AI=random.choice(aiType)
        if timeLimit:
            return f"Code a {AI} AI!" + f" in {timeL}"
        else: return f"Code a {AI} AI!"
    
    else: print("Unrecognized id!")

os.system("clear")

print("================IDEA GENERATOR==================")
print(F"Type: {languages[id]}")
print(f"Number of ideas: {times}")
print(f"Time Limit: {timeLimit}")
for i in range(times):
    print(gen(id))
print("================================================")
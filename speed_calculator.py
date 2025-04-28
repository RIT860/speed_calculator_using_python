from time import *
import random as r

def mistake(partest,usertest,time_s,time_e):
    partest = partest.split()  # Split the correct text into words
    usertest = usertest.split()  # Split the user's input into words
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1

        except :
            error = error + 1   

    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2) #time_R is the time taken by user to type the text in seconds || 2 is argument for round function
    if time_R == 0: #if user take 0 sec to type the text then speed is 0
        return 0
    elif time_R < 0: #if user take negative time to type the text then speed is 0
        return 0
    elif time_R > 0: #if user take positive time to type the text then speed is calculated
        pass
    
    word_count = len(userinput.split())#count the number of words
    speed = (word_count/time_R) * 60
    return round(speed,2) #Rounded to 2 decimal places    

if __name__ == '__main__':
    while True:
        check = input("Ready to test Yes / No : ")
        if check == "Yes":

            test = [
                    "asdf ;lkj asdf ;lkj asdf ;lkj asdf ;lkj asdf ;lkj asdf ;lkj asdf ;lkj asdf ;lkj",
                    "all ass ask add has had sad lad kad las gas glass jag fad dad dalda fall glad flags halda dash flash",
                    "qwert poiuy qwert poiuy qwert poiuy qwert poiuy qwert poiuy qwert poiuy qwert",
                    "sea fee see try hit writ rat hat lot did all kid oil pot toy eat tea test sit fill pat are out ark life pity said tail trial easy right hight white large route early",
                    "hand small chest very hen pen time around hangs lazy son net upon rights woman moral bird men habit powers borrow narrow catch van earns school college village certain curtain zebra cutter require",
                    "The quick brown fox jumps upon right over a lazy dog.",
                    "12345 09876 12345 98760 12345 98760 12345 98760 12345 98760 12345 98760",
                    "A paragraph is a self-contained unit of discourse in write",
                    "my name is Ritesh kumar and i have curntly studing in Gp Barauni,Begusarai",
                    "Welcome to T.C. Solution website",
                    "The quick brown fox jumps upon right over a lazy dog.",
                    "We live in a world filled with insects. When you play or work outside, it is easy to get bitten or stung. Bees, fire ants, and ticks are some of the most common types of biting and stinging insects.",
                    "Scientists Can See Better With Hubble Than With Any Telescope On The Ground Because Hubble Travels Above The Atmosphere. On Earth, The Atmosphere Make Pictures Taken By Visible-Light Telescopes Look Smeary Clouds, Precipitation, And Atmospheric Temperature Changes Get In The Way.",
                    "When you go on picnics, cover the food. Soda and cake attract bees. Don't drink from open cans. Yellow jackets like to climb inside the cans and will sting from there.",
                    "Baseball Has Been The National Pastime In The United States Since The Middle Of The 1800s. Each Period Has Had A Unique Flavor, And It Is Sometimes Useful To Read About A Period From The Perspective Of The Time In Which It Took Place.",
                    "This write-up on the National symbols of India contains brief information on various national symbols of India. It also traces the history and evolution of various Indian National symbols. "

                    ]
            
            test1 = r.choice(test)
            print("         ***** Typing speed ******")
            print(test1,"\n\n")
            time_1 = time()
            testinput = input(" Enter : ")
            time_2 = time()
            print("Speed : ",speed_time(time_1,time_2,testinput)," WPM")
            print("Total type Mistake word : ",mistake(test1,testinput,time_1,time_2))
        
        elif check == "No":
            print("Thank you")
            break
        
        else:
            print("!nvaled value!")
            continue
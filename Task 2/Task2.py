
#print the title for this program 
print("Park Run Timer")
print("~~~~~~~~~~~~~~\n\n")
print("Let's go!")
#creating a function which take all necessary parameters to complete this problem
def run_man():
    """This function processes input data of marathon runner names and times and outputs statistics on the number of runners,
    average time, slowest time, fastest time, and name of the runner with the fastest time."""
    #create a two  empty lists which store the input runner_time and runner_person
    runner_time = []
    runner_person = []
    print("Don't Enter runner name twice")
    #Start a infinite loop 
    while True:
        #take a input from a user
        reading = input(">")
        #check the input and evulate
        if reading == "End" or reading == "end" or reading == "END":
            #terminate the loop 
            break
        try:
            #assign  a value in two varaible as split by ::
            runner, new_reading = reading.split("::")
            #check whether the runner is blank or not
            if (runner == ""):

                print("Error in data stream. Ignorning. Carry on.")
                #continue the loop
                continue
            
            #changing new_reading into integer
            new_reading = int(new_reading)
            if (new_reading<0):
                print("Error in data stream. Ignorning. Carry on.")
                continue
            #This will append the data in empty list 
            runner_person.append(runner)
            runner_time.append(new_reading)
   #this will only run if the user input invalid format 
        except ValueError:
            print("Error in data stream. Ignorning. Carry on.")
            #continue the loop 
            continue
#assigning the lenthof list in varaible 
    no_of_readings = len(runner_time)
    #check the condition whether given varaible is 0 or not 
    if (no_of_readings == 0):
        print("No data found. Nothing to do. What a pity.")
    else:
        #using the string formatting to assign the value in particular varaible 
        print((f"Total Runner:{no_of_readings}") if (
            no_of_readings == 1) else (f"Total Runner:{no_of_readings}"))
# check the condtion within the len 
    if (len(runner_time) != 0):
        #calculate the Average of given number in list 
        average = sum(runner_time)/len(runner_time)
        #gives output of Average
        print("Average:", time(average))
        #calculate the max_value from the list(runner_time) using max method
        max_value = max(runner_time)
        #gives the output of Slowest Time runner time 
        print("Slowest Time:", time(max_value))
        #calculate the min_value from the list(runner_time) using min method
        min_value = min(runner_time)
        #display the output of Fastest Time of player running 
        print("Fastest Time:", time(min_value))
       #calculate the best runner in the list
        best_runner = runner_person[runner_time.index(min(runner_time))]
        print("Best Time Here:Runner", "#", best_runner)


def time(inputtime):
    """This function convert time into minutes and seconds """
    #check the condition whether input time is equal to 60 or greater than 60 or less than 60  and disaplay the output in satisfied conditon 
    if (inputtime == 60):
        return "1 Minute"
    elif (inputtime > 60):
        if (inputtime//60 == 1):
            return " 1 Minute " + str(int(inputtime % 60)) + " Seconds "
        else:
            return str(inputtime//60)+  " Minutes  " +  str(int(inputtime % 60)) + " Seconds"
    else:
        return "0.0 Minute "+str(int(inputtime)) + " Seconds"


run_man()

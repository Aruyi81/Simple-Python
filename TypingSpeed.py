from time import time  # to record the time

# now to calculate the accuracy of input prompt
def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords) - 1):
            if inwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if inwords[i] == words[i]:
                if (inwords[i + 1]) and (inwords[i - 1] == words[i - 1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors  # Corrected indentation

# now to calculate the speed of typing words per minute
def speed(inprompt, elapsed_time):
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = (twords / elapsed_time) * 60  # Convert to words per minute

    return speed

# calculate the total elapsed time
def elapsedtime(stime, etime):
    return etime - stime  # 'etime' is the end time and 'stime' is the start time

if __name__ == '__main__':
    prompt = "Red wine and sleeping pills, help me get back to your arms..."

    # this is the paragraph which we have to type to check our speed
    print("Type this:- ", prompt, " ")

    # checking to input Enter basically it will see
    input("Press Enter when you are ready to check your speed!!!")

    # recording time for input
    stime = time()
    inprompt = input()
    etime = time()

    # collect all the information returned by the functions
    elapsed_time = round(elapsedtime(stime, etime), 2)  # round off the time
    typing_speed = speed(inprompt, elapsed_time)
    errors = tperror(prompt)

    # printing all the required data to see result
    print("Total time elapsed:", elapsed_time, "seconds")
    print("Your Average Typing speed was", typing_speed, "words per minute (w/m)")
    print("With the total of", errors, "errors")
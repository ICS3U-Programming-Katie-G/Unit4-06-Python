#!/usr/bin/env python3
# Created by: Katie G
# Created on: December 5th, 2022
# This program will list every value of RGB.
# The program uses 3 nested FOR... loops
# to accomplish this task.


# this function will display all of the respective R, G and B
# values respectively using 3 nested FOR... loops.
def main():
    # tell the user to look at all the RGB values
    # that are about to be printed.
    print("I really like RGB values! Look at all these colors :)")

    # initializing the three counters.
    counter1 = 0
    counter2 = 0
    counter3 = 0
    # first FOR... loop, containing the counter
    # for the first value in RGB, R.
    for counter1 in range(0, 256):
        for counter2 in range(0, 256):
            for counter3 in range(0, 256):
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        str(counter1),
                        str(counter2),
                        str(counter3),
                        "RGB("
                        + str(counter1)
                        + ","
                        + str(counter2)
                        + ","
                        + str(counter3)
                        + ")",
                    )
                )


if __name__ == "__main__":
    main()

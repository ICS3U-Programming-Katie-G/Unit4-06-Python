#!/usr/bin/env python3
# Created by: Katie G
# Created on: December 5th, 2022
# This program will list every value of RGB.
# The program uses 3 nested while... loops
# to accomplish this task.


# this function will display all of the respective R, G and B
# values respectively using 3 nested while... loops.
def main():
    # tell the user to look at all the RGB values
    # that are about to be printed.
    print("I really like RGB values! Look at all these colors :)")

    # initializing the three counters. counter1 represents red,
    # counter2 represents green, and counter3 represents blue.
    counter1 = 0
    counter2 = 0
    counter3 = 0
    # first while... loop, containing the counter
    # for the first value in RGB, R / red.
    while counter1 <= 255:
        # got the RGB color printer format thing from carolyn because
        # i did not understand how to format it right
        # thank you carolyn i love you
        print(
            "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                str(counter1),
                str(counter2),
                str(counter3),
                " " + str(counter1) + ", " + str(counter2) + ", " + str(counter3) + " ",
            )
        )
        if counter2 and counter3 == 255:
            counter1 = counter1 + 1
        # second while...loop, containing the counter
        # for the second value in RGB, G / green.
        while counter2 < 255:
            # once again, got the RGB color printer format thing
            # from carolyn because
            # i did not understand how to format it right
            # thank you carolyn i love you
            print(
                "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                    str(counter1),
                    str(counter2),
                    str(counter3),
                    " "
                    + str(counter1)
                    + ", "
                    + str(counter2)
                    + ", "
                    + str(counter3)
                    + " ",
                )
            )
            if counter3 == 255:
                counter2 = counter2 + 1
            # third while...loop, containing the counter
            # for the third value in RGB, B / blue.
            while counter3 < 255:
                # and again, got the RGB color printer format thing
                # from carolyn because
                # i did not understand how to format it right
                # thank you carolyn i still love you
                # from the last time I said it :)
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        str(counter1),
                        str(counter2),
                        str(counter3),
                        " "
                        + str(counter1)
                        + ", "
                        + str(counter2)
                        + ", "
                        + str(counter3)
                        + " ",
                    )
                )
                counter3 = counter3 + 1


if __name__ == "__main__":
    main()

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # size
    if not (2 <= len(s) <= 6):
        return False

    # first 2 characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # just letters and numbers
    if not s.isalnum():
        return False

    # numbers in the end
    number_started = False

    for c in s:
        if c.isdigit():

            # first number can't be 0
            if not number_started:
                if c == "0":
                    return False
                number_started = True

        else: 
            if number_started:   
                return False

    return True


main()

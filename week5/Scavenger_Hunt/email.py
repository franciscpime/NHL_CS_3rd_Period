def main() -> None:
    email = input("Enter ur email: ")

    if is_valid_email(email):
        print("Nice")
    else:
        print("Bad")
 

def is_valid_email(email: str) -> bool:
    if email.count("@") != 1:
        return False

    part1, part2 = email.split("@")

    if len(part1) < 1 or len(part2) < 1:
        return False

    if "." not in part2:
        return False
    
    return True


if __name__ == "__main__":
    main()
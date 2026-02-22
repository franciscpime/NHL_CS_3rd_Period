from flask import Flask, render_template, request

from cs50 import SQL

app = Flask(__name__)

# Connect the application to the SQLite database file plates.db
db = SQL("sqlite:///plates.db")


def is_valid(s):

    # Plate must have between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Plate can only contain letters and numbers 
    if not s.isalnum():
        return False

    # Flag to track when the number sequence begins
    number_started = False

    # Loop through every character in the plate
    for c in s:

        # If the character is a digit
        if c.isdigit():

            # If this is the first digit found
            if not number_started:

                # The first digit cannot be 0
                if c == "0":
                    return False

                # Mark that numbers have started
                number_started = True

        else:
            # If we already started numbers and now see a letter >> invalid
            if number_started:
                return False

    return True


@app.route("/", methods=["GET", "POST"])
def index():

    # If the user submitted the form
    if request.method == "POST":

        # Get the plate value typed in the input field named "plate"
        plate = request.form.get("plate")

        # Check if the plate is valid using our function
        valid = is_valid(plate)

        # Insert the result into the database
        db.execute(
            "INSERT INTO plates (plate, valid) VALUES (?, ?)",
            plate,
            1 if valid else 0                                       # 1 = valid  0 = invalid
        )

        # Reload page showing the result
        return render_template("index.html", result=valid, plate=plate)

    # If user just opened the page (GET request), show empty form
    return render_template("index.html")


@app.route("/history")
def history():

    # Get all previous checks ordered from newest to oldest
    plates = db.execute("SELECT * FROM plates ORDER BY id DESC")

    # Send the list to the HTML page
    return render_template("history.html", plates=plates)


if __name__ == "__main__":
    app.run(debug=True)

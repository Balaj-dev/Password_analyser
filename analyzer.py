from flask import Flask , render_template , request
import csv

def check_passwords(password_of_user):
    with open("common_passwords.txt", "r") as file:
        reader = csv.reader(file)
        # Flatten the list: csv.reader returns list of rows, we only have one row
        passwords = [p.strip() for p in next(reader) if p.strip()]
        has_digit = any(c.isdigit() for c in password_of_user)
        has_symbol = any(not c.isalnum() for c in password_of_user)
        length_of_password = len(password_of_user)
        # Check length first
        if length_of_password < 8:
            return "Password must be at least 8 characters long."

        # Check symbol + number
        if not has_digit or not has_symbol:
            return "Password must contain at least one number and one symbol."

        # Check if password is in common list
        if password_of_user in passwords:
            return f"Your password '{password_of_user}' is too common. Consider changing it."
        else:
            return "Your password is strong."


app = Flask(__name__)
@app.route("/", methods=["GET" , "POST"])
def main_page():
    result = ''
    if request.method == "POST":
        password_of_user = request.form.get("password")
        result =  check_passwords(password_of_user)
    return render_template("index.html" , result=result)


if __name__ == "__main__":
    app.run(debug=True)


# Password Analyzer

A lightweight, local-only Flask web application that evaluates password strength using simple rule-based validation.  
The analyzer checks password length, character requirements, and verifies whether the password appears in a blacklist of common passwords.

---

## Features

### 1. Length Validation
The password must be at least **8 characters** long.

### 2. Complexity Requirements
The password must contain:
- At least one digit  
- At least one symbol (any non-alphanumeric character)

### 3. Common Password Detection
The application loads a list of common or weak passwords from `common_passwords.txt`.  
If the submitted password exists in this list, it is classified as insecure.

### 4. Local Web Interface
The tool runs on `localhost` using Flask and processes passwords through a POST form submission.

---

## How It Works

The core logic resides in the `check_passwords()` function.

1. Reads `common_passwords.txt` using Python's `csv` module.  
2. Flattens the CSV row into a list of common passwords.  
3. Performs the following checks:
   - Minimum length requirement  
   - Presence of at least one digit  
   - Presence of at least one symbol  
4. Compares the password with the blacklist.  
5. Returns a clear textual response:
   - `"Password must be at least 8 characters long."`
   - `"Password must contain at least one number and one symbol."`
   - `"Your password 'example' is too common. Consider changing it."`
   - `"Your password is strong."`

The Flask route `/` renders `index.html`, which accepts user input and displays the validation result.

---

## Project Structure

```commandline
Password_analyser/
├── analyzer.py # Main Flask application and password checking logic
├── common_passwords.txt # List of common passwords (CSV format, single row)
├── templates/
│ └── index.html # HTML template for the UI
├── static/ # Static assets (optional)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```


---

## Installation

### Requirements
- Python 3.8+
- pip package manager

### Steps (All Platforms)

```bash
# Clone the repository
git clone https://github.com/Balaj-dev/Password_analyser.git
cd Password_analyser

# Optional but recommended: create virtual environment
python -m venv .venv
# Activate (Windows)
.\.venv\Scripts\activate
# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python analyzer.py
```
## Output via
 Once running, open your browser and visit:
 http://localhost:5000/

## Usage
Submit any password through the form displayed on the main page.
The application will return one of the predefined validation messages based on the rules implemented.
Security Notes
This tool is intended for local use only.
Do not expose it to the internet without proper security measures.
Avoid logging or storing raw passwords.
## License
This project is licensed under the MIT License.
You are free to modify and distribute the project with proper attribution.
## Contributing
Pull requests and improvements are welcome.
Please ensure modifications remain aligned with the project's simple and local-only design.

---

If you want, I can also create:

- A **professional LICENSE file**  
- A **GitHub description + tags**  
- A **badges section** (Python version, license, last commit, etc.)  

Let me know by opening an issue.
# Password_analyser

> A simple web-based password analyzer that checks if a password is too common or easy to brute-force.  

## What it does

Password_analyser helps you **assess whether a given password is weak or risky**. It checks your password against a list of common passwords and provides feedback when a password is found to be too common or easily guessable.  

Use Cases:

- Quickly check if a chosen password is “safe enough.”  
- Avoid using common / easy-to-guess passwords.  
- Integrate as a local web-tool (localhost) for testing passwords before using them for real accounts.  

## How it works (brief technical explanation)

- The core logic lives in `analyzer.py`, which reads a list of common passwords from `common_passwords.txt`.  
- When you submit a password (via the web interface), the backend checks whether the password matches any in the common list.  
- Optionally, the script could be extended to include more checks (length, complexity, entropy, dictionary-checks, etc.).  
- A minimal web interface (using a web framework) allows you to input a password via GET or POST requests, and receive feedback.  

## Project structure

Password_analyser/
├── analyzer.py # Main logic for password checking
├── common_passwords.txt # List of common/password-blacklist entries
├── requirements.txt # Python dependencies
├── templates/ # HTML templates for the web interface
├── static/ # Static assets (CSS/JS) if any
├── LICENSE # MIT license
└── README.md # This file


## Installation & Running (all platforms: macOS, Linux, Windows)

### Prerequisites

- Python 3.x installed  
- `pip` (Python package manager) available  

### Setup & Run

```bash
# 1. Clone the repository  
git clone https://github.com/Balaj-dev/Password_analyser.git  
cd Password_analyser  

# 2. Install dependencies  
pip install -r requirements.txt        # Or 'pip3 install -r requirements.txt'  

# 3. Run the analyzer (web server)  
python analyzer.py                     # Or 'python3 analyzer.py' depending on your system  
```



## Accessing via Web (localhost)
Once the server is running, open your browser and go to:
 http://localhost:5000/

(Port may vary depending on the server config — check output in console when you run it.)

Then you can submit a password via the web-form. The tool will respond with whether the password is common/easily guessable or not.
(Optional) Using via HTTP API (GET / POST)
You can also call the analyzer programmatically via HTTP:
GET — pass the password in query parameters.
POST — send password data via request body (e.g. form or JSON).
This allows integration into other tools or scripts.
Why this project
Helps enforce good password hygiene.
Useful for developers, pentesters, sysadmins to quickly check password strength / commonness.
Easy to run locally — no need to expose users’ passwords to external services.
License
This project is released under the MIT License.
Contributing & Feedback

## FeedBack
If you want to improve the tool (e.g. add complexity checks, entropy scoring, blacklist updates), feel free to submit issues or pull requests.
Also welcome: improvements to UI, more robust password-handling, better feedback / reporting.
---

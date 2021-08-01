# Google Sheets Manipulation

## Techs
- [Python](https://www.python.org/)
- [Google Cloud Platform](https://cloud.google.com/)
- [gspread](https://docs.gspread.org/en/v3.7.0/)

## Setting up

First, get a clone of the project to your local machine and `cd` into it.

```
git clone https://github.com/JoaoP12/Google-Sheets-Manipulation.git
cd ./Google-Sheets-Manipulation
```

Before going ahead, it is needed to get Google Drive and Google Sheets' API credentials. So follow the steps below to get it done:
- Log in to your Google account and go to [Google Cloud Platform website](https://cloud.google.com/).
- Go to the Console.
- In the menu, select "APIs & Services" -> Library.
- Search and enable Google Drive and Google Sheets' APIs.
- In the menu, select "APIs & Services" -> Credentials.
- Click the "+ Create Credentials" button.
- Give your account a name.
- Go back to the Credentials screen.
- In the "Service Accounts" area, click at the newly created account's email.
- Create a new key in the json format.
- Save it in the project's directory with the name "service_account.json".

## Usage
This program was made to run with [this sheet](https://docs.google.com/spreadsheets/d/18PYR23BS3XzmLdQCOPGwJPOPmk5AcNSLIyMMEZbB1RA/), so you can run it in the terminal with ```python ./main.py``` (assuming that you are already in the projects' directory in your terminal).

You can change the code as you wish. The original program will take students' grades and will define their situation between: APPROVED, FINAL EXAM, FAILED BY ABSENCE and FAILED BY GRADES, then the sheet will be updated with their situation and the grade needed to pass the final exam, in case the student's situation is FINAL EXAM.
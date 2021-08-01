import gspread
from google.oauth2.service_account import Credentials
from math import ceil
from situation import Situation, situation_strings

def authenticate(acc_credentials, scopes):
    print("Authenticating access to the API")
    credentials = Credentials.from_service_account_file(acc_credentials, scopes=scopes)
    return gspread.authorize(credentials)

def get_sheet(sheet_key, acc_credentials='credentials.json', scopes=[]):
    gc = authenticate(acc_credentials, scopes)
    sheet = gc.open_by_key(sheet_key)
    print("Getting worksheet")
    worksheet = sheet.worksheet("engenharia_de_software") 
    return worksheet

def student_has_failed_by_absence(total_classes, num_missed):
    return (ceil(total_classes/4)) < num_missed

def calculate_naf(avg_grade):
    '''
        naf must fit the inequation 5 <= (m + naf)/2 
        In this case, the program is computing 50 istead of five because the grades filled in the worksheet are from
        0 to 100 and not from 0 to 10.
        So the formula is 50 <= (m + naf)/2.
    '''
    return ceil(100-avg_grade)

def define_student_situation(avg_grade, total_classes, num_missed):
    if student_has_failed_by_absence(total_classes, num_missed):
        return Situation.FAILED_BY_ABSENCE
    if 50 <= avg_grade < 70:
        return Situation.FINAL_EXAM
    if avg_grade < 50:
        return Situation.FAILED_BY_GRADES
    return Situation.APPROVED

def calculate_grade_averages_and_student_situations(worksheet, start_row=4, start_col=3, end_col=6):
    worksheet_data = worksheet.get_all_values()  # Get all sheet's values and turn into a list of lists 
    num_classes = int(worksheet_data[1][0].split(":")[1])
    end_row = len(worksheet_data)  # The list of lists' length is equal to the number of rows in the worksheet

    situation_and_grade_of_each_student = []
    print("Starting data processing")
    for row in range(start_row-1, end_row):
        curr_student = worksheet_data[row][1]
        classes_missed = int(worksheet_data[row][2])
        m = sum([int(worksheet_data[row][col]) for col in range(start_col, end_col)]) / 3
        student_situation = define_student_situation(m, num_classes, classes_missed)

        if student_situation == Situation.FINAL_EXAM:
            naf = calculate_naf(m) 
            situation_and_grade_of_each_student.append([situation_strings[student_situation], naf])
        else:
            situation_and_grade_of_each_student.append([situation_strings[student_situation], 0])
    
    return (situation_and_grade_of_each_student, start_row, end_row)

def update_worksheet(worksheet, results, start_row, end_row):
    print("Updating worksheet")
    worksheet.update(f'G{start_row}:H{end_row}', results)

def main():
    scopes = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets"
    ]
    sheet_key = "18PYR23BS3XzmLdQCOPGwJPOPmk5AcNSLIyMMEZbB1RA"
    service_account = "service_account.json"
    worksheet = get_sheet(sheet_key, service_account, scopes)
    students_results, start_row, end_row = calculate_grade_averages_and_student_situations(worksheet)
    update_worksheet(worksheet, students_results, start_row, end_row)
    print("Finished!")
 
if __name__ == '__main__':
    main()


    



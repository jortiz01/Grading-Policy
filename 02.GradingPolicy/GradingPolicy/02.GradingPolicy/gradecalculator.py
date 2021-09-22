import helper as h
class GradePolicy:
    def __init__(self, letterGrade, gpa, start_score, range):
        self.letterGrade = letterGrade
        self.range = range
        self.gpa = gpa
        self.startScore = start_score

    def __init__(self, name, code, letterGrade, gpa, start_score, range):
        self.name = name
        self.code = code
        self.letterGrade = letterGrade
        self.range = range
        self.gpa = gpa
        self.startScore = start_score

def calculate_mid(score):
    score = float(score)
    status = "failing"
    if score >= 65:
        status = "passing"

    return status

gpa_list = []


def load_data():
    f = open('\data\gpa-calculator-data.csv')
    next(f)
    for row in f:
        columns = row.strip().split(",")
        gp = GradePolicy(columns[0], columns[1], columns[2], float(columns[5])
            , float(columns[3]), f"{columns[3]} - {columns[4]}")
        print(columns)
        print(h.to_json(gp))
        gpa_list.append(gp)




def xload_data():
    gpa_list.append(GradePolicy("A", 4.0, 93, "93 - 100")   )
    gpa_list.append(GradePolicy("A-", 3.7, 90, "90 - 92.9")  )
    gpa_list.append(GradePolicy("B+", 3.3, 87, "87 - 89.9") )
    gpa_list.append(GradePolicy("B", 3.0, 83, "83 - 86.9")  )
    gpa_list.append(GradePolicy("B-", 2.7, 80, "80 - 82.9") )
    gpa_list.append(GradePolicy("C+", 2.3, 77, "77 - 79.9") )
    gpa_list.append(GradePolicy("C", 2.0, 70, "70 - 76.9")  )  
    gpa_list.append(GradePolicy("D", 1.0, 60, "60 - 69.9")   )
    gpa_list.append(GradePolicy("F", 0, 0, "0 - 59.9")   )
    print("Loading GPA data...")
    print(gpa_list)


def calculate_gpa(score, code = 'S001'):
    grading_policy = None
    if len(gpa_list) == 0:
        load_data()

    for x in gpa_list:
        if x.startScore <= score and x.code == code:
            grading_policy = x
            break

    
    return grading_policy


if __name__ == "__main__":
    load_data()

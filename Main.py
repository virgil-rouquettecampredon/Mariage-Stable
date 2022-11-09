import random


def generatePreferenceList(numberStudents, numberEstablishments, capacity):
    # generate a list of students and projects
    students = [[i for i in range(numberStudents)] for j in range(numberStudents)]
    establishments = [[i for i in range(numberEstablishments)] for j in range(numberEstablishments)]

    # generate a preference list for each student
    for i in range(numberStudents):
        # generate a preference list for the student
        random.shuffle(students[i])

    # generate a preference list for each project
    for i in range(numberEstablishments):
        # generate a preference list for the project
        random.shuffle(establishments[i])

    return students, establishments

#resolve a stable mariage between students and projects
def resolveStableMariage(students, projects):




if __name__ == '__main__':
    # generate a preference list for each student and project
    student, establishment = generatePreferenceList(10, 10, 1)

    # resolve a stable mariage between students and projects
    resolveStableMariage(student, establishment)






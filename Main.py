import random


def generatePreferenceList(numberStudents, numberEstablishments, capacity):
    # generate a list of students and establishments
    students = [random.sample(range(numberStudents), numberStudents) for i in range(numberStudents)]
    establishments = [random.sample(range(numberEstablishments), numberEstablishments) for i in range(numberEstablishments)]

    return students, establishments

#resolve a stable mariage between students and projects
#def resolveStableMariage(students, projects):




if __name__ == '__main__':
    # generate a preference list for each student and project
    student, establishment = generatePreferenceList(10, 10, 2)

    # resolve a stable mariage between students and projects
    #resolveStableMariage(student, establishment)



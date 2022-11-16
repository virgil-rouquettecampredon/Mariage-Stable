import random


def generatePreferenceList(numberStudents, numberEstablishments, capacity):
    # generate a list of students and establishments
    students = [random.sample(range(1, numberStudents + 1), numberStudents) for i in range(numberStudents)]
    establishments = [random.sample(range(1, numberEstablishments + 1), numberEstablishments) for i in
                      range(numberEstablishments)]

    return students, establishments


# resolve a stable mariage between students and projects
def resolveStableMariage(students, establishments):
    studentAssignment = [0] * len(students)
    establishmentAssignment = [0] * len(establishments)
    finalChoice = {}

    while 0 in studentAssignment:  # Tant qu'un étudiant n'est pas affecté à un établissemnt
        newChoice = 0
        # print(studentAssignment)
        while studentAssignment[newChoice] != 0:
            newChoice += 1
        # print(students[newChoice])
        establishment = students[newChoice].pop(0)
        # print(establishment)
        if establishmentAssignment[establishment - 1] == 0:  # Si l'établissement n'a pas encore choisi d'étudiant
            finalChoice[establishment] = newChoice + 1
            studentAssignment[newChoice] = 1
            establishmentAssignment[establishment - 1] = 1
            #print("L'étudiant", newChoice + 1, "est affecté à l'établissement", establishment)
        else:
            #print("L'étudiant", newChoice + 1, "est en attente de l'établissement", establishment)
            actualChoice = finalChoice[establishment]
            #print("Le choix actuel est l'étudiant", actualChoice)
            trouve = False
            y = 0
            # print(establishments[establishment-1][0])
            while not trouve:
                if establishments[establishment - 1][y] == newChoice + 1:
                    trouve = True
                    preference = newChoice + 1
                elif establishments[establishment - 1][y] == actualChoice:
                    trouve = True
                    preference = actualChoice
                y += 1

            #print("Le choix est l'étudiant", preference)
            if preference == newChoice + 1:
                finalChoice[establishment] = newChoice + 1
                studentAssignment[actualChoice - 1] = 0
                studentAssignment[newChoice] = 1
                establishmentAssignment[establishment - 1] = 1
                #print("L'étudiant", newChoice + 1, "est affecté à l'établissement", establishment)
    return finalChoice


def satisfactionAlgorithm(studentsV, establishmentsV, finalChoice):
    satisfactionV = 0
    for i in range(len(studentsV)):
        for j in range(len(establishmentsV)):
            if finalChoice[j + 1] == i + 1:
                satisfactionV += (len(studentsV) - establishmentsV[j].index(i + 1)) + 1
    return satisfactionV


if __name__ == '__main__':
    # generate a preference list for each student and project
    #student, establishment = generatePreferenceList(100, 100, 2)

    establishment = [[2, 1, 3], [1, 2, 3], [1, 2, 3]]
    student = [[1, 3, 2], [2, 1, 3], [2, 1, 3]]

    studentPrioritizeEstablishment = [row[:] for row in student]
    establishmentPrioritizeEstablishment = [row[:] for row in establishment]

    print("Student priorities :")
    print(student)
    print("Establishment priorities :")
    print(establishment)


    # resolve a stable mariage between students and projects
    print("Stable mariage between students and establishments for students prioritize")
    finalChoice = resolveStableMariage(studentPrioritizeEstablishment, establishmentPrioritizeEstablishment)
    print(finalChoice)
    # List of establishments for each student has been modified after resolving the stable mariage, for calculated
    # the number of choices that the student was affected to the establishment is the number of establishments
    # minus the number of establishments in the list of establishments for the student

    # print(studentPrioritizeEstablishment)
    # print(establishmentPrioritizeEstablishment)

    # calculate the satisfaction of the students
    satisfaction = satisfactionAlgorithm(student, establishment, finalChoice)
    #print(satisfaction)
    # calculate the average rank for the students
    satisfaction = satisfaction / len(student)
    satisfaction = (satisfaction / len(establishment)) * 100
    #print("Satisfaction of the students for establishments prioritize : " + str(round(satisfaction)) + "%")

    # calculate the satisfaction of the establishments
    satisfaction = satisfactionAlgorithm(establishment, student, finalChoice)
    #print(satisfaction)
    # calculate the average rank for the establishments
    satisfaction = satisfaction / len(establishment)
    satisfaction = (satisfaction / len(student)) * 100
    #print("Satisfaction of the establishments for establishments prioritize : " + str(round(satisfaction)) + "%")


    studentPrioritizeStudent = [row[:] for row in student]
    establishmentPrioritizeStudent = [row[:] for row in establishment]

    # resolve a stable mariage between students and projects
    print("Stable mariage between students and establishments for establishments prioritize")
    finalChoice = resolveStableMariage(establishmentPrioritizeStudent, studentPrioritizeStudent)
    print(finalChoice)
    # List of establishments for each student has been modified after resolving the stable mariage, for calculated
    # the number of choices that the student was affected to the establishment is the number of establishments
    # minus the number of establishments in the list of establishments for the student

    # calculate the satisfaction of the establishments
    satisfaction = satisfactionAlgorithm(establishment, student, finalChoice)
    #print(satisfaction)
    # calculate the average rank for the establishments
    satisfaction = satisfaction / len(establishment)
    satisfaction = (satisfaction / len(student)) * 100
    #print("Satisfaction of the establishment for students prioritize : " + str(round(satisfaction)) + "%")

    # calculate the satisfaction of the students
    satisfaction = satisfactionAlgorithm(student, establishment, finalChoice)
    #print(satisfaction)
    # calculate the average rank for the students
    satisfaction = satisfaction / len(student)
    satisfaction = (satisfaction / len(establishment)) * 100
    #print("Satisfaction of the students for students prioritize : " + str(round(satisfaction)) + "%")


    # print(studentPrioritizeStudent)
    # print(establishmentPrioritizeStudent)

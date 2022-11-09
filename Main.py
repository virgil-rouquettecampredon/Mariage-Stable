import random


def generatePreferenceList(numberStudents, numberEstablishments, capacity):
    # generate a list of students and establishments
    students = [random.sample(range(1, numberStudents+1), numberStudents) for i in range(numberStudents)]
    establishments = [random.sample(range(1, numberEstablishments+1), numberEstablishments) for i in range(numberEstablishments)]

    return students, establishments

#resolve a stable mariage between students and projects
def resolveStableMariage(students, establishments):
    studentAssignment = [0] * len(students)
    establishmentAssignment = [0] * len(establishments)
    finalChoice = {}

    while 0 in studentAssignment: #Tant qu'un étudiant n'est pas affecté à un établissemnt
        newChoice = 0
        #print(studentAssignment)
        while studentAssignment[newChoice] != 0:
            newChoice+=1
        #print(students[newChoice])
        establishment = students[newChoice].pop(0)
        #print(establishment)
        if establishmentAssignment[establishment-1] == 0: #Si l'établissement n'a pas encore choisi d'étudiant
            finalChoice[establishment] = newChoice + 1
            studentAssignment[newChoice] = 1
            establishmentAssignment[establishment-1] = 1
        else:
            actualChoice = finalChoice[establishment]
            trouve = False
            y = 0
            #print(establishments[establishment-1][0])
            while not trouve :
                if establishments[establishment-1][y] == newChoice + 1:
                    trouve = True
                    preference = newChoice
                elif establishments[establishment-1][y] == actualChoice:
                    trouve = True
                    preference = actualChoice
                y+=1
            if preference == newChoice + 1:
                finalChoice[establishment] = newChoice + 1
                studentAssignment[actualChoice - 1] = 0
                studentAssignment[newChoice] = 1
                establishmentAssignment[establishment-1] = 1
    return finalChoice


if __name__ == '__main__':
    # generate a preference list for each student and project
    student, establishment = generatePreferenceList(100, 100, 2)

    studentPrioritizeEstablishment = [row[:] for row in student]
    establishmentPrioritizeEstablishment = [row[:] for row in establishment]

    print("Student priorities :")
    print(student)
    print("Establishment priorities :")
    print(establishment)

    # resolve a stable mariage between students and projects
    print("Stable mariage between students and establishments for establishments prioritize")
    print(resolveStableMariage(studentPrioritizeEstablishment, establishmentPrioritizeEstablishment))
    #List of establishments for each student has been modified after resolving the stable mariage, for calculated
    #the number of choices that the student was affected to the establishment is the number of establishments
    #minus the number of establishments in the list of establishments for the student

    #print(studentPrioritizeEstablishment)
    #print(establishmentPrioritizeEstablishment)

    studentPrioritizeStudent = [row[:] for row in student]
    establishmentPrioritizeStudent = [row[:] for row in establishment]

    # resolve a stable mariage between students and projects
    print("Stable mariage between students and establishments for students prioritize")
    print(resolveStableMariage(establishmentPrioritizeStudent, studentPrioritizeStudent))
    # List of establishments for each student has been modified after resolving the stable mariage, for calculated
    # the number of choices that the student was affected to the establishment is the number of establishments
    # minus the number of establishments in the list of establishments for the student

    #print(studentPrioritizeStudent)
    #print(establishmentPrioritizeStudent)



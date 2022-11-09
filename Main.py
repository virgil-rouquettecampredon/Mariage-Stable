import random


def generatePreferenceList(numberStudents, numberEstablishments, capacity):
    # generate a list of students and establishments
    students = [random.sample(range(1, numberStudents + 1), numberStudents) for i in range(numberStudents)]
    establishments = [random.sample(range(1, numberEstablishments + 1), numberEstablishments) for i in range(numberEstablishments)]

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
    student, establishment = generatePreferenceList(10, 10, 2)

    # resolve a stable mariage between students and projects
    print(resolveStableMariage(student, establishment))



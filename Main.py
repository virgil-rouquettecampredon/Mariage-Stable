import random


def generatePreferenceList(numberStudents, numberProjects):
    # generate a list of students and projects
    students = list(range(1, numberStudents + 1))
    projects = list(range(1, numberProjects + 1))
    # generate a preference list for each student
    for student in students:
        # generate a preference list for the student
        preferenceList = random.sample(projects, len(projects))
        # write the preference list to a file
        with open("student" + ".txt", "a") as f:
            f.write(str(preferenceList) + "\n")
    # generate a preference list for each project
    for project in projects:
        # generate a preference list for the project
        preferenceList = random.sample(students, len(students))
        # write the preference list to a file
        with open("project" + ".txt", "a") as f:
            f.write(str(preferenceList) + "\n")
    return students, projects

#resolve a stable mariage between students and projects
def resolveStableMariage(students, projects):



if __name__ == '__main__':
    # create an empty file
    open('student.txt', 'w').close()
    open('project.txt', 'w').close()

    # generate a preference list for each student and project
    generatePreferenceList(10, 10)





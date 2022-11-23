import eel
import random

eel.init('web', allowed_extensions=['.js', '.html'])

@eel.expose
def generatePreferenceList(numberStudents, numberEstablishments):
    # generate a list of students and establishments
    students = [random.sample(range(numberStudents), numberStudents) for i in range(numberStudents)]
    establishments = [random.sample(range(numberEstablishments), numberEstablishments) for i in range(numberEstablishments)]

    return students, establishments

eel.start('index.html', mode=None)
#ABIYYU TAJ MAHASIN BAGINDO
#TP058652

def registerPatient():

    patient = []

    name = input("Enter patient name: ")
    patientid = input("Enter patient ID: ")
    email = input("Enter patient email: ")
    group = input("Enter patient group: ")
    zone = input("Enter patient zone: ")

    patient.append(name)
    patient.append(patientid)
    patient.append(email)
    patient.append(group)
    patient.append(zone)
    patient.append("1")
    patient.append(" - ")
    print(patient)
    
    with open("patient.txt", "a") as f:
        print(patient, file = f) 
    with open("name.txt", "a") as f:
        print(patient[0], file = f)   
    with open("id.txt", "a") as f:
        print(patient[1], file = f) 
    with open("mail.txt", "a") as f:
        print(patient[2], file = f) 
    with open("group.txt", "a") as f:
        print(patient[3], file = f) 
    with open("zone.txt", "a") as f:
        print(patient[4], file = f)   
    with open("test.txt", "a") as f:
        print(patient[5], file = f)   
    
def testPatient():

    patientID = input("Enter patient ID: ")

    # Read all patient ID
    f = open("id.txt", "r")
    linesID = f.read().split('\n')
    f.close()
    del(linesID[-1])
    

    # Read all patient test number
    f = open("test.txt", "r")
    linesTest = f.read().split('\n')
    f.close()
    del(linesTest[-1])

    # Read all patient names
    f = open("name.txt", "r")
    linesName = f.read().split('\n')
    f.close()
    del(linesName[-1])

    # Read all groups
    f = open("group.txt", "r")
    linesGroup = f.read().split('\n')
    f.close()
    del(linesGroup[-1])

    # Read all T1 results
    f = open("test1.txt", "r")
    linesT1 = f.read().split('\n')
    f.close()
    del(linesT1[-1])

    # Read all T2 results
    f = open("test2.txt", "r")
    linesT2 = f.read().split('\n')
    f.close()
    del(linesT2[-1])

    # Read all T3 results
    f = open("test3.txt", "r")
    linesT3 = f.read().split('\n')
    f.close()
    del(linesT3[-1])

    # Determine 
    for patient in linesID:
        if patient == patientID:
            testSubject = patientID
            break
        else:
            print("Patient not found")    
    print(testSubject)

    IndexValue = int(testSubject) - 1

    testSubjectTest = linesTest[IndexValue]
    testSubjectName = linesName[IndexValue]
    testSubjectGroup = linesGroup[IndexValue]
    testSubjectT1 = linesT1[IndexValue]
    testSubjectT2 = linesT2[IndexValue]
    testSubjectT3 = linesT3[IndexValue]
    
    int(testSubjectTest)

    print("Commit Test " + str(testSubjectTest) + " on patient " + testSubjectName + "?")
    print("1. Yes")
    print("2. No")
    commitTest = input("Choose option: ")

    commitTest = int(commitTest)

    if commitTest == 1: # Start test

        print("Enter test result: ")
        print("1. Positive")
        print("2. Negative")
        testResult = input("Enter choice: ")
         #EXP
        
        if testSubjectTest == "1": # First test

            if testResult == "1": # First test shows positive

                if testSubjectGroup == "ATO":
                    testSolution = "QHNF"
                elif testSubjectGroup == "ACC":
                    testSolution = "QHNF"  
                elif testSubjectGroup == "AEO":
                    testSolution = "QHNF"
                elif testSubjectGroup == "SID":
                    testSolution = "QHNF"    
                elif testSubjectGroup == "AHS":
                    testSolution = "HQNF"
                else:
                    print("Invalid Group")
                print("Please do " + testSolution)      

            elif testResult == "2": # First test shows negative

                if testSubjectGroup == "ATO":
                    testSolution = "QDFR"
                elif testSubjectGroup == "ACC":
                    testSolution = "QDFR"  
                elif testSubjectGroup == "AEO":
                    testSolution = "QDFR"
                elif testSubjectGroup == "SID":
                    testSolution = "HQFR"    
                elif testSubjectGroup == "AHS":
                    testSolution = "CWFR"
                else:
                    print("Invalid Group")
                print("Please do " + testSolution)         

            else: #Invalid First Test
                print(testResult + " is an invalid Choice")            

        elif testSubjectTest == "2": # Second test

            if testResult == "1": # Second test shows positive

                if testSubjectGroup == "ATO":
                    testSolution = "QHNF"
                elif testSubjectGroup == "ACC":
                    testSolution = "QHNF"  
                elif testSubjectGroup == "AEO":
                    testSolution = "QHNF"
                elif testSubjectGroup == "SID":
                    testSolution = "QHNF"    
                elif testSubjectGroup == "AHS":
                    testSolution = "HQNF"
                else:
                    print("Invalid Group")
                print("Please do " + testSolution)       

            elif testResult == "2": # Second test shows negative

                if testSubjectGroup == "ATO":
                    testSolution = "QDFR"
                elif testSubjectGroup == "ACC":
                    testSolution = "QDFR"  
                elif testSubjectGroup == "AEO":
                    testSolution = "QDFR"
                elif testSubjectGroup == "SID":
                    testSolution = "HQFR"    
                elif testSubjectGroup == "AHS":
                    testSolution = "CWFR"
                else:
                    print("Invalid Group")    
                print("Please do " + testSolution) 

            else: #Invalid second test
                print(testResult + " is an invalid Choice")

        elif testSubjectTest == "3": # Third test

            if testResult == "1": # Third test shows positive

                if testSubjectGroup == "ATO":
                    testSolution = "QHNF"
                elif testSubjectGroup == "ACC":
                    testSolution = "QHNF"  
                elif testSubjectGroup == "AEO":
                    testSolution = "QHNF"
                elif testSubjectGroup == "SID":
                    testSolution = "QHNF"    
                elif testSubjectGroup == "AHS":
                    testSolution = "HQNF"
                else:
                    print("Invalid Group")
                print("Please do " + testSolution)       

            elif testResult == "2": # Second test shows negative

                if testSubjectGroup == "ATO":
                    testSolution = "RU"
                elif testSubjectGroup == "ACC":
                    testSolution = "RU"  
                elif testSubjectGroup == "AEO":
                    testSolution = "RU"
                elif testSubjectGroup == "SID":
                    testSolution = "RU"    
                elif testSubjectGroup == "AHS":
                    testSolution = "CW"
                else:
                    print("Invalid Group")
                print("Please do " + testSolution)         

            else: #Invalid third test
                print(testResult + " is an invalid Choice")  

        else: #Fourth and so on tests
            print("Patients are only allowed to do up to a maximum of three tests")              
                       
    elif commitTest == 2: #Testing did not start
        print("Goodbye")

    else: #faggot
        result = "wrong answer faggot"    
            
testPatient()
def readFile():
    FILE_NAME = 'Class.txt'
    FILE_OBJECT = open(FILE_NAME, "r")
    WORDS = FILE_OBJECT.read().splitlines()
    FILE_OBJECT.close()

    return WORDS
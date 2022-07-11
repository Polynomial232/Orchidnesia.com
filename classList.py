def readFile():
    FILE_NAME = 'Class.txt'
    FILE_OBJECT = open(FILE_NAME, "r")
    WORDS = FILE_OBJECT.read().splitlines()
    FILE_OBJECT.close()

    return 
    
def pred(FILE):
    SHAPE = (224, 224)
    IMG = plt.imread(FILE)
    IMG = cv2.resize(IMG,(224,224))
    IMG = IMG.reshape(1,224,224,3)

    PRED = MODEL.predict(np.array(IMG))

    return CLASS[np.argmax(PRED)]
class Postprocessor:
    def __init__(self):
        pub = rospy.Publisher('chatter', String, queue_size=10)
    def generateMessages(self, machineOutput):
        systemOutput = ""
        for key in machineOutput:
            systemOutput = systemOutput + key
        return systemOutput

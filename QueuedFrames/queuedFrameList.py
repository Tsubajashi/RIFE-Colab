class QueuedFrameList:
    frameList:list = None
    startFrame:str = None
    startFrameDest:str = None
    endFrame:str = None
    endFrameDest:str = None
    progressMessage:str = None
    def __init__(self, frameList, startFrame,startFrameDest, endFrame,endFrameDest):
        self.frameList = frameList
        self.startFrame = startFrame
        self.startFrameDest = startFrameDest
        self.endFrame = endFrame
        self.endFrameDest = endFrameDest


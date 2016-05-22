class PrintJob(object):
    def __init__(self, who, priority):
        self._who = who
        self._priority = priority

    def __cmp__(self, other):
        if type(other) != type(self):
            raise TypeError, "Type must be PrintJob"
        return cmp(self._priority, other._priority)

    def getJob(self):
        return self._who

    def getPriority(self):
        return self._priority

    def __str__(self):
        return "("+str(self._who)+","+str(self._priority)+")"

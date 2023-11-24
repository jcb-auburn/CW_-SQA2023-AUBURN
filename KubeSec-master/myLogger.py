import logging

def createLoggerObj():
    fileName  = "usage.log"
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
    myLogObj = logging.getLogger('sqa2023-logger')
    return myLogObj
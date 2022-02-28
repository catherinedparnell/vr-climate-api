import constants as CONSTANTS
def processTemp(celcius):
    return celcius * 9/5 + 32

def processPrecip(yearlyAvg):
    return yearlyAvg / CONSTANTS.AVG_PRECIP_DAYS_PER_YEAR
import fileinput


class DriverData:
    def __init__(self, totalDistance, totalDuration):
        self.totalDistance = totalDistance
        self.totalDuration = totalDuration


def GetDriverData(input):
    """Gets Drivers Data from a FileInput and returns it as a dictionary of key: Driver name, value: DriverData (class)"""
    driversData = {}
    for line in input:
        # Split line into args
        args = line.rstrip().split(' ')

        # Determine line command type
        # New Driver
        if args[0] == 'Driver' and len(args) == 2:
            if not args[1] in driversData:
                driversData[args[1]] = DriverData(0, 0)
        # New Trip
        elif args[0] == 'Trip' and len(args) == 5:
            if args[1] in driversData:
                try:
                    AddTripToDriver(driversData[args[1]], args[2], args[3], float(args[4]))
                except Exception:
                    raise Exception(f'Invalid trip input {line}')
            else:
                raise Exception(f'Driver does not exist: {args[1]}')
        else:
            raise Exception(f'Line not a valid format {line}')
    return driversData


def AddTripToDriver(driverData, startTime, endTime, distance):
    """Adds a trip to a driver's data"""
    startSplit = startTime.split(':')
    endSplit = endTime.split(':')
    durationInHours = (int(endSplit[0]) - int(startSplit[0])) + ((int(endSplit[1]) - int(startSplit[1])) / 60)
    speed = distance / durationInHours
    # Dont add trips where the speed was less than 5 mph or greather than 100 mph
    if speed >= 5 and speed <= 100:
        driverData.totalDistance += distance
        driverData.totalDuration += durationInHours


def PrintReport(driverDictionary):
    """Prints a report given a dictonary of Driver Data (key: driver name, value: DriverData class)"""
    # Sort driver data by further travelled first
    for driver in sorted(driverDictionary, key=lambda x: driverDictionary[x].totalDistance, reverse=True):
        driverData = driverDictionary[driver]
        if driverData.totalDuration > 0:
            avgSpeed = round(driverData.totalDistance / driverData.totalDuration)
            print(f'{driver} {driverData.totalDistance} miles @ {avgSpeed} mph')
        else:
            print(f'{driver} {driverData.totalDistance} miles')


driverData = GetDriverData(fileinput.input())
PrintReport(driverData)

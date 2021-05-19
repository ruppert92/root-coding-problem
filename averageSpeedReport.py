import sys


class DriverData:
    def __init__(self, name, totalDistance, totalDuration):
        self.name = name
        self.totalDistance = totalDistance
        self.totalDuration = totalDuration

    @property
    def avgSpeed(self):
        if self.totalDuration > 0:
            return round(self.totalDistance / self.totalDuration)
        return 0

    def AddTripToDriver(self, startTime, endTime, distance):
        """Adds a trip to a driver's data"""
        startSplit = startTime.split(':')
        endSplit = endTime.split(':')
        durationInHours = (int(endSplit[0]) - int(startSplit[0])) + ((int(endSplit[1]) - int(startSplit[1])) / 60)
        speed = distance / durationInHours
        # Dont add trips where the speed was less than 5 mph or greather than 100 mph
        if speed >= 5 and speed <= 100:
            self.totalDistance += distance
            self.totalDuration += durationInHours


def GetDriverData(filepath):
    """Gets Drivers Data from a file and returns it as a list of key: Driver name, value: DriverData (class)"""
    driversData = {}
    with open(filepath) as f:
        for line in f.readlines():
            # Split line into args
            args = line.rstrip().split(' ')

            # Determine line command type
            # New Driver
            if args[0] == 'Driver' and len(args) == 2:
                if not args[1] in driversData:
                    driversData[args[1]] = DriverData(args[1], 0, 0)
            # New Trip
            elif args[0] == 'Trip' and len(args) == 5:
                if args[1] in driversData:
                    try:
                        driversData[args[1]].AddTripToDriver(args[2], args[3], float(args[4]))
                    except Exception:
                        raise Exception(f'Invalid trip input {line}')
                else:
                    raise Exception(f'Driver does not exist: {args[1]}')
            else:
                raise Exception(f'Line not a valid format {line}')
    # Sort driver data by further travelled first
    return sorted(driversData.values(), key=lambda x: x.totalDistance, reverse=True)


def PrintReport(driverDataList):
    """Prints a report given a dictonary of Driver Data (key: driver name, value: DriverData class)"""
    for driverData in driverDataList:
        if driverData.totalDuration > 0:
            print(f'{driverData.name} {driverData.totalDistance} miles @ {driverData.avgSpeed} mph')
        else:
            print(f'{driverData.name} {driverData.totalDistance} miles')


def GenerateAndPrintReport(filepath):
    driverData = GetDriverData(filepath)
    PrintReport(driverData)


if __name__ == "__main__":
    GenerateAndPrintReport(sys.argv[1])

class UndergroundSystem:

    def __init__(self):
        self.check_in = defaultdict(tuple)
        self.check_out = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, start_station = self.check_in[id]
        total = t - start_time
        self.check_out[(start_station, stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.check_out[(startStation, endStation)]) / len(
            self.check_out[(startStation, endStation)]
        )


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

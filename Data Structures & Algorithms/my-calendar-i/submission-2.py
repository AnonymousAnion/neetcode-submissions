class MyCalendar:
    
    def __init__(self):
        
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        
        for booking in self.bookings:

            start, end = booking

            if start <= startTime < end or start < endTime <= end or (startTime <= start and end <= endTime):

                return False

        self.bookings.append((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def print_time(self):
        print(f"The time is {self.hour}:{self.minute}")

hour = input("Enter hour: ")
minute = input("Enter minute: ")

my_time = Time(hour, minute)
my_time.print_time()
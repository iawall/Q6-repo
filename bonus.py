''' my attempt at bonus
S: Each class has its own single responsibility with seperate classes
O: you can add a new type of activity with a subclass of Activity and the classes given will not need to be modified
L: WalkingActivity and RunningActivity inherit from activity and are similar, therefore can be replaceable
I: ActivityDataStorage and Activity Display use abstractmethod and the subclasses and the subclasses use these methods
D: DataStorage and Display depend on the abstraction and defining of ActivityDataStorage and ActivityDisplay
'''
from abc import ABC, abstractmethod
import math

burned_per_step = 0.05
# each class has a different responsibility (storing/displaying/calculating/etc) (SRP)
class ActivityDataStorage(ABC):
    @abstractmethod
    def __init__(self, totalSteps, totalHours):
        self.totalSteps = totalSteps
        self.totalHours = totalHours
    
    def totalMiles(totalSteps, stepLength):
        return (totalSteps * stepLength) / 5280

# only has printTotalMethod which segregates from the unnecessary methods (ISP)
class ActivityDisplay(ABC):
    @abstractmethod
    def printTotal(self, totalSteps):
        print(f"{self.totalSteps}") # subclass prints total steps

# DataStorage and Display can be extended but not modified (OCP)
# they also depend on the abstract classes ActivityDataStorage and ActivityDisplay so they can be extended (DIP)
class DataStorage(ActivityDataStorage):
    def __init__(self, totalSteps, totalHours):
        self.totalSteps = totalSteps
        self.totalHours = totalHours
    def add_activity(self, activity):
        self.totalSteps += activity.steps

class Display(ActivityDisplay):
    def printTotal(self, totalSteps):
        print(f"Total Steps: {totalSteps}")

# can be used instead of WalkingActivity and RunningActivity (LSP)
class Activity:
    def __init__(self, steps, distance, calories_burned, min_spent):
        self.steps = steps
        self.distance = distance
        self.calories_burned = calories_burned
        self.min_spent = min_spent

# Walking activity and Running activity are added without changing the existing code (OCP)
class WalkingActivity(Activity):
    def __init__(self, steps, distance, calories_burned, min_spent):
        self.steps = steps
        self.distance = distance
        self.calories_burned = calories_burned
        self.min_spent = min_spent
class RunningActivity(Activity):
    def __init__(self, steps, distance, calories_burned, min_spent):
        self.steps = steps
        self.distance = distance
        self.calories_burned = calories_burned
        self.min_spent = min_spent
class Calculations:
    @staticmethod
    def stepsToDistance(steps, stepLength):
        return (steps * stepLength) / 5280

    @staticmethod
    def distanceToSteps(distanceMiles, stepLength):
        return (distanceMiles * 5280) / stepLength

    @staticmethod
    def caloriesBurned(steps):
        return burned_per_step * steps

    @staticmethod
    def minutesToHours(minutes):
        return minutes / 60

def main():
    total_steps = 9784
    total_hours = 4.7

    data_storage = DataStorage(total_steps, total_hours) # data storage object

    display = Display()
    display.printTotal(total_steps)

    walking_activity = WalkingActivity(steps=5000, distance=2.5, calories_burned=250, min_spent=60) # created walking activity object
    running_activity = RunningActivity(steps=10000, distance=5, calories_burned=500, min_spent=120) # created running activity object

if __name__ == "__main__":
    main()

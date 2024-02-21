from abc import ABC, abstractmethod
import math

burned_per_step = 0.05

class DataStorage:
    @abstractmethod
    def __init__(self, totalSteps, totalHours):
        self.totalSteps = totalSteps
        self.totalHours = totalHours
    
    def totalMiles(totalSteps, stepLength):
        return (totalSteps * stepLength) / 5280

class Display:
    def printTotal():
        print(f"Total Steps: {DataStorage.totalSteps}")
        print(f"Total Miles: {DataStorage.totalMiles(totalSteps, stepLength)}")
        print(f"Hours working out: {totalHours}")

class Activity:
    @abstractmethod
    def __init__(self, steps, distance, calories_burned, min_spent):
        self.steps = steps
        self.distance = distance
        self.calories_burned = calories_burned
        self.min_spent = min_spent

class Calculations:
    def stepsToDistance(steps, stepLength):
        distanceMiles = (steps * stepLength) / 5280
        return distanceMiles

    def distanceToSteps(distanceMiles, stepLength):
        steps = (distanceMiles * 5280) / stepLength
        return steps

    def caloriesBurned(steps):
        burned_per_step = 0.05
        calories_burned = burned_per_step * steps
        return calories_burned

    def minutesToHours(minutes):
        return minutes / 60

    


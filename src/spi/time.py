import pygame
import time
from enum import IntEnum


class TimeUnit(IntEnum):
    NANOS = 0
    MICROS = 1
    MILLIS = 2
    SECOND = 3
    MINUTE = 4
    HOUR = 5

    @staticmethod
    def convert(time: float, old_unit: "TimeUnit", new_unit: "TimeUnit") -> float:
        if old_unit == new_unit:
            return time
        
        nanos_per_unit = {
            TimeUnit.NANOS: 1,
            TimeUnit.MICROS: 1000,
            TimeUnit.MILLIS: 1000000,
            TimeUnit.SECOND: 1000000000,
            TimeUnit.MINUTE: 60000000000,
            TimeUnit.HOUR: 3600000000000
        }
        
        return time * (nanos_per_unit[old_unit] / nanos_per_unit[new_unit])


class _TimedeltaCalculator():
    def __init__(self):
        self._last_tick_time: float = 0
        self._elapsed_time: float = 0
        
    def tick(self):
        current_time = time.time()
        self._elapsed_time = current_time - self._last_tick_time
        self._last_tick_time = current_time
    
    def get_timedelta(self):
        return self._elapsed_time


class _AverageFpsCalculator():
    def __init__(self):
        self._frames: int = 0
        self._last_calc_time: float = 0
        self._average_fps: int = 0
    
    def tick(self):
        self._frames += 1
        current_time = time.time()
        if current_time - self._last_calc_time >= 1:
            self._average_fps = self._frames
            self._frames = 0
            self._last_calc_time = current_time
    
    def get_average_fps(self):
        return self._average_fps


class Time():
    _clock = pygame.time.Clock()
    _timedelta_calculator = _TimedeltaCalculator()
    _average_fps_calculator = _AverageFpsCalculator()
    
    @classmethod
    def tick(cls, fps: float):
        cls._clock.tick(fps)
        cls._timedelta_calculator.tick()
        cls._average_fps_calculator.tick()
    
    @classmethod
    def get_average_fps(cls):
        return cls._average_fps_calculator.get_average_fps()
    
    @classmethod
    def get_fps(cls):
        return 1 / (cls._timedelta_calculator.get_timedelta() + 1e-6)
    
    @classmethod
    def get_timedelta(cls):
        return cls._timedelta_calculator.get_timedelta()

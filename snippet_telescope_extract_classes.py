from typing import List

class Telescope:
    def __init__(self, brand: str, aperture: float, focal_length: float, mount_type: str):
        self.brand = brand
        self.aperture = aperture
        self.focal_length = focal_length
        self.mount_type = mount_type
        self.lens = None
        self.motor = None
        self.tracking_system = None
        self.observations = []

    def attach_lens(self, lens):
        self.lens = lens

    def attach_motor(self, motor):
        self.motor = motor

    def attach_tracking_system(self, tracking_system):
        self.tracking_system = tracking_system

    def observe(self, target):
        if self.tracking_system is not None:
            self.tracking_system.track(target)
        observation = f"Observing {target} with {self.brand} telescope."
        self.observations.append(observation)
        print(observation)

# Exemple d'utilisation
telescope = Telescope("Celestron", 200, 1000, "Equatorial")
telescope.attach_lens("Barlow 2x")
telescope.attach_motor("Stepper Motor")
telescope.attach_tracking_system("GPS Tracker")
telescope.observe("Orion Nebula")


# - Solution

from typing import List

class Lens:
    def __init__(self, name: str):
        self.name = name

class Motor:
    def __init__(self, type: str):
        self.type = type

class TrackingSystem:
    def __init__(self, name: str):
        self.name = name

    def track(self, target):
        print(f"Tracking {target}.")

class Observation:
    def __init__(self, target: str, telescope_brand: str):
        self.target = target
        self.telescope_brand = telescope_brand

class Telescope:
    def __init__(self, brand: str, aperture: float, focal_length: float, mount_type: str):
        self.brand = brand
        self.aperture = aperture
        self.focal_length = focal_length
        self.mount_type = mount_type
        self.lens = None
        self.motor = None
        self.tracking_system = None
        self.observations: List[Observation] = []

    def attach_lens(self, lens: Lens):
        self.lens = lens

    def attach_motor(self, motor: Motor):
        self.motor = motor

    def attach_tracking_system(self, tracking_system: TrackingSystem):
        self.tracking_system = tracking_system

    def observe(self, target: str):
        if self.tracking_system is not None:
            self.tracking_system.track(target)
        observation = Observation(target, self.brand)
        self.observations.append(observation)
        print(f"Observing {target} with {self.brand} telescope.")


# -- Test unitaires

import pytest
from telescope import Telescope, Lens, Motor, TrackingSystem

# Test Telescope class
def test_telescope_creation():
    telescope = Telescope("Celestron", 200, 1000, "Equatorial")
    assert telescope.brand == "Celestron"
    assert telescope.aperture == 200
    assert telescope.focal_length == 1000
    assert telescope.mount_type == "Equatorial"
    assert telescope.lens is None
    assert telescope.motor is None
    assert telescope.tracking_system is None
    assert telescope.observations == []

def test_attach_lens():
    telescope = Telescope("Celestron", 200, 1000, "Equatorial")
    lens = Lens("Barlow 2x")
    telescope.attach_lens(lens)
    assert telescope.lens == lens

def test_attach_motor():
    telescope = Telescope("Celestron", 200, 1000, "Equatorial")
    motor = Motor("Stepper Motor")
    telescope.attach_motor(motor)
    assert telescope.motor == motor

def test_attach_tracking_system():
    telescope = Telescope("Celestron", 200, 1000, "Equatorial")
    tracking_system = TrackingSystem("GPS Tracker")
    telescope.attach_tracking_system(tracking_system)
    assert telescope.tracking_system == tracking_system

def test_observe():
    telescope = Telescope("Celestron", 200, 1000, "Equatorial")
    tracking_system = TrackingSystem("GPS Tracker")
    telescope.attach_tracking_system(tracking_system)
    target = "Orion Nebula"
    telescope.observe(target)
    assert len(telescope.observations) == 1
    observation = telescope.observations[0]
    assert observation.target == target
    assert observation.telescope_brand == "Celestron"

# Test Lens class
def test_lens_creation():
    lens = Lens("Barlow 2x")
    assert lens.name == "Barlow 2x"

# Test Motor class
def test_motor_creation():
    motor = Motor("Stepper Motor")
    assert motor.type == "Stepper Motor"

# Test TrackingSystem class
def test_tracking_system_creation():
    tracking_system = TrackingSystem("GPS Tracker")
    assert tracking_system.name == "GPS Tracker"

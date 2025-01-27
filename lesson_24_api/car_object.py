from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    year: str
    engine_volume: float
    price: int
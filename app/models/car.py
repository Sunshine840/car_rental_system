from enum import Enum  # import enums


# Different car types, add more if available
class CarType(Enum):
    SEDAN = "Sedan"
    SUV = "SUV"
    HATCHBACK = "Hatchback"
    COUPE = "Coupe"
    CONVERTIBLE = "Convertible"


# Car transmission types extendable
class TransmissionType(Enum):
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class Car:
    def __init__(
        self,
        id,
        make,
        model_year,
        color,
        car_type: CarType,
        transmission: TransmissionType,
        mileage,
        availability_status=True,  # default set to available
        price=0.0,  # default set to 0
    ):
        self.id = id
        self.make = make
        self.model_year = model_year
        self.color = color
        self.car_type = car_type
        self.transmission = transmission
        self.mileage = mileage
        self.availability_status = availability_status
        self.price = price

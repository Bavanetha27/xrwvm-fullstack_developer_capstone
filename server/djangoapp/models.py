from django.db import models


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description[:50]}..."


class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    TRUCK = 'Truck'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (TRUCK, 'Truck'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()  # Cloudant dealer ID
    name = models.CharField(null=False, max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES)
    year = models.DateField()

    def __str__(self):
        return (
            f"{self.name} ({self.car_type}, {self.year.year}) "
            f"from {self.car_make.name}"
        )

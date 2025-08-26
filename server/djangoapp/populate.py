from .models import CarMake, CarModel


def initiate():
    """
    Populates the database with initial CarMake and CarModel data.
    """
    # Create CarMake instances using bulk_create for efficiency
    car_makes_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]
    
    car_make_objects = [CarMake(**data) for data in car_makes_data]
    CarMake.objects.bulk_create(car_make_objects)

    # Fetch the newly created CarMake instances
    car_make_instances = {
        car.name: car for car in CarMake.objects.all()
    }

    # Prepare CarModel instances with the corresponding CarMake instances
    car_models_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances["NISSAN"]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances["NISSAN"]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances["NISSAN"]},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances["Mercedes"]},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances["Mercedes"]},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances["Mercedes"]},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances["Audi"]},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances["Audi"]},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances["Audi"]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances["Kia"]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances["Kia"]},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances["Kia"]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances["Toyota"]},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances["Toyota"]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances["Toyota"]},
    ]

    car_model_objects = [CarModel(**data) for data in car_models_data]
    CarModel.objects.bulk_create(car_model_objects)

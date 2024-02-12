import uuid
from datetime import datetime


class BaseModel:
    """Defines the BaseModel class."""

    def __init__(self):
        """Initialize BaseModel attributes."""
        self.id = str(uuid.uuid4())  # Generate unique id
        self.created_at = datetime.now()  # Set creation datetime
        self.updated_at = datetime.now()  # Set update datetime

    def __str__(self):
        """Return string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()  # Get instance attributes
        obj_dict['__class__'] = type(self).__name__  # Add class name
        obj_dict['created_at'] = self.created_at.isoformat()  # ISO format
        obj_dict['updated_at'] = self.updated_at.isoformat()  # ISO format
        return obj_dict


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)

    my_model.save()
    print(my_model)

    my_model_json = my_model.to_dict()
    print(my_model_json)

    print("JSON of my_model:")
    for key, value in my_model_json.items():
        print("\t{}: ({}) - {}".format(key, type(value), value))


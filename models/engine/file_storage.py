import json

class FileStorage:
    """Serializes instances to JSON format and deserializes JSON to instances."""

    def __init__(self):
        """Initialize an empty dictionary to store serialized objects."""
        self.__objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set the value of __objects with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON and save to file."""
        filename = "file.json"
        with open(filename, "w") as file:
            obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize JSON from file to __objects."""
        filename = "file.json"
        try:
            with open(filename, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    module = __import__("models." + class_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj_instance = class_(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

# Create an instance of FileStorage to be used as a storage object
storage = FileStorage()


#!/usr/bin/python3
"""Command Interpreter Module"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class."""
    prompt = "(hbnb) "

    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review}

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel and saves it
        to JSON file."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.class_dict[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        obj = objs.get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
        else:
            del objs[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        objs = storage.all()
        if arg and arg in HBNBCommand.class_dict:
            print([str(obj) for key, obj in objs.items()
                   if type(obj).__name__ == arg])
        elif arg in HBNBCommand.class_dict:
            print([str(obj) for key, obj in objs.items()
                   if type(obj).__name__ == arg])
        elif arg:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objs.values()])

    def do_count(self, arg):
        """Retrieves the number of instances of a class."""
        count = 0
        objs = storage.all()
        if arg in HBNBCommand.class_dict:
            for obj in storage.all().values():
                if isinstance(obj, HBNBCommand.class_dict[arg]):
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
        else:
            setattr(objs[key], args[2], args[3])
            storage.save()

    def do_update_from_dict(self, arg):
        """Updates an instance based on the class name and id with a dictionary."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** dictionary missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
        else:
            new_dict = eval(args[2])
            for k, v in new_dict.items():
                setattr(objs[key], k, v)
            storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        sys.exit()

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True
    
    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()


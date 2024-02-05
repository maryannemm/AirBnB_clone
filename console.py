#!/usr/bin/python3
"""Console module"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        cls = HBNBCommand.classes.get(arg)
        if not cls:
            print("** class doesn't exist **")
            return

        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args or args[0] not in HBNBCommand.classes:
            print("** class name missing **")
            return

        cls = HBNBCommand.classes[args[0]]
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(cls.__name__, obj_id)
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return

        print(objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args or args[0] not in HBNBCommand.classes:
            print("** class name missing **")
            return

        cls = HBNBCommand.classes[args[0]]
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(cls.__name__, obj_id)
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return

        del objs[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = arg.split()
        objs = models.storage.all()

        if not args:
            print([str(objs[obj]) for obj in objs.values()])
            return

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        cls = HBNBCommand.classes[args[0]]
        print([str(obj) for obj in objs.values() if isinstance(obj, cls)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args or args[0] not in HBNBCommand.classes:
            print("** class name missing **")
            return

        cls = HBNBCommand.classes[args[0]]
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(cls.__name__, obj_id)
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute = args[2]
        value = args[3]
        setattr(objs[key], attribute, value)
        objs[key].save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        parts = line.split(".")
        if len(parts) == 2:
            class_name = parts[0]
            if class_name in HBNBCommand.classes:
                command = parts[1].split("(")[0]
                if command == "all":
                    self.do_all(class_name)
                elif command == "count":
                    self.do_count(class_name)
                elif command == "show":
                    id_str = parts[1].split("(")[1].rstrip(")")
                    self.do_show("{} {}".format(class_name, id_str))
                elif command == "destroy":
                    id_str = parts[1].split("(")[1].rstrip(")")
                    self.do_destroy("{} {}".format(class_name, id_str))
                elif command == "update":
                    update_str = parts[1].split("(")[1].rstrip(")")
                    update_args = update_str.split(", ")
                    id_str = update_args[0].strip('"')
                    update_args[0] = "{} {}".format(class_name, id_str)
                    update_args_str = ", ".join(update_args)
                    self.do_update("{} {}".format(class_name, update_args_str))
                else:
                    super().default(line)
            else:
                super().default(line)
        else:
            super().default(line)

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        args = arg.split()
        if not args or args[0] not in HBNBCommand.classes:
            print("** class name missing **")
            return

        cls = HBNBCommand.classes[args[0]]
        objs = models.storage.all()
        count = sum(1 for obj in objs.values() if isinstance(obj, cls))
        print(count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()


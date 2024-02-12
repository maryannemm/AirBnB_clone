#!/usr/bin/python3
"""Implements the HBNB console for managing HolbertonBnB objects."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_arguments(args):
    """Parse arguments from command line input."""
    curly_braces = re.search(r"\{(.*?)\}", args)
    brackets = re.search(r"\[(.*?)\]", args)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(args)]
        else:
            lex = split(args[:brackets.span()[0]])
            ret_list = [i.strip(",") for i in lex]
            ret_list.append(brackets.group())
            return ret_list
    else:
        lex = split(args[:curly_braces.span()[0]])
        ret_list = [i.strip(",") for i in lex]
        ret_list.append(curly_braces.group())
        return ret_list


class HBNBConsole(cmd.Cmd):
    """Implements the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, args):
        """Exit the program."""
        return True

    def do_EOF(self, args):
        """Handle EOF signal."""
        print("")
        return True

    def do_create(self, args):
        """Create a new object instance."""
        arg_list = parse_arguments(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBConsole.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, args):
        """Display object details."""
        arg_list = parse_arguments(args)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBConsole.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, args):
        """Delete an object."""
        arg_list = parse_arguments(args)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBConsole.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, args):
        """Display all objects."""
        arg_list = parse_arguments(args)
        if len(arg_list) > 0 and arg_list[0] not in HBNBConsole.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, args):
        """Count objects."""
        arg_list = parse_arguments(args)
        count = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, args):
        """Update object attributes."""
        arg_list = parse_arguments(args)
        obj_dict = storage.all()

        if len(arg_list) == 0


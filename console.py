#!/usr/bin/python3
"""module for HBNBCommand(cmd.Cmd)"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """prompt for comand interpretor"""

    prompt = 'hbnb '

    def do_quit(self, arg):
        """to exit the program"""
        return True

    def do_EOF(self, arg):
        """to exit the program"""
        print("")
        return True

    def emptyline(self):
        """shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class
        name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name
        """
        args = arg.split()
        if args:
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            else:
                objs = [obj for obj in storage.all().values()
                        if obj.__class__.__name__ == args[0]]
                print([str(obj) for obj in objs])
        else:
            print([str(obj) for obj in storage.all().values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 4:
            print("** arguments missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                attr_name = args[3]
                attr_val = args[4].strip('"')
                try:
                    attr_val = type(getattr(instance, attr_name))(attr_val)
                except AttributeError:
                    print("** attribute name missing **")
                else:
                    setattr(instance, attr_name, attr_val)
                    instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

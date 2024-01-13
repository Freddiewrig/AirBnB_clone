#!/usr/bin/python3
"""module for HBNBCommand(cmd.Cmd)"""
import cmd
from shlex import split
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """prompt for comand interpretor"""
    
    prompt = 'hbnb '
    __classes = {
        'BaseModel',
        'User',
        'City',
        'Amenity',
        'Place',
        'Review',
        'State',
    }

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
        class_name = args[0]
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        class_name = args[0].strip()
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_id = args[1].strip()
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        args = arg.split()
        class_name = args[0].strip()
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_id = args[1].strip()
            key = "{}.{}".format(class_name, instance_id)
            all_instances = storage.all
            if key in all_instances:
                del all_instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        if args and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if args and args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif not args:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj =objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for e, v in eval(args[2]).items():
                if(e in obj.__class__.__dict__.keys() and
                   type(obj.__class__.__dict__[e]) in
                   {str, int, float}):
                    valtype = type(obj.__class__.__dict__[e])
                    obj.__dict__[e] = valtype(v)
                else:
                    obj.__dict__[e] = v
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
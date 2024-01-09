#!/usr/bin/python3
"""module for HBNBCommand(cmd.Cmd)"""
import cmd


class HBNBCommand(cmd.Cmd):
    """prompt for comand interpretor"""
    
    prompt = 'hbnb'

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
if __name__ == '__main__':
    HBNBCommand().cmdloop()
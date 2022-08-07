#!/usr/bin/python3
""" The console module 
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ A command line console
    """
    prompt = '(hbnb) '
    class_list = []

    def emptyline(self):
        """ Does nothing when an empty line + Enter is clicked
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True
    
    def do_EOF(self, arg):
        """When EOF commands are called
        """
        return True
    
    def do_create(self, arg):
        """ Creates a new instance of BaseModel
        """
        if (len(arg) == 0):
            print("** class name missing **")
        elif (arg not in HBNBCommand.class_list):
            print("** class doesn't exist **")
        else:
            new_base = BaseModel()
            print(new_base.id)

    def do_show(self, arg):
        """ prints the string representation of an instance
        """
        if (len(arg) == 0):
            print("** class name missing **")
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()

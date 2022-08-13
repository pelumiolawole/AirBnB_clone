#!/usr/bin/python3
""" The console module 
"""
import cmd
import models

class HBNBCommand(cmd.Cmd):
    """A command line console
    """
    prompt = '(hbnb) '
    instances_of_base_model = []

    def emptyline(self):
        """Does nothing when an empty line + Enter is clicked
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
        """Creates a new instance of BaseModel
        """
        if (arg is None or len(arg) == 0):
            print("** class name missing **")
        elif (arg not in HBNBCommand.instances_of_base_model):
            print("** class doesn't exist **")
        else:
            new_base = models.base_model.BaseModel()
            new_base.save()
            print(new_base.id)

    def do_show(self, line):
        """ prints the string representation of an instance
        """
        arg = line.split()
        if (line is None or len(line) == 0):
            print("** class name missing **")
        elif (arg[0] not in HBNBCommand.instances_of_base_model):
            print("** class doesn't exist **")
        elif (len(arg) < 2 ):
            print(" instance id missing")
        else:
            obj_dict =  models.storage.all()
            
        
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
""" 
This is the console or commandline interpreter's
definition file
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ 
    This is HBNBCommand class of the console
    for the airbnb_clone project 
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ 
        This is the quit method of the 
        HBNBCommand class
        """
        return True

    def do_EOF(self, arg):
        """ 
        This is the EOF method of the 
        HBNBCommand class
        """
        print()
        return True

    # def do_help(self, arg):
    #     """ 
    #     This is the help method of the 
    #     HBNBCommand class
    #     """
    #     print("This is the help documentation")

    def help_quit(self):
        """ 
        This is the help_quit method of the 
        HBNBCommand class
        """
        print("Quit command to exit the program")

    def empty_line(self):
        """ 
        This is the empty line method of the 
        HBNBCommand class. Empty line + ENTER shouldn't execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

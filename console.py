#!/usr/bin/python3
"""
This is the console or commandline interpreter's
definition file
"""
import cmd
import models
from models.base_model import BaseModel


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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        save it, and print the id
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instance_key = f"{class_name}.{instance_id}"
        all_objects = models.storage.all()

        if instance_key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[instance_key])

    def valid_class_names(self):
        """Return a list of valid class names"""
        return ["BaseModel"]


if __name__ == '__main__':
    HBNBCommand().cmdloop()

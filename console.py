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

    def do_quit(self, argum):
        """
        This is the quit method of the
        HBNBCommand class
        """
        return True

    def do_EOF(self, argum):
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

    def do_create(self, argum):
        """
        Create a new instance of BaseModel,
        save it, and print the id
        """
        argums = argum.split()

        if not argums:
            print("** class name missing **")
            return
        class_name = argums[0]
        if class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, argum):
        """
        Prints the string representation of an instance
        """
        argums = argum.split()

        if not argums:
            print("** class name missing **")
            return
        # argums[0] is the class name
        class_name = argums[0]
        if class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        if len(argums) < 2:
            print("** instance id missing **")
            return
        # argums[1] is the instance id
        instance_id = argums[1]
        instance_key = f"{class_name}.{instance_id}"
        all_objects = models.storage.all()

        if instance_key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[instance_key])

    def do_destroy(self, argum):
        """
        Deletes an instance based on
        class name and class id
        """
        argums = argum.split()

        if not argums:
            print("** class name missing **")
            return
        # argums[0] is the class name
        class_name = argums[0]
        if class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        if len(argums) < 2:
            print("** instance id missing **")
            return
        # argums[1] is the instance id
        instance_id = argums[1]
        instance_key = f"{class_name}.{instance_id}"
        all_objects = models.storage.all()

        if instance_key not in all_objects:
            print("** no instance found **")
            return

        del all_objects[instance_key]
        models.storage.save()

    def do_all(self, argum):
        """
        Print string representations of all instances
        Filter to get only the ones that begin with the
        class name.id
        """
        class_name = argum.strip()

        if class_name and class_name not in self.valid_class_names():
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        # if class_name:
        #     filtered_objs = [str(obj) for key, obj in all_objects.items(
        #     ) if key.startswith(class_name + ".")]
        # else:
        #     filtered_objs = [str(obj) for obj in all_objects.values()]
        if class_name:
            for key, obj in all_objects.items():
                if key.startswith(class_name + "."):
                    filtered_objs = str(obj)
        else:
            for obj in all_objects.values():
                filtered_objs = str(obj)

        print(filtered_objs)

    def valid_class_names(self):
        """Return a list of valid class names"""
        return ["BaseModel"]


if __name__ == '__main__':
    HBNBCommand().cmdloop()

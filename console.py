#!/usr/bin/env python3

"""
This is a simple console application that will allow the user to interact with
the models of the application
"""
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """
    This is a simple console application that will allow the user to interact
    with the
    """

    prompt = "(hbnb) "

    def do_quit(self, _):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, _):
        """
        EOF command to exit the program
        """
        return True

    # Handle blank lines
    def emptyline(self):
        """
        Empty line command to do nothing
        """
        pass

    def do_create(self, arg):
        """
        Create command to create a new instance of a class and print the id if
        the class exists
        """
        from models import available_models

        if not arg:
            print("** class name missing **")
        elif arg not in available_models:
            print("** class doesn't exist **")
        else:
            new_instance = available_models[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show command to print the string representation of an instance based on
        the class name and id
        """
        from models import available_models, storage

        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in available_models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance based on the class name and id
        """
        from models import available_models, storage

        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in available_models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        All command to print all string representation of all instances based
        on the class name
        """
        from models import available_models, storage

        args = arg.split()
        if args[0] not in available_models:
            print("** class doesn't exist **")
        else:
            print(
                [
                    str(value)
                    for key, value in storage.all().items()
                    if key.split(".")[0] == args[0]
                ]
            )

    def do_update(self, arg):
        """
        Update command to update an instance based on the class name and id
        """
        from models import available_models, storage

        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in available_models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            instance = storage.all()[key]
            setattr(instance, args[2], args[3])
            instance.save()

    def do_count(self, arg):
        """
        Count command to count the number of instances of a class
        """
        from models import available_models, storage

        args = arg.split()
        if args[0] not in available_models:
            print("** class doesn't exist **")
        else:
            print(
                len(
                    [
                        key
                        for key in storage.all()
                        if key.split(".")[0] == args[0]
                    ]
                )
            )

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        dot_index = arg.find(".")
        if dot_index != -1:
            argl = [arg[:dot_index], arg[dot_index + 1:]]
            open_paren_index = argl[1].find("(")
            close_paren_index = argl[1].find(")")
            if (
                open_paren_index != -1
                and close_paren_index != -1
                and open_paren_index < close_paren_index
            ):
                command = [
                    argl[1][:open_paren_index],
                    argl[1][open_paren_index + 1: close_paren_index],
                ]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))


if __name__ == "__main__":
    HBNBCommand().cmdloop()

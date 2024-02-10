#!/uar/bin/env python

"""
This is a simple console application that will allow the user to interact with
the models of the application
"""
import cmd


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
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

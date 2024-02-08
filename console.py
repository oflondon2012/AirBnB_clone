#!/uar/bin/env python

"""
This is a simple console application that will allow the user to interact with
the
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This is a simple console application that will allow the user to interact
    with the
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

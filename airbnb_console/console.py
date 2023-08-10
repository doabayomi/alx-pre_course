#!/usr/bin/python3
"""A simple console script."""
import cmd
from models import storage
from models.base_model import BaseModel
import string


class HBNBCommand(cmd.Cmd):
    """TestShell for console.

    Args:
        cmd (object): Command interpreter object
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Handle the empty line condition."""
        pass

    def do_create(self, arg):
        """Create a instance of a class.

        Usage:
            create <className>
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = eval(arg)()
            print({}.format(new_model.id))
            storage.save()

    def do_show(self, arg):
        """Show the string representation of an instance.

        Usage:
            show <className> <instance_id>
        """
        args = arg.split()
        arg_rep = "{}.{}".format(args[0], args[1])
        object_list = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif arg_rep not in object_list:
            print("** no instance found **")
        else:
            print("{}". format(arg_rep))

    def do_destroy(self, arg):
        """Destroy a class instance.

        Usage:
            destroy <className> <instance_id>
        """
        args = arg.split()
        arg_rep = "{}.{}".format(args[0], args[1])
        object_list = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif arg_rep not in object_list.keys():
            print("** no instance found **")
        else:
            object_list.pop(arg_rep)
            storage.save()

    def do_all(self, arg):
        """Print the string representation of all instances of a class.

        Usage:
            all <className> OR all
        """
        final_list = list()
        object_list = storage.all()
        if (len(arg) > 0):
            if (arg != "BaseModel"):
                print("** class doesn't exist **")
        else:
            for instance in object_list.values():
                if (len(arg) > 0 and arg == instance.__class__.__name__):
                    final_list.append(instance.__str__)
                elif len(arg) == 0:
                    final_list.append(instance.__str__)
            print(final_list)

    def do_update(self, arg):
        """Update an attribute of an instance.

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        arg_rep = "{}.{}".format(args[0], args[1])
        object_list = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif arg_rep not in object_list.keys():
            print("** no instance found **")
            return False
        elif len(args) == 2:
            print("** attribute name missing **")
            return False
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except Exception:
                print("** value missing **")
                return False

        obj = object_list["{}.{}".format(args[0], args[1])]
        if len(args) == 4:
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()


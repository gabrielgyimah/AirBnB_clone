#!/usr/bin/python3
# Entry point of this AirBnB Application

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    class_names = ["BaseModel", "User", "City", "Review",
                   "Place", "State", "Amenity"]

    def do_quit(self, line):
        return True

    def help_quit(self):
        # Help handler for the quit method
        print('\n'.join(['Exits the program']))
        print()

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        # Help handler for the quit method
        print('\n'.join(['Exits the program']))
        print()

    def emptyline(self):
        pass

    def help_emptyline(self):
        # Help handler for the quit method
        print('\n'.join(['Returns an empty line']))
        print()

    def do_create(self, line):
        # Creates a new instance of the BaseModel

        if not line:
            print("** class name missing **")
        else:
            line = line.lower()
            class_names = [class_name.lower()
                           for class_name in self.class_names]
            if line.lower() in class_names:
                obj = BaseModel()
                storage.new(obj)
                storage.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def help_create(self):
        # Help handler for the create method
        print(
            '\n'.join(
                ['Creates a new instance of the BaseModel']))
        print()

    def do_show(self, line):
        # Prints the string representation
        # of an instance based on the class
        # name and id
        if not line:
            print("** class name missing **")

        else:
            split_line = line.split(" ")
            try:
                line, id = split_line[0], split_line[1]
                line = line.lower()
                class_names = [class_name.lower()
                               for class_name in self.class_names]

                if line not in class_names:
                    print("** class doesn't exist **")
                else:
                    file_path = storage.get_file
                    with open(file_path, "r", encoding="UTF-8") as file:
                        data = file.read()

                    data = json.loads(data)
                    full_id = f"{line}.{id}"
                    found = False

                    for key, object in data.items():
                        if key.lower() == full_id:
                            found = True
                            name = object['__class__']
                            base = eval(f"{name}(**object)")
                            print(base)

                    if found is False:
                        print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def help_show(self):
        print("Prints the string representation of an instance\n")

    def do_destroy(self, line):
        # Prints the string representation
        # of an instance based on the class
        # name and id
        if not line:
            print("** class name missing **")

        else:
            split_line = line.split(" ")
            try:
                line, id = split_line[0], split_line[1]
                line_main = line

                line = line.lower()
                class_names = [class_name.lower()
                               for class_name in self.class_names]

                if line not in class_names:
                    print("** class doesn't exist **")
                else:
                    file_path = storage.get_file
                    with open(file_path, "r", encoding="UTF-8") as file:
                        data = file.read()

                    data = json.loads(data)
                    full_id = f"{line_main}.{id}"

                    if full_id in [id for id in data]:
                        del data[full_id]
                        with open('file.json', "w", encoding="UTF-8") as file:
                            json.dump(data, file, indent=8)

                    else:
                        print("** no instance found **")
            except Exception:
                print("** Invalid number of arguments **")

    def help_destroy(self):
        print("Deletes an instance based on the class name\n")

    def do_all(self, line=None):
        # Prints all string representation
        # of all instances based or not on the
        # class name
        with open(storage.get_file, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        if line:
            line = line.split(" ")

            for line_item in line:
                item_exist = False
                for class_name in self.class_names:
                    if line_item.lower() == class_name.lower():
                        item_exist = True
                        class_found = class_name
                if item_exist:
                    for id, obj in data.items():
                        if obj['__class__'] == class_found:
                            base = eval(f"{class_found}(**obj)")
                            print(base)
                else:
                    print("** class doesn't exist **")
        else:
            for id, obj in data.items():
                base = eval(f"{obj['__class__']}(**obj)")
                print(base)

    def help_all(self):
        # Help documentation handler for do_all method
        print("Prints all string representation of all instances\n")

    def do_update(self, line):
        # Updates an instance based on the
        # class name and id by adding or
        # updating attribute
        # (save the change into the JSON file)

        if not line:
            print("** class name missing **")
        else:
            capture_value = line.split("\"")
            line = line.split(" ")
            try:
                frm_line_class, frm_line_id = line[0], line[1]
                frm_line_att = line[2]
                class_found = ""
                if not frm_line_class:
                    print("** class name missing **")
                elif not frm_line_id:
                    print("** instance id missing **")
                elif not frm_line_att:
                    print("** attribute name missing **")
                elif not capture_value[1]:
                    print("** value missing **")
                else:
                    pass
            except Exception:
                pass

            for class_name in self.class_names:
                if frm_line_class.lower() == class_name.lower():
                    class_found = class_name

            if not class_found:
                print("** class doesn't exist **")
            else:
                try:
                    with open(storage.get_file, 'r', encoding='UTF-8') as file:
                        data = json.load(file)
                    try:
                        got_id = False
                        id_found = ""

                        for id in data:
                            id_split = id.split(".")
                            if id_split[1].lower() == frm_line_id.lower():
                                got_id = True
                                id_found = id
                        if not got_id:
                            print("** no instance found **")
                        else:
                            # if frm_line_att in data[id_found]:
                            #     del data[id_found][frm_line_att]
                            print(type(data[id_found][frm_line_att]))
                            # data[id_found][frm_line_att] = capture_value[1]
                            # returning_data = data

                            # try:
                            #     with open(
                            # storage.get_file, 'w',
                            # encoding='UTF-8')
                            # as file:
                            #         json.dump(returning_data, file, indent=8)
                            # except Exception:
                            #     pass
                    except Exception:
                        pass

                except Exception:
                    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

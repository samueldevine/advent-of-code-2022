from typing import List

with open("inputs/day_07.txt") as input_file:
    commands = input_file.readlines()


class Directory:
    def __init__(self, level: int, name: str, parent):
        self.level = level
        self.name = name
        self.nested_directories = []
        self.files = {}
        self.parent = parent

    def __repr__(self):
        return self.name

    def add_nested(self, dir):
        self.nested_directories.append(dir)

    def add_file(self, name: str, size: int):
        self.files[name] = size

    def calculate_size(self):
        return self.sum_of_files() + self.sum_of_nested_directories()

    def sum_of_files(self):
        return sum(self.files.values())

    def sum_of_nested_directories(self):
        sum = 0
        for dir in self.nested_directories:
            sum += dir.calculate_size()
        return sum


def directories():
    directories: List[Directory] = []
    level: int = 0
    cwd: Directory = None

    for command in commands:
        if command[0:7] == "$ cd ..":
            cwd = cwd.parent
            level -= 1
        elif command[0:5] == "$ cd ":
            new_dir = Directory(level, command[5:-1], cwd)
            if cwd is not None:
                cwd.add_nested(new_dir)
            directories.append(new_dir)
            cwd = new_dir
            level += 1
        elif command[0:4] != "$ ls" and command[0:3] != "dir":
            (size, name) = command.split(" ")
            cwd.add_file(name.strip(), int(size))

    return directories


dir_list = directories()
filtered_directories = {}
for dir in dir_list:
    size = dir.calculate_size()
    if size < 100000:
        filtered_directories[dir] = size

print(sum(filtered_directories.values()))

# part 2
total_disk_space = 70000000
required_for_update = 30000000

unfiltered_directories = {}
for dir in dir_list:
    size = dir.calculate_size()
    unfiltered_directories[dir] = size

free_space = total_disk_space - 42586708
deletion_threshold = required_for_update - free_space

dir_to_delete = None
for dir in unfiltered_directories:
    if dir_to_delete is None:
        dir_to_delete = dir

    if (
        dir.calculate_size() > deletion_threshold
        and dir.calculate_size() < dir_to_delete.calculate_size()
    ):
        dir_to_delete = dir

print(free_space)
print(deletion_threshold)
print(dir_to_delete)
print(dir_to_delete.calculate_size())

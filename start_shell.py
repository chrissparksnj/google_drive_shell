import json
import goog_shell
import directions
instructions = directions.directions()
shell = goog_shell.goog_shell()

print "Type h for available options: "

while True:
    user_command = raw_input('>> ')
    if user_command == 'h':
        instructions.help_goog()
    if 'ls' in user_command:
        if user_command.split()[0] == "lls":
            pass
        else:
            shell.list_directory()
    if 'cd' in user_command:
        if user_command == "lcd":
            pass
        if len(user_command.split()) < 2:
            target_dir = 'root'
        else:
            target_dir = user_command.split()[1]
        shell.change_directory(target_dir)
    if 'get' in user_command:
        if len(user_command.split()) < 2:
            print "Please specify file descriptor. EG: get 1"
        if len(user_command.split()) == 2:
            file_descriptor = user_command.split()[1]
            shell.get_file(file_descriptor)
    if user_command == "lls":
        shell.local_list()
    if user_command == "lcd":
        directory = user_command.split()[1]
        shell.local_change_dir(directory)
    if user_command == "lpwd":
        shell.localcwd()
    if user_command == "downloadall":
        shell.get_all()
    if "rename" in user_command:
        if len(user_command.split()) == 1:
            print "Please select old file, and supply new name. EG: 0 newfile.txt"
        else:
            originalfile = user_command.split()[1]
            newfile = user_command.split()[2]
            shell.rename(originalfile, newfile)
    if user_command == "exit":
        exit(0)
        
            
        
    



import json
import goog_shell
import directions
instructions = directions.directions()
shell = goog_shell.goog_shell()

print " 'h' for available options "
print " 'see'  for examples "
print " 'exit' to quit"


while True:
    user_command = raw_input('>> ')
    if user_command == 'h':
        instructions.help_goog()
    if user_command == 'see':
        instructions.see()
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
    if "remove" in user_command:
        if len(user_command.split()) < 2:
            print "You must specify file to delete"
        else:
            target_file = user_command.split()[1]
            remove_prompt = raw_input("Are you sure you want to delete the following file? y or n: {} ".format(int(target_file)))
            if remove_prompt == "y":
                shell.remove(target_file)
            else:
                print "Failed to remove file: user selected n at prompt"
    if "deleteall" in user_command:
        remove_prompt = raw_input("Are you sure you want to delete all files in this directory?: y or n")
        if remove_prompt == "y":
            shell.remove_all()
        else:
            print "Failed to initiate destruction: user selected n at prompt"
                
    if user_command == "exit":
        exit(0)
        
            
        
    



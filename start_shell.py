#!/usr/bin/python
import readline
import json
import goog_shell
import directions
import os
instructions = directions.directions()
shell = goog_shell.goog_shell()

print " 'h' for available options "
print " 'see'  for examples "
print " 'exit' to quit"



while True:
    try:
        readline.parse_and_bind("tab: complete")
        readline.set_completer(shell.complete)
        user_command = raw_input('>> ')
        tokenized = user_command.split()
        token_one = user_command.split()[0]
        if token_one == 'h':
            instructions.help_goog()
        if token_one == "see":
            instructions.see()
        if token_one == "ls":
                shell.list_directory()
        if token_one == "clear":
            os.system('clear')
        if token_one == "cd":
            if len(user_command.split()) < 2: 
                shell.change_directory('root')
            else:
                try:
                    input_command = user_command.split()[1]
                    shell.change_directory(input_command)
                except:
                    print "Ensure file descriptor is a number"
        if token_one == "get":
            if len(user_command.split()) < 2:
                print "Please specify file descriptor. EG: get 1"
            if len(user_command.split()) == 2:
                file_descriptor = user_command.split()[1]
                shell.get_file(file_descriptor)
        if token_one == "lls":
            shell.local_list()
        if token_one == "lpwd":
            shell.localcwd()
        if token_one == "downloadall":
            shell.get_all()
        if token_one == "lcd":
            shell.local_change_dir(tokenized[1])
        if token_one == "pwd":
            shell.print_working_directory()
        if token_one == "rename":
            if len(user_command.split()) == 1:
                print "Please select old file, and supply new name. EG: 0 newfile.txt"
            else:
                originalfile = user_command.split()[1]
                newfile = user_command.split()[2]
                shell.rename(originalfile, newfile)
        if token_one == "rm":
            if len(user_command.split()) < 2:
                print "You must specify file to delete"
            else:
                target_file = user_command.split()[1]
                remove_prompt = raw_input("Are you sure you want to delete the following file? y or n: {} ".format(target_file))
                if remove_prompt == "y":
                    shell.remove(target_file)
                else:
                    print "Failed to remove file: user selected n at prompt"
        if token_one == "deleteall":
            remove_prompt = raw_input("Are you sure you want to delete all files in this directory?: y or n")
            if remove_prompt == "y":
                shell.remove_all()
            else:
                print "Failed to initiate destruction: user selected n at prompt"
        if token_one == "upload":
            if len(user_command.split()) < 2:
                print "Please specify the filename"
            else:
                file_name = user_command.split()[1]
                shell.upload(file_name)
        if token_one == "touch":
            if len(user_command.split()) < 2:
                print "Please add a file name for your new file: eg 'touch test.txt'"
            else:
                file_name = user_command.split()[1]
                shell.touch(file_name)
        if token_one == "cat":
            if len(user_command.split()) < 2:
                print "Please enter file number to see its contents"
            else:
                shell.cat(user_command.split()[1])
        if token_one == "mkdir":
            if len(user_command.split()) < 2:
                print "Please specify a file name: eg 'mkdir testfolder'"
            else:
                shell.make_directory(user_command.split()[1])
        if token_one == "rmdir":
            shell.rmdir(user_command.split()[1])
        if token_one == "exit":
        
            exit(0)
    except Exception, e:
        print "Error written in error.log"
        print e
        f = open('error.log', 'wa+')
        f.write("Usercommand: " + user_command + "\n")
        f.write("Error message: " + str(e) + "\n")
        f.write("-----------------------" + "\n")
        f.close()
        
            
        
    



class directions:

    def help_goog(self):
        print "'ls'                   <-- lists files in current directory"
        print "'cd <directory_name>'          <-- changes directory. Use the pre-pended number. EG: cd 0"
        print "'cd ..'                <-- moves back one directory"
        print "'get <filename>          <-- downloads specific file"
        print "'downloadall'          <-- downloads all files in current directory"
        print "'rename <filename> <new> <-- renames files"
        print "'remove <filename>       <-- removes single file"
        print "'deleteall'            <-- deletes all files in current working directory"
        print "'see'                  <-- shows examples of how to use commands"
        print "'lpwd'                 <-- prints local working directory"
        print "'lls'                  <-- lists local directory"
        print "'lcd <directory_name>' <-- changes local directory"
        print "'upload <filename>     <-- uploads local file to drive"
        print 'rmdir <directory name> <-- removes directory'
  
    def see(self):
        print "cd:  cd 3"
        print "get: get 4"
        print "remove: remove 4"
        print "'deleteall'"
        print "lcd : lcd /"
        print "upload: upload file_name.txt"
        print "rename: rename 0 newfile.txt"
        print "rmdir: rmdir folder"

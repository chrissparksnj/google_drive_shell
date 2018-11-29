class directions:

    def help_goog(self):
        print "'ls'                   <-- lists files in current directory"
        print "'cd <number>'          <-- changes directory. Use the pre-pended number. EG: cd 0"
        print "'cd ..'                <-- moves back one directory"
        print "'get <number>          <-- downloads specific file"
        print "'downloadall'          <-- downloads all files in current directory"
        print "'rename <number> <new> <-- renames files"
        print "'remove <number>       <-- removes single file"
        print "'deleteall'            <-- deletes all files in current working directory"
        print "'see'                  <-- shows examples of how to use commands"
        print "'lpwd'                 <-- prints local working directory"
        print "'lls'                  <-- lists local directory"
        print "'lcd <filename>'       <-- changes local directory"
  
    def see(self):
        print "cd:  cd 3"
        print "get: get 4"
        print "remove: remove 4"
        print "'deleteall'"
        print "lcd : lcd /"
        print "rename: rename 0 newfile.txt"

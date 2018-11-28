class directions:

    def help_goog(self):
        print "'ls'                   <-- lists files in current directory"
        print "'cd <number>'          <-- changes directory. Use the pre-pended number. EG: cd 0"
        print "'cd ..'                <-- moves back one directory"
        print "'get <number>          <-- downloads specific file"
        print "'downloadall'          <-- downloads all files in current directory"
        print "'rename <number> <new> <-- renames files"
        print "'see'                  <-- shows examples of how to use commands"
  
    def see(self):
        print "cd:  cd 3"
        print "get: get 4"
        print "rename: rename 0 newfile.txt"

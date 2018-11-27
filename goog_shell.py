import os

class goog_shell:

    place_holder_dict = {}
    folder_list = []
    files_list = []
    last_dir = ''
    current_dir = 'root'
    mimetype_dict = {
        "application/vnd.google-apps.document" : 'application/pdf',
        'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        }

    def __init__(self):
        from pydrive.drive import GoogleDrive
        from pydrive.auth import GoogleAuth 
        self.gauth = GoogleAuth()
        self.drive = GoogleDrive(self.gauth) 
        self.gauth.LocalWebserverAuth()
        
        

    def list_directory(self):
        file_list = self.drive.ListFile({'q':"'{}' in parents".format(self.current_dir)}).GetList()
            
        for file1 in file_list:
            # list folders and files differently
            if file1['mimeType'] == "application/vnd.google-apps.folder":
                self.folder_list.append(file1['title'])
                print "[{}] folder: {}".format(self.folder_list.index(file1['title'].encode("utf-8")), file1['title'].encode("utf-8"))

            else:
                self.files_list.append(file1['title'])
                print "[{}] file: {}".format(self.files_list.index(file1['title']),file1['title'].encode("utf-8"))
                
            self.place_holder_dict[file1['title']] = file1['id']

    def change_directory(self, target_dir):
        """ Target dir will be a number """
        # goes back one file with .. 
        if target_dir == '..':
            self.current_dir = self.last_dir
            self.last_dir = '';
            return;
        if target_dir == 'root':
            self.current_dir = 'root'
            self.last_dir = ''
            return
        
        # set current dir to last dir
        self.last_dir = self.current_dir

        #enter current dir
        """ uses index passed by user to look up name in folder_list """
        """ uses name to get ID in place_holder_list """
        self.current_dir = self.place_holder_dict[self.folder_list[int(target_dir)]]
        
    def get_file(self, target_file):
        target_file = self.files_list[int(target_file)]
        file_id = self.place_holder_dict[target_file]
        created_file = self.drive.CreateFile({'id': file_id})
        print "Downloading {}".format(target_file.encode('utf-8'))
        try:
            created_file.GetContentFile("files/" + target_file)
        except:
            mime_type = self.mimetype_dict[created_file['mimeType']]
            created_file.GetContentFile("files/" + target_file, mimetype=mime_type)

    def local_list(self):
        cur_dir = os.listdir('.')
        for file1 in cur_dir:
            print file1

    def local_change_dir(self, directory):
        os.chdir(directory)

    def localcwd(self):
        print os.getcwd()

    def get_all(self):
        file_list = self.drive.ListFile({'q':"'{}' in parents".format(self.current_dir)}).GetList()
        
        for file1 in file_list:
            created_file = self.drive.CreateFile({'id': file1['id']})
            try:
                created_file.GetContentFile("files/" + file1['title'])
                print "Downloading: {}".format(file1['title'].encode('utf-8'))
            except:
                mime_type = self.mimetype_dict[created_file['mimeType']]
                created_file.GetContentFile("files/" + target_file, mimetype=mime_type)
                print "Downloading: {}".format(file1['title'].encode('utf-8'))
            if file1['mimeType'] == "application/vnd.google-apps.folder":
                print "Ignoring folder"

            

            

        
        

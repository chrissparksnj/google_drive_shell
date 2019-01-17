import os

class goog_shell:

    place_holder_dict = {}
    folder_list = []
    files_list = []

    folders_dict = {}
    files_dict = {}  # stored like: {'linux advanced.zip': u'19eN8iy1jJzcICyDz8rLsiivrhb7izv2D'}

    reverse_folders_dict = {}
    reverse_files_dict = {} # stored like: {'19eN8iy1jJzcICyDz8rLsiivrhb7izv2D': u'linux advanced.zip'}

    last_dir = ''
    current_dir = 'root'
    mimetype_dict = {
        "application/vnd.google-apps.document" : 'application/pdf',
        'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        }
    mimetype_reverse = {
        'application/pdf' : "application/vnd.google-apps.document",
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' : 'application/vnd.google-apps.spreadsheet'
    }

    def __init__(self):
        from pydrive.drive import GoogleDrive
        from pydrive.auth import GoogleAuth 
        self.gauth = GoogleAuth()
        self.drive = GoogleDrive(self.gauth) 
        self.gauth.LocalWebserverAuth()
        self.load_files_into_memory()
    
    def print_working_directory(self):
        print self.current_dir

    def complete(self, text, state):
        files = self.files_list
        results = [x for x in files if x.startswith(text)] + [None]
        return results[state]
    
    def convert(self, file_descriptor):
        ''' takes user input in form of int, gets name, and uses name to get id from dict'''
        file_title = self.files_list[int(file_descriptor)] # returns file title: "Untitled spreadsheet"
        file_id = self.place_holder_dict[file_title]       # returns file id: 1TKD2I5uMq9ExzT0WQLS2q6WeQOLT7zl-KaZF1_elpnE
        return file_id
    
    def load_files_into_memory(self):
        file_list = self.drive.ListFile({'q':"'{}' in parents".format(self.current_dir)}).GetList()
        for file1 in file_list:
            self.files_dict[file1['mimeType']] = file1['title']
            if file1['mimeType'] == "application/vnd.google-apps.folder":
                self.folder_list.append(file1['title'])
                self.folders_dict[file1['title']] = file1['id']
                self.reverse_folders_dict[file1['id']] = file1['title']
            else:
                self.files_list.append(file1['title'])
                self.files_dict[file1['title']] = file1['id']
                self.reverse_files_dict[file1['id']] = file1['title']

        print self.files_dict
        print self.reverse_files_dict

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
            return
        if target_dir == 'root':
            self.current_dir = 'root'
            self.last_dir = ''
            return
        
        # set current dir to last dir
        self.last_dir = self.current_dir

        #enter current dir
        """ uses index passed by user to look up name in folder_list """
        """ uses name to get ID in place_holder_list """
        # self.current_dir = self.place_holder_dict[self.folder_list[int(target_dir)]]
        self.current_dir = self.folders_dict[target_dir]
           
    def get_file(self, target_file):
        file_id = self.files_dict[target_file]
        created_file = self.drive.CreateFile({'id': file_id})
        print "Downloading {}".format(target_file.encode('utf-8'))
        try:
            created_file.GetContentFile("files/" + target_file)
        except:
            mime_type = self.mimetype_reverse[created_file['mimeType'].encode('utf-8')]
            created_file.GetContentFile("files/" + target_file, mimetype = mime_type)
            
    def local_list(self):
        cur_dir = os.listdir('.')
        for file1 in cur_dir:
            print file1

    def local_change_dir(self, directory):
        root = os.getcwd()
        target_dir = root + "/" + directory
        print target_dir
        os.chdir(target_dir)

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

    def rename(self, target_file, new_name):

        """ Look up target file in files list by index """
        file_title = self.files_list[int(target_file)] # returns file title: "Untitled spreadsheet"

        """ Take target file name and get ID out of place_holder_dict """ # returns file id: 1TKD2I5uMq9ExzT0WQLS2q6WeQOLT7zl-KaZF1_elpnE
        file_id = self.place_holder_dict[file_title]

        """ Create file instance """
        a = self.drive.auth.service.files().get(fileId=file_id).execute()
        a['title'] = new_name
        self.drive.auth.service.files().update(fileId=file_id,body=a).execute()

    def remove(self, target_file):
        file_title = self.files_list[int(target_file)]
        file_id = self.place_holder_dict[file_title]
        a=self.drive.auth.service.files().delete(fileId=file_id).execute()
        print "Deleted File: {}".format(file_title.encode('utf-8'))

    def remove_all(self):
        file_list = self.drive.ListFile({'q':"'{}' in parents".format(self.current_dir)}).GetList()
        for file1 in file_list:
            file_id = file1['id']
            a=self.drive.auth.service.files().delete(fileId=file_id).execute()
            print "Deleted file: {}".format(file1['title'].encode('utf-8'))
    
    def upload(self, file_name):
        ''' takes name of file you want to upload: eg upload('file.txt') '''
        url = os.getcwd()
        full_url = str(url) + "/" + str(file_name)
        file1 = self.drive.CreateFile({'title':file_name})
        file1.SetContentFile(full_url)
        file1.Upload()
        print "Uploaded {}".format(full_url.encode('utf-8'))
    
    def touch(self, file_name):
        file1 = self.drive.CreateFile({
            'title': file_name, 
            "parents":[{
                "kind":"drive#fileLink", "id":self.current_dir
                }]
            })
        file1.Upload()
        print "Uploaded {}".format(file_name)

    def cat(self, index):
        file_id = self.convert(index)
        try:
            file1 = self.drive.auth.service.files().get_media(fileId=file_id).execute()
            print file1
        except Exception as e:
            print "Couldn't see contents of file. Try downloading first"
            print "----------------------"
            print e
            print "----------------------"

    def make_directory(self, folder_name):
        folder_metadata = {"title": folder_name,'mimeType' : 'application/vnd.google-apps.folder'}
        folder = self.drive.CreateFile(folder_metadata)
        folder.Upload()
        print "Made new directory: {}".format(folder['title'])



        

        
                

            

            
      
        

import os
from os import path
from datetime import datetime, timedelta

class DeleteFile:

    def __init__(self, path, except_files = ['.gitignore'], days_before = 10):
        self.path = path
        self.except_files = except_files
        self.days_before = int(days_before)
        self.files_to_delete = []

    def exists_path(self):
        return path.exists(self.path)

    def get_files_directory(self):
        files = os.listdir(self.path)
        files_to_delete = []
        # Remove files to except
        for file_to_except in self.except_files:
            if file_to_except in files:
                files.remove(file_to_except)

        # Days to delete
        today = datetime.today()
        today_substract_days = today - timedelta(days=self.days_before)

        # Push Files with subs days
        for name_file in files:
            date_updated = datetime.utcfromtimestamp(os.stat(os.path.join(self.path, name_file)).st_mtime)
            if date_updated < today_substract_days:
                files_to_delete.append((name_file, date_updated))

        self.files_to_delete = files_to_delete

    def delete_files_from_directory(self):
        for file_to_delete in self.files_to_delete:
            print("file to delete >>>", os.path.join(self.path, file_to_delete[0]))
            os.remove(os.path.join(self.path, file_to_delete[0]))



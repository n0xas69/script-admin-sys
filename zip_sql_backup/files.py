class Files:

    def __init__(self, file, c_date):
        self.file = file
        self.c_date = c_date

    def get_file(self):
        return self.file

    def get_date(self):
        return self.c_date
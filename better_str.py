class Better_Str:
    def __init__(self, str2):
        self.str_keep = str2

    def append(self, appending):
        self.str_keep = self.str_keep + appending

    def __repr__(self):
        return self.str_keep
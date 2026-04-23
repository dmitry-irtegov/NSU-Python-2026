class Storage:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def edit(self):
        return StorageEditor(self)


class StorageEditor:
    def __init__(self, storage):
        self.storage = storage
        self.temp = storage.data.copy()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            self.storage.data = self.temp

    def __getitem__(self, key):
        return self.temp[key]

    def __setitem__(self, key, value):
        self.temp[key] = value

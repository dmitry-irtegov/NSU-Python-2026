class _StorageTransaction:
    def __init__(self, draft, commit, rollback):
        self.__draft = draft
        self.__commit = commit
        self.__rollback = rollback

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__commit(self.__draft)
        self.__rollback()

    def __getitem__(self, item):
        return self.__draft[item]

    def __setitem__(self, key, value):
        self.__draft[key] = value

    def __delitem__(self, key):
        del self.__draft[key]


class Storage:
    def __init__(self):
        self.__data = {}
        self.__has_ongoing_transaction = False

    def __getitem__(self, item):
        return self.__data[item]

    def _commit_function(self):
        def commit(draft):
            self.__data = draft
            self.__has_ongoing_transaction = False

        return commit

    def _rollback_function(self):
        def rollback():
            self.__has_ongoing_transaction = False

        return rollback

    def edit(self):
        if self.__has_ongoing_transaction:
            raise RuntimeError("Some transaction already in progress")

        self.__has_ongoing_transaction = True
        return _StorageTransaction(
            self.__data.copy(),
            self._commit_function(),
            self._rollback_function(),
        )

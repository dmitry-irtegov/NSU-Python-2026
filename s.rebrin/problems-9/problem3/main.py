class Directory:
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)

        if callable(attr) and not name.startswith("__"):

            def wrapper(*args, **kwargs):
                d = object.__getattribute__(self, "__dict__")

                name_log = "_Directory__log"

                if name_log not in d:
                    d[name_log] = {}

                if name not in d[name_log]:
                    d[name_log][name] = {"count": 0, "calls": []}

                d[name_log][name]["count"] += 1
                d[name_log][name]["calls"].append({"args": args, "kwargs": kwargs})

                return attr(*args, **kwargs)

            return wrapper

        return attr

    def __str__(self):
        d = object.__getattribute__(self, "__dict__")
        return str(d.get("_Directory__log", {}))

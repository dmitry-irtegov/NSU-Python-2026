class Directory:
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        print(name)

        if callable(attr) and not name.startswith("__"):

            def wrapper(*args, **kwargs):
                d = object.__getattribute__(self, "__dict__")

                if "m" not in d:
                    d["m"] = {}

                if name not in d["m"]:
                    d["m"][name] = {"count": 0, "calls": []}

                d["m"][name]["count"] += 1
                d["m"][name]["calls"].append({"args": args, "kwargs": kwargs})

                return attr(*args, **kwargs)

            return wrapper

        return attr

    def __str__(self):
        d = object.__getattribute__(self, "__dict__")
        return str(d.get("m", {}))

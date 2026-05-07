from sortedDict import SortedDict

if __name__ == "__main__":
    sd = SortedDict[int, int]()

    print("Commands:")
    print("  insert <key> <value>")
    print("  get <key>")
    print("  delete <key>")
    print("  contains <key>")
    print("  keys")
    print("  items")
    print("  quit")
    print()

    while True:
        try:
            line = input("> ").strip().split()
            if not line:
                continue
            cmd = line[0].lower()

            if cmd == "quit":
                break

            elif cmd == "insert":
                if len(line) != 3:
                    print("Использование: insert <key> <value>")
                    continue
                k = int(line[1])
                v = int(line[2])
                sd[k] = v
                print(f"Вставлено: {k}: {v}")

            elif cmd == "get":
                if len(line) != 2:
                    print("Использование: get <key>")
                    continue
                k = int(line[1])
                try:
                    val = sd[k]
                    print(f"Значение: {k}: {val}")
                except KeyError:
                    print(f"Ключ {k} не найден.")

            elif cmd == "delete":
                if len(line) != 2:
                    print("Использование: delete <key>")
                    continue
                k = int(line[1])
                try:
                    del sd[k]
                    print(f"Ключ {k} удалён.")
                except KeyError:
                    print(f"Ключ {k} не найден.")

            elif cmd == "contains":
                if len(line) != 2:
                    print("Использование: contains <key>")
                    continue
                k = int(line[1])
                print(k in sd)

            elif cmd == "keys":
                keys = list(sd)
                print("Ключи:", keys)

            elif cmd == "items":
                items = list(sd.items())
                print("Пары:", items)

            else:
                print("Неизвестная команда. Повторите ввод.")

        except ValueError:
            print("Ошибка: ключ и значение должны быть целыми числами.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
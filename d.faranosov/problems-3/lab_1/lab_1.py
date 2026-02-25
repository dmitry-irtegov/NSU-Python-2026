from typing import List


class Table:
    def __init__(self, lists):
        if not isinstance(lists, list):
            raise TypeError("not a list was given")

        list_size = -1
        for arg in lists:
            if not isinstance(arg, list):
                raise TypeError("list does not consist of lists")
            if list_size == -1:
                list_size = len(arg)
            elif list_size != len(arg):
                raise ValueError("lists with different size")

        self.table = lists
        self.list_size = list_size

    def head(self, cnt:int=1):
        if cnt > len(self.table) or cnt < 0:
            raise ValueError("Cnt lines to return more than lines in table")
        return Table([self.table[l] for l in range(cnt)])

    def tail(self, cnt:int=1):
        if cnt > len(self.table) or cnt < 0:
            raise ValueError("Cnt lines to return more than lines in table")
        return Table([self.table[l] for l in range(len(self.table) - cnt, len(self.table))])

    def get_lines(self, lines_numbers: List[int]):
        res = []
        for line in lines_numbers:
            if not (-1 < line < len(self.table)):
                raise ValueError("line out of index")
            res.append(self.table[line])
        return Table(res)

    def left_line_add(self, other):
        return self.__adding(other, self)

    def right_line_add(self, other):
        return self.__adding(self, other)

    @staticmethod
    def __adding(first,  second):
        if not isinstance(first, Table) or not isinstance(second, Table):
            raise TypeError("Adding with not a table")

        if first.list_size != second.list_size:
            raise ValueError("Adding tables with different lines size")

        return Table(first.table + second.table)

    def left_row_add(self, other):
        return self.__row_adding(other, self)

    def right_row_add(self, other):
        return self.__row_adding(self, other)

    @staticmethod
    def __row_adding(first, second):
        if not isinstance(first, Table) or not isinstance(second, Table):
            raise TypeError("Adding with not a table")

        if len(first.table) != len(second.table):
            raise ValueError("Adding tables with different rows size")

        res = []
        for i, line in enumerate(first.table):
            res.append(line + second.table[i])
        return Table(res)

    def get_rows(self, rows_nums: List[int]):
        res = []
        for index in rows_nums:
            if not (-1 < index < self.list_size):
                raise ValueError("Row index out of range")

        for line in self.table:
            res.append([line[index] for index in rows_nums])

        return Table(res)

    def __eq__(self, other):
        if not isinstance(other, Table):
            raise TypeError("comparing with not a table")

        if len(self.table) != len(other.table) or self.list_size != other.list_size:
            return False

        for i, line in enumerate(self.table):
            check_res = line == other.table[i]
            if not check_res:
                return check_res

        return True



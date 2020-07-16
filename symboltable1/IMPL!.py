class SMBTUnit:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class SMBLTable:
    def __init__(self):
        self.__symbols = []
        pass

    def Add(self, key, val):
        self.__symbols.append(SMBTUnit(key, val))

    def Get(self, key):
        return self.__symbols[key].val

    def Print(self):
        for smbl in self.__symbols:
            print(smbl.key + "  " + str(smbl.val))


if __name__ == "__main__":
    smblTbl = SMBLTable()
    print("Enter the words")
    uip = input()
    cnt = 1
    while uip != "":
        cnt += 1
        smblTbl.Add(uip, cnt)
        uip = input()
    smblTbl.Print();








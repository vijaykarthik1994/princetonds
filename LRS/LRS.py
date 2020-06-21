import  math as mi


def CheckLRS(userinputs):
    lrs = ""
    for i in range(len(userinputs)-1):
        for j in range(i+1, len(userinputs)):
            substr = GetSubString(userinputs[i:len(userinputs)], userinputs[j:len(userinputs)]);
            if len(substr) > len(lrs) :
              lrs = substr
    return lrs


def GetSubString(str1, str2):
    n = min(len(str1), len(str2))
    for i in range(n):
        if str1[:i] != str2[:i] :
            return str1[:i-1]
    return str1[:n]





if __name__ == "__main__":
    userinputs = (input("Enter the sequence"))
    print(CheckLRS(userinputs))







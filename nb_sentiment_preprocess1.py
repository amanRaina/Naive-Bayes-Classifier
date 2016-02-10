import sys


def main():
    with open(sys.argv[2],'w') as outfile:
        with open(sys.argv[1], "r") as infile:
            data = infile.readlines()
            for line in data:
                dat = line.split()
                if dat[0] == "1" or dat[0] == "2" or dat[0] == "3" or dat[0] == "4":
                    outfile.write("NEGATIVE "+line[2:])
                elif dat[0] == "7" or dat[0] == "8" or dat[0] == "9":
                    outfile.write("POSITIVE "+line[2:])
                elif dat[0] == "10":
                    outfile.write("POSITIVE "+line[3:])
        infile.close()
    outfile.close()

if __name__=="__main__":
    main()    
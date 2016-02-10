import sys

def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        with open(sys.argv[2], "w") as op:
            for line in data:
                words = line.split()
                op.write(str(words[0]))
                for word in words[1:]:
                    value=word.split(":")
                    feature=int(value[0])+1
                    op.write(" "+str(feature)+":"+str(value[1]))
                op.write("\n")
            op.close()

if __name__=="__main__":
    main()        

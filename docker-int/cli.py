import sys
import os


def read(file): 
    if os.path.isfile(file): 
        data = []
        with open(file, mode='r', encoding='utf8') as f: 
            while True: 
                line = f.readline()
                if line == '': 
                    break
                data.append(line.strip()[0:len(line)-1])
        f.close()
        return data
    else: 
        return None



def printerr(error): 
    sys.stdout.buffer.write(error.encode(sys.stdout.encoding))
    sys.stdout.buffer.write("\n".encode(sys.stdout.encoding))

def handle(file=None): 
    if os.path.isfile(file): 
        d = read(file)
        for f in d: 
            sys.stdout.buffer.write(f.encode(sys.stdout.encoding))
            sys.stdout.buffer.write("\n".encode(sys.stdout.encoding))
    else: 
        printerr("no file found..")

if __name__ == "__main__":

    #repl here.
    while True: 
        file = input(">> ") 
        handle(file)

    


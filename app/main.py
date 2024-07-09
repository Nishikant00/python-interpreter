import sys
def equality(eql):
    num=eql//2
    rem=eql%2
    ee_arr=""
    e_arr=""
    for i in range(rem):
        e_arr+="EQUAL = null\n"
    for i in range(num):
        ee_arr+="EQUAL_EQUAL == null\n"
    return (ee_arr,e_arr)

def scanner(data):
    tokens = {
        '(': "LEFT_PAREN ( null\n",
        ')': "RIGHT_PAREN ) null\n",
        '{': "LEFT_BRACE { null\n",
        '}': "RIGHT_BRACE } null\n",
        ',': "COMMA , null\n",
        '.': "DOT . null\n",
        '*': "STAR * null\n",
        '+': "PLUS + null\n",
        '-': "MINUS - null\n",
        ';': "SEMICOLON ; null\n",
        '/': "FORWARD_SLASH / null\n",
    }
        
    
    res = ""
    error_code = 0
    lines = 1
    eql=0
    for i,ch in enumerate(data):
        if ch in tokens:
            res += tokens[ch]
        elif ch == '\n':
            lines += 1
        elif ch=='=':
            try:
                if data[i+1]=='=':
                    eql+=1
                else:
                    eql+=1
                    ee_arr,e_arr=equality(eql)
                    eql=0
                    res
                    res+=ee_arr
                    res+=e_arr
            except:
                eql+=1
                ee_arr,e_arr=equality(eql)
                eql=0
                res+=ee_arr
                res+=e_arr

        else:
            error_code = 65
            print(f"[line {lines}] Error: Unexpected character: {ch}", file=sys.stderr)

    print(res + "EOF  null")
    exit(error_code)
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    if file_contents:
        scanner(file_contents)
    else:
        print("EOF  null") 


if __name__ == "__main__":
    main()

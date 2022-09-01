def main():
    client_file = open('clients.txt','r')
    i = 0
    for line in client_file:
        i += 1
        print(str(i) + '. ' + line.rstrip('\n'))

    
main()


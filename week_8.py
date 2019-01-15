def main():
    file_name=input("Enter the name of the file: ")
    infile=open(file_name,'r')
    line=infile.readline()
    line_count=1
    while line:
        print(f"{line_count} {line}",end="")
        line=infile.readline()
        line_count+=1
    infile.close()

main()


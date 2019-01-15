def read_file(input_csv):
    store={}
    infile=open(input_csv,'r')
    line=infile.readline()
    line_count=1
    while line:
        temp_list=line.split(";")
        key=temp_list[0]
        name=temp_list[1]
        phone=temp_list[2]
        email=temp_list[3]
        if len(temp_list)==5:
            skype=temp_list[4]
        else:
            skype=""
        if key not in store:
            store[key]={}
            store[key]["name"]=name
            store[key]["phone"]=phone
            store[key]["email"]=email
            store[key]["skype"]=skype
        line=infile.readline()
        line_count+=1
    infile.close()
    # for k,v in store.items():
    #         print(f"stored fields for {k} are")
    #         for keys,values in v.items():
    #             print(keys,":",values)
    return store

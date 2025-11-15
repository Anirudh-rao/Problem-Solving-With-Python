def RecusriveTable(n,i=1):
    if ( i == 11):
        return
    print(n ,"*", i ,"=", n*i)
    i += 1
    RecusriveTable(n,i)


print(RecusriveTable(15))
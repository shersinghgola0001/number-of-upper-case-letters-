def str_char(s):
    m={"upper_case":0,"lower_case":0}
    for c in s:
        if c.isupper():
           m["upper_case"]+=1
        elif c.islower():
           m["lower_case"]+=1
        else:
           pass
    print("string:-", s)
    print("No. of Upper case char:-",m["upper_case"])
    print("No. of Lower case char:-",m["lower_case"])
str_char('The quick Brow Fox')

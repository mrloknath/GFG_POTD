def compute(head): 
    #return True/False
    s=''
    while head:
        s+=head.data
        head=head.next
    return s==(s[::-1])

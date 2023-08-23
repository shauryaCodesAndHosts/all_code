def reverse(root):
    p=root
    q=None
    r=None
    while(p!=None):
        r=q
        q=p
        p=p.next
        q.next=r
    root=q
    return root
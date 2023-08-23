import pyhtml as h

t = h.html(
    h.head(h.title('Test page')), h.body(h.h1('This is Title'),
                                         h.div('this is some text', h.h2("and it is inside div")))
)
print(t.render())

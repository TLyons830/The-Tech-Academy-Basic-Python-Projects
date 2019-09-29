mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst

lst = color_function('TYLER')
for i in lst:
    print(i)

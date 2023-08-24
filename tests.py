from config import me



def read():
    print(me["name"])


def modify():
    me["age"]=21
    print(me)


def create():
    me["favorite_color"] = "purple"
    print(me)


def remove():
    me["hobbies"].pop()
    print(me)


    #  call functions
read()
modify()
create()
remove()
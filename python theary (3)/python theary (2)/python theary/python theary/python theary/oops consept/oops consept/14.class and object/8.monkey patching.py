
class N():
    def nil():
        print("not a mankey patching")

obj=N()
N.nil()

def jay():
    print("this is monkey patching")

N.nil=jay
print("After monkey patching")
N.nil()    
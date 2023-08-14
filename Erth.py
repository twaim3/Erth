

role = {"deceased": 0, "wife": 1, "husband": 2, "father":3, "mother":4, "gff":5, "gfm":6, 'gmf':7, "gmm":8,
        "son": 9, "daughter": 10, "gSon":11, "gDaughter": 12, "fBrother": 13, "fSister": 14, "hBrother":15,
        "hsister": 16, "siblingM":17, "fbSon":18, "hbSon": 19, "fUncle": 20, "hUncle": 21, "fUncleSon": 22,
        "hUncleSon":23}

status = {"exists":0, "in3idaDivorced": 1, "passed": 2, "devorced": 3, "in3idaFinDivorced": 4}

class Person:
    def __init__(self, role, id, fname, parent, status):
        self.role = role
        self.id = id
        self.fname = fname
        self.parent = parent
        self.status = status
    def __str__(self):
        if self.parent is None:
            return "family name:{} ".format(self.fname)
        else:
            return "{} {}".format(self.fname, self.parent)


class Erth:
    plist = []

    def __init__(self):
        self.roleId = None
    tes = 4
    def erth(self):
        return None
    def block(self):
        print('block')

    def save(self):
        print('save')
    @classmethod
    def load(self, filename):
        try:
            fd = open(filename, "r")
            for l in fd:
                print(l)
        except:
            print("Error: {} file not found".format(filename))



class Deceased(Erth):
    def __init__(self, fname = 'deceased', lname= 'family', tarika=100):
        fam = Person(None, Erth.plist.len(), lname, None, None)
        self.person = Person(role["deceased"], Erth.plist.len(), fam, status["passed"])

    def save(self):
        print('\{')



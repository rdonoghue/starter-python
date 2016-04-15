class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

frank=Person("Frank")

print frank

frank.pet="Fido"

print frank.name

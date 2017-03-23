""" Some class tools and utilities(maybe later)"""

""" Generic Display Tool"""

class AttrDisplay:
    """diplays instance objects with class names and key, value pairs for
    attributes of that instance (not attrs inherited though)"""

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count
            TopTest.count += 2
    class SubTest(TopTest):
        pass

    Wank, Er = TopTest(), SubTest()
    print(Wank)
    print(Er)

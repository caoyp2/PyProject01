
class demo:

    temp = 10

    def testtemp01(self):
        print(self.temp)

    def testtemp02(self):
        self.temp = 20
        print(self.temp)

    def testtemp03(self):
        print(self.temp)

test = demo()
test.testtemp01()
test.testtemp02()
test.testtemp03()


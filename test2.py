class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.setUp()
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert (self.test.wasRun) # assert 값이 예상과 다르면 trace back 발생
        print("test done")

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)
        print("test done")

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()

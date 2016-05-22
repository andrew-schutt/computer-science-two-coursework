from linkedIndexedList import LinkedIndexedList
import unittest

class TestLinkedIndexedList(unittest.TestCase):
    def setUp(self):
        self._lyst = LinkedIndexedList()
        for i in xrange(5):
            self._lyst.append(str(i))

    def test__getItem__(self):
        for i in xrange(5):
            self.assertEquals(self._lyst[i],str(i))
        self._lyst.append(1)
        self.assertEquals(self._lyst[5],1)
        self._lyst.append(True)
        self.assertTrue(self._lyst[6])

    def testIndex(self):
        for i in xrange(5):
            val = self._lyst.index(str(i))
            self.assertEquals(val,i)

    def testZeroRemove(self):
        out = self._lyst.remove(0)
        self.assertEquals(out,"0")
        self.assertEquals(len(self._lyst),4)
        self.assertEquals(self._lyst._head.data,"1")
        self.assertEquals(self._lyst._tail.data,"4")

    def testTailRemove(self):
        out = self._lyst.remove(4)
        self.assertEquals(out,"4")
        self.assertEquals(len(self._lyst),4)
        self.assertEquals(self._lyst._head.data,"0")
        self.assertEquals(self._lyst._tail.data,"3")

    def testMiddleRemove(self):
        out = self._lyst.remove(2)
        self.assertEquals(out,"2")
        self.assertEquals(len(self._lyst),4)
        self.assertEquals(self._lyst._head.data,"0")
        self.assertEquals(self._lyst._tail.data,"4")
        self.assertEquals(self._lyst.__str__(),"0 1 3 4 ")

    def testRemoveAddMiddle(self):
        out = self._lyst.remove(2)
        self._lyst.insert(2,"two")
        self.assertEquals(len(self._lyst),5)
        self.assertEquals(self._lyst._head.data,"0")
        self.assertEquals(self._lyst._tail.data,"4")
        self.assertEquals(self._lyst.__str__(),"0 1 two 3 4 ")

    def testRemoveAll(self):
        self._lyst = LinkedIndexedList()
        self._lyst.append("0")
        self._lyst.append("0")
        out = self._lyst.remove(0)
        out = self._lyst.remove(0)
        self.assertEquals(out,"0")
        self.assertEquals(len(self._lyst),0)
        self.assertEquals(self._lyst._head,None)
        self.assertEquals(self._lyst._tail,None)
        
suite = unittest.makeSuite(TestLinkedIndexedList)
unittest.TextTestRunner().run(suite)
  

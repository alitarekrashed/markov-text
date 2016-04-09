import unittest
from markov import MarkovState

class TestStateConstruction(unittest.TestCase):
  def test_construct(self):
    x = MarkovState(("hello"))
    self.assertEqual(x.state, ("hello"))
    self.assertEqual(x.total, 0)

  def test_tuple_member(self):
    x = MarkovState(("hello", "world"))
    self.assertEqual(x.state[0], "hello")
    self.assertEqual(x.state[1], "world")

class TestStateComparison(unittest.TestCase):
  def test_matching_true(self):
    x = MarkovState(("hello"))
    self.assertTrue(x.is_matching("hello"))

  def test_matching_false(self):
    x = MarkovState(("hello"))
    self.assertFalse(x.is_matching("world"))

class TestStateAppend(unittest.TestCase):
  def test_append_1(self):
    x = MarkovState(("hello"))
    x.append("foo")
    self.assertEqual(x.total, 1)

  def test_append_2(self):
    x = MarkovState(("hello"))
    self.assertEqual(x.total, 0)
    x.append("foo")
    x.append("foo")
    self.assertEqual(x.total, 2)

  def test_append_3(self):
    x = MarkovState(("hello"))
    self.assertEqual(x.total, 0)
    x.append("foo")
    x.append("bar")
    self.assertEqual(x.follow["foo"], 1) 
    self.assertEqual(x.total, 2)

class TestStateGenerateNext(unittest.TestCase):
  def test_generate_next_1(self):
    x = MarkovState(("hello"))
    x.append("foo")
    self.assertEqual(x.generate_next(), "foo")

class TestStateHashAndEq(unittest.TestCase):
  def test_eq_true(self):
    x = MarkovState(("hello"))
    x.append("foo")
    y = MarkovState(("hello"))
    self.assertTrue(x == y)

  def test_eq_false(self):
    x = MarkovState(("hello"))
    x.append("foo")
    y = MarkovState("world")
    y.append("foo")
    self.assertFalse(x == y)

  def test_hash_true(self):
    x = MarkovState(("hello"))
    x.append("foo")
    y = MarkovState(("hello"))
    d = {}
    d[x] = 5
    self.assertTrue(y in d)

  def test_hash_false(self):
    x = MarkovState(("hello"))
    x.append("foo")
    y = MarkovState(("world"))
    d = {}
    d[x] = 5
    self.assertFalse(y in d)

if __name__ == '__main__':
    unittest.main()
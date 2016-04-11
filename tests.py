import unittest
from markov import *

class TestStateConstruction(unittest.TestCase):
  def test_construct(self):
    x = MarkovState(("hello",))
    self.assertEqual(x.state, ("hello",))
    self.assertEqual(x.total, 0)

  def test_tuple_member(self):
    x = MarkovState(("hello", "world"))
    self.assertEqual(x.state[0], "hello")
    self.assertEqual(x.state[1], "world")

class TestStateComparison(unittest.TestCase):
  def test_matching_true(self):
    x = MarkovState(("hello",))
    self.assertTrue(x.is_matching(("hello",)))

  def test_matching_false(self):
    x = MarkovState(("hello",))
    self.assertFalse(x.is_matching(("world",)))

class TestStateString(unittest.TestCase):
  def test_to_string_1(self):
    x = MarkovState(("hello", "world"))
    self.assertEqual(str(x), "hello world")

  def test_to_string_2(self):
    x = MarkovState(("hello",))
    self.assertEqual(str(x), "hello")

class TestStateAppend(unittest.TestCase):
  def test_append_1(self):
    x = MarkovState(("hello",))
    x.append("foo")
    self.assertEqual(x.total, 1)

  def test_append_2(self):
    x = MarkovState(("hello",))
    self.assertEqual(x.total, 0)
    x.append("foo")
    x.append("foo")
    self.assertEqual(x.total, 2)

  def test_append_3(self):
    x = MarkovState(("hello",))
    self.assertEqual(x.total, 0)
    x.append("foo")
    x.append("bar")
    self.assertEqual(x.follow["foo"], 1) 
    self.assertEqual(x.total, 2)

class TestStateGenerateNext(unittest.TestCase):
  def test_generate_next_1(self):
    x = MarkovState(("hello",))
    x.append("foo")
    self.assertEqual(x.generate_next(), "foo")

class TestStateHashAndEq(unittest.TestCase):
  def test_eq_true(self):
    x = MarkovState(("hello",))
    x.append("foo")
    y = MarkovState(("hello",))
    self.assertTrue(x == y)

  def test_eq_false(self):
    x = MarkovState(("hello",))
    x.append("foo")
    y = MarkovState("world",)
    y.append("foo")
    self.assertFalse(x == y)

  def test_hash_true(self):
    x = MarkovState(("hello",))
    x.append("foo")
    y = MarkovState(("hello",))
    d = {}
    d[x] = 5
    self.assertTrue(y in d)

  def test_hash_false(self):
    x = MarkovState(("hello",))
    x.append("foo")
    y = MarkovState(("world",))
    d = {}
    d[x] = 5
    self.assertFalse(y in d)

class TestStateAdjust(unittest.TestCase):
  def test_adjust_1(self):
    x = MarkovState(("hello",))
    y = x.adjust_state("foo")
    self.assertEqual(y, MarkovState(("foo",)))

  def test_adjust_2(self):
    x = MarkovState(("hello", "world"))
    y = x.adjust_state("foo")
    self.assertEqual(y, MarkovState(("world", "foo")))

  def test_adjust_3(self):
    x = MarkovState(("hello", "world", "lorem"))
    y = x.adjust_state("foo")
    self.assertEqual(y, MarkovState(("world", "lorem", "foo")))

class TestEngineAppend(unittest.TestCase):
  def test_append_1(self):
    m = MarkovEngine()
    m.append_instance(("hello",), "blah")
    self.assertEqual(len(m.states), 1)

  def test_append_2(self):
    m = MarkovEngine()
    self.assertEqual(len(m.states), 0)

  def test_append_3(self):
    m = MarkovEngine()
    m.append_instance(("hello",), "blah")
    m.append_instance(("hello",), "bleh")
    self.assertEqual(len(m.states), 1)

  def test_append_4(self):
    m = MarkovEngine()
    m.append_instance(("hello",), "blah")
    m.append_instance(("world",), "blah")
    self.assertEqual(len(m.states), 2)

class TestEngineExists(unittest.TestCase):
  def test_exist_empty(self):
    m = MarkovEngine()
    self.assertFalse(m.exists(("hello",)))

  def test_exist_true_1(self):
    m = MarkovEngine()
    m.append_instance(("hello",), "blah")
    self.assertTrue(m.exists(("hello",)))

class TestEngineGeneration(unittest.TestCase):
  def test_random_state_1(self):
    m = MarkovEngine()
    m.append_instance(("hello",), "blah")
    x = MarkovState(("hello",))
    self.assertEqual(x, m.get_random_state())

  def test_random_state_2(self):
    m = MarkovEngine()
    m.append_instance(("hello",), "foo")
    m.append_instance(("hello",), "bar")
    m.append_instance(("hello",), "foobar")
    x = MarkovState(("hello",))
    self.assertEqual(x, m.get_random_state())

  def test_random_state_3(self): #hacky test, maybe fix this?
    m = MarkovEngine()
    m.append_instance(("hello",), "foo")
    m.append_instance(("world",), "bar")
    x = MarkovState(("hello",))
    y = MarkovState(("world",))
    result = m.get_random_state()
    self.assertTrue(x == result or y == result)

  def test_generate_chain_1(self):
    m = MarkovEngine()
    m.append_instance(("hello", "world"), "foo")
    result = m.generate_chain(100)
    self.assertEqual(result, "hello world foo")

  def test_generate_chain_2(self):
    m = MarkovEngine()
    m.append_instance(("hello", "world"), "foo")
    m.append_instance(("world", "foo"), "bar")
    result = m.generate_chain(100)
    self.assertEqual(result, "hello world foo bar")

  def test_generate_chain_2(self): #hacky test, maybe fix this?
    m = MarkovEngine()
    m.append_instance(("hello", "world"), "foo")
    m.append_instance(("world", "foo"), "bar")
    result = m.generate_chain(100)
    self.assertTrue(result == "hello world foo bar" or result == "world foo bar")

if __name__ == '__main__':
    unittest.main()
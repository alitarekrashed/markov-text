import unittest
from markov import *

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
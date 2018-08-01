from python_purple_parrots.application import Test

def test_cookie():
   assert Test.cookie('Hi my name is Jeff') == 'Hi cookie my cookie name cookie is cookie Jeff cookie'
   assert Test.cookie('I like vegetables') == 'Me cookie like cookie vegetables'

def test_dog():
   assert Test.dog('I am a dog') == 'Woof woof woof woof'
   assert Test.dog('I like to chew toys') == 'Woof woof woof woof woof'

def test_kermit():
   assert Test.kermit('I will commit suicide') == 'I will kermit suicide'
   assert Test.kermit('He will commit arson') == 'He will kermit arson'



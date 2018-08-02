from application import MessageBoard, YodaMessage, DogMessage, CookieMessage, KermitMessage, BritishMessage, MessageId, get_app
from unittest import TestCase


class Rtest(TestCase):
    def setUp(self):
        self.application = get_app()
        self.client = self.application.test_client

YodaMessage.post('I am your father')


def test_message_board():
    assert mb.get() == 'your father I am'


def test_cookie():
    assert CookieMessage.get('Hi my name is Jeff') == 'Hi cookie my cookie name cookie is cookie Jeff cookie'
    assert CookieMessage.get('I like vegetables') == 'Me cookie like cookie vegetables'


def test_dog():
    assert DogMessage.get('I am a dog') == 'Woof woof woof woof'
    assert DogMessage.get('I like to chew toys') == 'Woof woof woof woof woof'


def test_kermit():
    assert KermitMessage.get('I will commit suicide') == 'I will kermit suicide'
    assert KermitMessage.get('He will commit arson') == 'He will kermit arson'


def test_british():
    assert BritishMessage.get('I like cookies') == 'I like cookies mate'
    assert BritishMessage.get('Mitochondria is the powerhouse of the cell') == 'Mitochondria is the ' \
                                                                          'powerhouse of the cell mate'
    assert BritishMessage.get('color line favorite labor tv') == 'colour queue favourite labour telly mate'


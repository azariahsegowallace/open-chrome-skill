from mycroft import MycroftSkill, intent_file_handler


class OpenChrome(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('chrome.open.intent')
    def handle_chrome_open(self, message):
        self.speak_dialog('chrome.open')


def create_skill():
    return OpenChrome()


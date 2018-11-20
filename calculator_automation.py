import random
import string
import time
import unittest
import lackey


def highlight_click(element, duration_time):
    element.highlight(duration_time)
    lackey.Screen().click(element)


def highlight_double_click(element, duration_time):
    element.highlight(duration_time)
    lackey.Screen().click(element)


def generate_random_filename(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class TestKeyboardMethods(unittest.TestCase):

    def test_open_notepad(self):
        search_field = lackey.Screen().find("images/search_tab.PNG")
        highlight_click(search_field, 2)
        search_field.type("notepad")
        search_field.type("{ENTER}")
        time.sleep(2)

    def test_write_text(self):
        notepad_window = lackey.Screen().find("images/notepad_window.PNG")
        highlight_click(notepad_window, 2)
        notepad_window.type("This is desktop automation via Lackey")
        notepad_window.type("{ENTER}")
        file_menu_option = lackey.Screen().find("images/File_menu_option.PNG")
        highlight_click(file_menu_option, 2)
        save_menu_option = lackey.Screen().find("images/SaveAs_Menu.png")
        highlight_click(save_menu_option, 2)
        save_as_window = lackey.Screen().find("images/SaveAs_window.PNG")
        save_as_window.highlight(2)
        save_as_window.type("{BACKSPACE}")
        file_name_field = lackey.Screen().find("images/File_name_field.PNG")
        highlight_click(file_name_field, 2)
        file_name_field.type(generate_random_filename())
        save_button = lackey.Screen().find("images/Save_button.PNG")
        highlight_click(save_button, 2)
        highlight_click(file_menu_option, 2)
        exit_menu_option = lackey.Screen().find("images/Exit_Menu_option.png")
        highlight_click(exit_menu_option, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)

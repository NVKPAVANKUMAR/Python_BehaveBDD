from pywinauto.application import Application
import unittest


class WindowsNotepadAutomation(unittest.TestCase):
    @staticmethod
    def test_notepad():
        app = Application().start("notepad.exe")
        app.UntitledNotepad.menu_select("Help->About Notepad")
        app.AboutNotepad.OK.click()
        app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)
        app.UntitledNotepad.Edit.select()
        app.UntitledNotepad.menu_select("File->Save As")
        app.SaveAs.ComboBox3.select("UTF-8")
        app.SaveAs.Edit1.set_text("Example-uft8.txt")
        app.SaveAs.Save.click()
        app.ConfirmSaveAs.Yes.click()
        app.UntitledNotepad.menu_select("File->Exit")
        app.ConfirmSaveAs.Yes.click()

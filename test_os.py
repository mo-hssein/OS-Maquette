import unittest
from OS import StackApp, NodeApp, App


class TestOS(unittest.TestCase):
    def test_App(self):
        google = App("Google Chrome")
        os = StackApp()
        os.open_app(google)
        result = os.get_num_of_apps()
        self.assertEqual(result, 1)

    def test_NodeApp(self):
        Photoshop = App("Adobe Photoshop")
        os = StackApp()
        os.open_app(Photoshop)
        result = os.get_num_of_apps()
        self.assertEqual(result, 2)

    def test_StackApp(self):
        VSCode = App("Visual Studio Code")
        os = StackApp()
        os.open_app(VSCode)
        result = os.get_num_of_apps()
        self.assertEqual(result, 3)

    def test_get_num_of_apps(self):
        Notion = App("Notion")
        os = StackApp()
        os.open_app(Notion)
        result = os.get_num_of_apps()
        self.assertEqual(result, 4)

    def test_close_app(self):
        os = StackApp()
        with self.assertRaises(IndexError) as context:
            os.close_app()
        self.assertEqual(
            str(context.exception), "There are no open applications at this time."
        )
        result = os.get_num_of_apps()
        self.assertEqual(result, 3)

    def test_stack_empty(self):
        os = StackApp()
        result = os.stack_empty()
        self.assertEqual(result, False)

    def test_open_app(self):
        os = StackApp()
        OVBox = App("Oracle VM VirtualBox")
        os.open_app(OVBox)
        result = os.get_num_of_apps()
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()

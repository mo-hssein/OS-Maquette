class App:
    def __init__(self, name) -> None:
        """
        This creates the App object.

        Parameters:
        - name (str) : name of Application

        Returns:
        - None
        """
        self.name = name


class NodeApp:
    # the size of stack apps
    size = 0

    def __init__(self, data) -> None:
        """
        This creates the Application object.

        Parameters:
        - data (object): The data to be stored in the node.

        Returns:
        - None
        """
        self.__data = data
        self.__next = None  # This indicates the following application is running in the background

        # Adds a new item to the stack size whenever a new application is opened
        NodeApp.size += 1


class StackApp(NodeApp):
    def __init__(self) -> None:
        """
        This creates the StackApp object.

        Parameters:
        - None

        Returns:
        - None
        """
        self.__top = None  # It refers to the first application we stand on

    def get_num_of_apps(self) -> int:
        """
        This feature displays the number of applications that are currently open.

        Parameters:
        - None

        Returns:
        - Number of open applications.
        """
        return NodeApp.size

    def stack_empty(self) -> bool:
        """
        This feature detects whether there are applications currently open or not.

        Parameters:
        - None

        Returns:
        - True if there is no application open and false if there is one or more applications open.
        """
        if NodeApp.size == 0:
            return True
        else:
            return False

    def open_app(self, app) -> None:
        """
        This feature opens a new application.

        Parameters:
        - app (str) : Application name.

        Returns:
        - None.
        """
        new_app_node = NodeApp(app)
        new_app_node.__next = self.__top
        self.__top = new_app_node


    def close_app(self) -> None:
        """
        This feature closes the last opened application.

        Parameters:
        - None

        Returns:
        - None.
        """
        if self.stack_empty():
            raise IndexError("There are no open applications at this time.")
        elif self.__top is not None:
            app = self.__top
            self.__top = self.__top.__next
            NodeApp.size -= 1
            return f"{app} is locked"
        else:
            raise IndexError("There are no open applications at this time.")


# Applications on our desktop
Google = App("Google Chrome")
VSCode = App("Visual Studio Code")
Photoshop = App("Adobe Photoshop")

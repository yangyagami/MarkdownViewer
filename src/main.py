"""MarkdownViewer entry point.

"""

import sys

from PySide6 import QtWidgets

from ui import main_window

def main():
    """The main function, Program's entry point.

    Create Qt Application and run.
    """

    app = QtWidgets.QApplication(sys.argv)
    window = main_window.MainWindow(sys.argv)
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()

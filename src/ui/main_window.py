"""Application main window.
"""

from PySide6 import QtWidgets
from PySide6 import QtWebEngineCore, QtWebEngineWidgets
from PySide6 import QtCore

import resources
from controller import markdown_document

class MainWindow(QtWidgets.QWidget):
    """MainWindow class.
    """

    def __init__(self, argv):
        super().__init__()

        self.setMinimumSize(800, 600)

        self._web_engine_page = QtWebEngineCore.QWebEnginePage()
        self._web_engine_page.setUrl(QtCore.QUrl('qrc:/index.html'))

        self._web_engine_view = QtWebEngineWidgets.QWebEngineView(self)
        self._web_engine_view.setPage(self._web_engine_page)

        self._layout = QtWidgets.QHBoxLayout()
        self.setLayout(self._layout)
        self._layout.addWidget(self._web_engine_view)

        self._document_controller = markdown_document.MarkdownDocumentController(self._web_engine_page, argv)

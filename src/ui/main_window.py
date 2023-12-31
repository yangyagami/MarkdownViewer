"""Application main window.
"""

import os

from PySide6 import QtWidgets
from PySide6 import QtWebEngineCore, QtWebEngineWidgets
from PySide6 import QtCore

import resources
from controller import markdown_document

class MainWindow(QtWidgets.QWidget):
    """MainWindow class.
    """

    def _set_web_engine_attribute(self, attribute, value):
        """Set attribute for webengine view and webengine page.
        """
        self._web_engine_page.settings().setAttribute(
            attribute,
            value
        )
        self._web_engine_view.settings().setAttribute(
            attribute,
            value
        )

    def _set_web_engine(self):
        """Set common attribute for webengine.
        """
        self._set_web_engine_attribute(
            QtWebEngineCore.QWebEngineSettings.LocalContentCanAccessFileUrls,
            True
        )
        self._set_web_engine_attribute(
            QtWebEngineCore.QWebEngineSettings.LocalContentCanAccessRemoteUrls,
            True
        )

    def __init__(self, argv):
        super().__init__()

        self.setMinimumSize(800, 600)

        file_handler = QtCore.QFile(':/index.html')
        html_text = ''
        if (file_handler.open(QtCore.QIODevice.ReadOnly) == True):
            stream = QtCore.QTextStream(file_handler)
            html_text = stream.readAll()

        self._web_engine_view = QtWebEngineWidgets.QWebEngineView(self)
        self._web_engine_page = QtWebEngineCore.QWebEnginePage()

        self._set_web_engine()
        self._web_engine_page.setHtml(
            html_text,
            QtCore.QUrl.fromLocalFile(os.getcwd()+os.path.sep)
        )

        self._web_engine_view.setPage(self._web_engine_page)

        self._layout = QtWidgets.QHBoxLayout()
        self.setLayout(self._layout)
        self._layout.addWidget(self._web_engine_view)

        self._document_controller = (markdown_document.
                                     MarkdownDocumentController(
                                         self._web_engine_page,
                                         argv
                                     ))

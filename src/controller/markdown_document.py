"""Markdown document controller.
"""

import os

from PySide6 import QtWebChannel
from PySide6 import QtCore

class _MarkdownDocument(QtCore.QObject):
    """MarkdownDocument class.

    Property:
             text_changed_signal: 
                The signal of _MarkdownDocument. If text changed, it will be emited.
             text:
                The property of Qt's program. It used to communicate with webchannel.
    """

    text_changed_signal = QtCore.Signal(str)

    def __init__(self):
        super().__init__()

        self._text = ''

        self.channel = QtWebChannel.QWebChannel(self)
        self.channel.registerObject('content', self)

    def set_text(self, text):
        """Set text to document.
        """
        if self._text == text:
            return
        self._text = text

        self.text_changed_signal.emit(self._text)

    def get_text(self):
        """Get text from document.
        """
        return self._text

    text = QtCore.Property(
        str,
        final = True,
        fget = get_text,
        notify = text_changed_signal,
    )

class MarkdownDocumentController(QtCore.QObject):
    """MarkdownDocumentController parse argv and set document.
    """

    def _read_file_content(self, file_path) -> str:
        """Read file's text content.
        """
        file_content = ''
        with open(file_path, 'r') as file_handler:
            file_content = file_handler.read()

        return file_content

    @QtCore.Slot(str)
    def _on_file_changed(self, file_path):
        """File changed slot
        """
        file_content = self._read_file_content(file_path)
        self._document.set_text(file_content)

    def _set_file_watcher(self, file_path):
        """Set file watcher.

        If file changed. The document will be updated.
        """
        self._file_watcher = QtCore.QFileSystemWatcher(self)
        self._file_watcher.addPath(file_path)
        self._file_watcher.fileChanged.connect(self._on_file_changed)

    def _parse_argv(self, argv) -> str:
        """Parse argv.

        Parse argv from command line. If argv's size <= 1 then program exit. 

        Arguments:
                  argv: The arguments from command line.
        Returns:
               return a file's content.
        """
        if len(argv) <= 1:
            return ''
        file_path = argv[1]

        return file_path

    def _set_web_channel(self, web_page):
        """Set channel for web page.
        """
        web_page.setWebChannel(self._document.channel)

    def __init__(self, web_page, argv):
        super().__init__()

        self._document = _MarkdownDocument()
        self._set_web_channel(web_page)

        file_path = self._parse_argv(argv)
        content = self._read_file_content(file_path)
        self._set_file_watcher(file_path)
        self._document.set_text(content)


"""Markdown document controller.
"""

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
        file_handler = open(file_path, 'r')
        file_content = file_handler.read()
        file_handler.close()

        return file_content

    def _set_web_channel(self, web_page):
        """Set channel for web page.
        """
        web_page.setWebChannel(self._document.channel)

    def __init__(self, web_page, argv):
        super().__init__()

        self._document = _MarkdownDocument()
        self._set_web_channel(web_page)

        content = self._parse_argv(argv)
        self._document.set_text(content)


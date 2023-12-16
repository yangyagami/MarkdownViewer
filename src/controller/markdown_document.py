"""Markdown document controller.
"""

from PySide6 import QtWebChannel
from PySide6 import QtCore

class MarkdownDocument(QtCore.QObject):
    """MarkdownDocument class.
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

# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.4.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x02\xe1\
<\
!doctype html>\x0a<\
html lang=\x22en\x22>\x0a\
<meta charset=\x22u\
tf-8\x22>\x0a<head>\x0a  \
<!--link rel=\x22st\
ylesheet\x22 type=\x22\
text/css\x22 href=\x22\
3rdparty/markdow\
n.css\x22-->\x0a  <scr\
ipt src=\x22https:/\
/cdn.jsdelivr.ne\
t/npm/marked/mar\
ked.min.js\x22></sc\
ript>\x0a  <script \
src=\x22qrc:/qtwebc\
hannel/qwebchann\
el.js\x22></script>\
\x0a</head>\x0a<body>\x0a\
  <div id=\x22place\
holder\x22></div>\x0a \
 <script>\x0a  'use\
 strict';\x0a\x0a  var\
 placeholder = d\
ocument.getEleme\
ntById('placehol\
der');\x0a\x0a  var up\
dateText = funct\
ion(text) {\x0a    \
  placeholder.in\
nerHTML = marked\
.parse(text);\x0a  \
}\x0a\x0a  new QWebCha\
nnel(qt.webChann\
elTransport,\x0a   \
 function(channe\
l) {\x0a      var c\
ontent = channel\
.objects.content\
;\x0a      updateTe\
xt(content.text)\
;\x0a      content.\
text_changed_sig\
nal.connect(upda\
teText);\x0a    }\x0a \
 );\x0a  </script>\x0a\
</body>\x0a</html>\x0a\
\
"

qt_resource_name = b"\
\x00\x0a\
\x0c\xba\xf2|\
\x00i\
\x00n\x00d\x00e\x00x\x00.\x00h\x00t\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8cq\xcc\xa9\xc5\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

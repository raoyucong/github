import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from lxml import etree


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载外部网页的例子')
        self.resize(800,700)
        self.lay = QVBoxLayout()
        self.lay_btn = QHBoxLayout()
        self.browser=QWebEngineView()
        self.btn = QPushButton('刷新')
        #加载外部的web界面
        self.browser.load(QUrl('file:///D:/code/github/htmltest/quickquery.html'))
        self.lay_btn.addStretch(1)
        self.lay_btn.addWidget(self.btn)
        self.lay_btn.addStretch(1)
        self.lay.setContentsMargins(0, 10, 0, 0)
        self.lay.addLayout(self.lay_btn)
        self.btn.clicked.connect(self.fresh)
        self.lay.addWidget(self.browser)
        self.setLayout(self.lay)
        with open('D:/code/github/htmltest/quickquery.html', 'r+', encoding='utf-8') as f:
            sourcecode = f.read()
            html = etree.HTML(sourcecode)

        headtitle = html.xpath('//head/title/text()')
        print(headtitle)

    def fresh(self):
        self.browser.setHtml('''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body>
                <h1>Hello PyQt5</h1>
                <h1>Hello PyQt5</h1>
                <h1>hello PyQt5</h1>
                <h1>hello PyQt5</h1>
                <h1>hello PyQt5</h1>
                <h1>Hello PyQt5</h1>

            </body>
        </html>

        ''')
    
    def contextMenuEvent(self, event):

           cmenu = QMenu(self)

           newAct = cmenu.addAction("New")
           opnAct = cmenu.addAction("Open")
           quitAct = cmenu.addAction("Quit")
           action = cmenu.exec_(self.mapToGlobal(event.pos()))

           if action == quitAct:
               pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())

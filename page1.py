# 第1页，心灵之旅，开始测试


from PyQt5.QtWidgets import QPushButton, QFrame, QLabel
from PyQt5.QtGui import QPixmap, QFont

def next_page(self):
    # 先关闭本页，再打开下一页
    self.frame_page1.deleteLater()
    self.show_frame_page2()

def show_frame_page1_d(self):
    print('开始第1页')
    self.frame_page1 = QFrame(self)
    self.frame_page1.setProperty("old_geometry", (0, 0, 1920, 991))

    self.frame_page1_label1 = QLabel(self.frame_page1)
    self.frame_page1_label1.setProperty("old_geometry", (0, 0, 1920, 991))
    frame_pixmap1 = QPixmap('resource\\page1\\主界面.png')
    self.frame_page1_label1.setPixmap(frame_pixmap1)
    # 设置图片填充效果
    self.frame_page1_label1.setScaledContents(True)

    self.frame_page1_button1 = QPushButton('开 始 测 试', self.frame_page1)
    self.frame_page1_button1.raise_()  # 将按钮移动到堆栈顶部，确保显示在图片之上
    self.frame_page1_button1.setProperty("old_geometry", (800, 800, 400, 110))
    self.frame_page1_button1.setStyleSheet('''
                           QPushButton {
                                border-radius: 15px;
                                border-image: url(resource/page1/开始测试按钮.png);
                                color:#264649;
                                        }
                           QPushButton:hover {
                                border-radius: 15px;
                                border-image: url(resource/page1/开始测试按钮_高亮.png);
                                color:#264649;
                                     }  
                                        ''')

    # self.frame_page1_button1.setFont(QFont("Microsoft YaHei", 25, QFont.Bold))
    self.frame_page1_button1.setFont(QFont(self.font_heavy, 29))
    self.frame_page1_button1.setProperty('origin_font_size', 29)
    self.frame_page1_button1.clicked.connect(lambda: next_page(self))
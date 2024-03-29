#########################################
#Author:Fle
#date:2021.12.22
#######################################33
import sys
import cv2
import threading
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QGroupBox
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PIL import Image
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtSql import *
import time
# from double_led import Double_LED_Class
import os

from MainWindow import Ui_Dialog as Ui_Dialog_MainWindow
from Admin_enter import Ui_Dialog as Ui_Dialog_Admin_enter
from Face_rec import Ui_Dialog as Ui_Dialog_Face_rec
from SQliteWindow import Ui_Dialog as Ui_Dialog_SQliteWindow

# 导入OpenCV自带的数据集，定义多个是因为在后面有多次调用，用一个的话会报错
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade1 = cv2.CascadeClassifier(cascadePath)
faceCascade2= cv2.CascadeClassifier(cascadePath)
faceCascade3 = cv2.CascadeClassifier(cascadePath)
faceCascade4=cv2.CascadeClassifier(cascadePath)

# Hardware_double_led=Double_LED_Class()
class Fle_MainWindow(QDialog,Ui_Dialog_MainWindow):
    def __init__(self):
        super(Fle_MainWindow,self).__init__()
        self.setupUi(self)
        # 创建定时器,定时器用来定时拍照
        self.timer_camera = QtCore.QTimer()
        self.user = []
        self.recognizer = cv2.face.LBPHFaceRecognizer_create() #创建LBPH人脸识别器
        faces, ids = self.getImagesAndLabels("./Face_data") #录入人脸的路径
        self.recognizer.train(faces, np.array(ids)) #训练人脸数据，区别是不同的人脸

        self.font = cv2.FONT_HERSHEY_SIMPLEX #指定字体
        self.camera_init()

        self.timer_camera.timeout.connect(self.show_camera)#将定时器的超时信号与self.show_camera函数进行连接。这意味着每当定时器超时时，就会自动调用 self.show_camera 函数
        self.timer_camera.start(30) #启动定时器，设置超时时间为30ms

        # 点击管理员按钮事件
        self.pushButton_administrators.clicked.connect(self.slot_btn_admin)


    # 函数获取图像和标签数据
    def getImagesAndLabels(self,path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)] #拼接路径
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            # 转换为灰度
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            print(imagePath)
            # id = int(imagePath.split("/")[2].split(".")[1]) #分隔符的问题
            id=1
            faces = faceCascade3.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
        print(ids)
        return faceSamples, ids

    def camera_init(self):
        # 打开设置摄像头对象
        self.cap = cv2.VideoCapture(0)
        self.__flag_work = 0
        self.x = 0
        self.count = 0
        self.minW = 0.2 * self.cap.get(3)#视频流的帧宽度
        self.minH = 0.2 * self.cap.get(4)#视频流的帧高度

    def show_camera(self):
        flag, self.image = self.cap.read()#这个对象用于从摄像头或其他视频源获取实时视频流，从视频流中读取一帧图像。这个方法返回两个值
        self.image=cv2.flip(self.image, 1)#用于对图像进行翻转操作
        # 将图片变化成灰度图
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # 探测图片中的人脸
        faces = faceCascade1.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(self.minW), int(self.minH)),
        )
        # 判断是否检测到人脸，没检测到设置为低电平
        if len(faces)!=0:
            WxH_max=0 #人脸矩形的面积
            WxH_max_face=faces[0] #存储人脸最大矩形面积
            for i in faces:
                if(i[2]*i[3]>WxH_max):
                    WxH_max=i[2]*i[3]
                    WxH_max_face=i
            # 围绕脸的框
            x=WxH_max_face[0]
            y = WxH_max_face[1]
            w = WxH_max_face[2]
            h = WxH_max_face[3]
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255, 0), 2) #在图像上绘制一个矩形框
            # 把要分析的面部的捕获部分作为参数，并将返回其可能的所有者，指示其ID以及识别器与该匹配相关的置信度
            id, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])
            # 对置信度进行判断，高于预定值显示出提示信息，并控制GPIO输出高低电平来控制门的开关
            if (confidence < 70):
                confidence = "  {0}%".format(round(100 - confidence)) #得到一百补数的百分数
                for i in range(0,mysqlite.get_rows()):
                    if mysqlite.find_data(i,0)==id:
                        self.label_ID.setText(str(mysqlite.find_data(i,1)))
                        self.label_name.setText(str(mysqlite.find_data(i,2)))
                    # Hardware_double_led.makerobo_set_red_Color(0)
                    # Hardware_double_led.makerobo_set_green_Color(100)
            else:
                confidence = "  {0}%".format(round(100 - confidence))
                self.label_ID.setText("不认识")
                self.label_name.setText("不认识")
                # Hardware_double_led.makerobo_set_red_Color(100)
                # Hardware_double_led.makerobo_set_green_Color(0)
            # 给图片添加文本 图片矩阵, 添加文本名称, 设置文本显示位置,
            # 字体样式, 字体大小, 字体颜色, 字体粗细
            cv2.putText(self.image, str(id), (x + 5, y - 5), self.font, 1, (255, 255, 255), 2)
            cv2.putText(self.image, str(confidence), (x + 5, y + h - 5), self.font, 1, (255, 255, 0), 1)
        else:
            # Hardware_double_led.makerobo_set_red_Color(0)
            # Hardware_double_led.makerobo_set_green_Color(0)
            print("无对象")
        # 将视频显示在了label上
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB) #得到一个大小为640x480像素且颜色空间为RGB的图像
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.lab_face.setPixmap(QtGui.QPixmap.fromImage(showImage))  #在pyqt上显示图像


    # 点点击管理员按钮事件
    def slot_btn_admin(self):
        self.timer_camera.stop()
        self.cap.release()
        self.logon = Fle_Admin_enter()
        self.logon.show()
        self.hide()
        # Hardware_double_led.makerobo_set_red_Color(0)
        # Hardware_double_led.makerobo_set_green_Color(0)


# 创建登录界面类
class Fle_Admin_enter(QDialog,Ui_Dialog_Admin_enter):
    def __init__(self):
        super(Fle_Admin_enter, self).__init__()
        self.setupUi(self)

        #将输入信息初始化为空
        self.lineEdit_admin_ID.setText("")
        self.lineEdit_admin_key.setText("")
        #设置密码为隐藏方式显示
        self.lineEdit_admin_key.setEchoMode(QLineEdit.Password)

        # 点击mylineedit事件
        self.lineEdit_admin_ID.textEdited[str].connect(self.changeEdit_ID)
        self.lineEdit_admin_key.textEdited[str].connect(self.changeEdit_key)

        # 点击返回按钮事件
        self.pushButton_admin_back.clicked.connect(self.slot_btn_back)
        # 点击登录按钮事件
        self.pushButton_admin_enter.clicked.connect(self.slot_btn_logon)


    # 点击Edit_ID事件
    def changeEdit_ID(self):
        Edit_ID = self.lineEdit_admin_ID.text()
        print("Edit_ID=",Edit_ID)

    # 点击Edit_key事件
    def changeEdit_key(self):
        Edit_key = self.lineEdit_admin_key.text()
        print("Edit_ID=",Edit_key)

    # 点击返回按钮事件
    def slot_btn_back(self):
        self.menu = Fle_MainWindow()
        self.menu.show()
        self.hide()

    # 点击登录按钮事件
    def slot_btn_logon(self):
        # 判断账号和密码是否输入正确
        print(self.lineEdit_admin_ID.text)
        print(self.lineEdit_admin_key.text)
        if self.lineEdit_admin_ID.text() == "1" and self.lineEdit_admin_key.text() == "1":
            self.manager_face = Fle_Face_rec()
            self.manager_face.show()
            self.hide()
            #print("enter Ui_manager_face")
        else:
            QMessageBox.warning(self, "提示", "账号或密码错误！", QMessageBox.Close)


class Fle_Face_rec(QDialog,Ui_Dialog_Face_rec): #录入人脸界面
    def __init__(self):
        super(Fle_Face_rec, self).__init__()
        self.setupUi(self)
        # 初始化 ID
        self.lineEdit_ID.setText("")
        self.lineEdit_name.setText("")

        # 初始化进度条定时器
        self.timer = QBasicTimer()
        self.step = 0
        # 创建定时器
        self.timer_camera = QtCore.QTimer()
        # 初始化摄像头数据
        self.camera_init()
        # 定时器函数，用来显示人脸检测结果，并不录入数据
        self.timer_camera.timeout.connect(self.show_camera)
        self.timer_camera.start(30)
        # 点击按钮开启线程
        self.pushButton_begin_rec.clicked.connect(self.slot_btn_enter)
        self.pushButton_back.clicked.connect(self.slot_btn_back)
        self.pushButton_show_sqlite.clicked.connect(self.show_sqlitedata)
    # 初始化摄像头数据
    def camera_init(self):
        # 打开设置摄像头对象
        self.cap = cv2.VideoCapture(0)
        # self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            print("无法打开摄像头")
        self.__flag_work = 0
        self.x =0
        self.count = 0
        self.cap.set(4,640) # set Width
        self.cap.set(3,480) # set Height

    # 点击返回按键返回上一界面
    def slot_btn_back(self):
        self.timer_camera.stop()
        self.cap.release()
        self.logon = Fle_MainWindow() #创建Fle_MainWindow()的对象
        self.logon.show()
        self.hide()

    def show_camera(self): #检测人脸
        flag, self.image = self.cap.read()
        self.image = cv2.flip(self.image, 1)
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faceCascade2 = cv2.CascadeClassifier(cascadePath)
        faces = faceCascade2.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(200, 200)
        )
        if len(faces)!=0:
            WxH_max = 0  # 人脸矩形的面积
            WxH_max_face = faces[0]
            for i in faces:
                if (i[2] * i[3] > WxH_max):
                    WxH_max = i[2] * i[3]
                    WxH_max_face = i
            # 围绕脸的框
            x = WxH_max_face[0]
            y = WxH_max_face[1]
            w = WxH_max_face[2]
            h = WxH_max_face[3]

            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = self.image[y:y + h, x:x + w]

        # 将视频显示在了label上
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_face.setPixmap(QtGui.QPixmap.fromImage(showImage))

    # 点击按钮开启线程
    def slot_btn_enter(self):
        self.count = 0
        # 创建线程并开启
        self.thread = threading.Thread(target=self.thread_pic)
        self.thread.start()
        # 开启进度条定时器
        self.timer.start(100, self)

    # 加载进度条
    def timerEvent(self, e):
        self.progressBar.setValue(self.count)


    # 录入人脸线程
    def thread_pic(self):
        tip="正在录入"+str(self.lineEdit_ID.text())+str(self.lineEdit_name.text())+"的人脸！！"
        print(tip)
        # 创建目录，将获取的人脸照片放入指定的文件夹
        self.file = "./Face_data"
        if not os.path.exists(self.file):
            os.makedirs(self.file)
        file_ID=str(self.lineEdit_ID.text())
        while (True):
            # 灰度化处理
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade4.detectMultiScale(gray, 1.3, 5)
            if len(faces)!=0:
                WxH_max = 0  # 人脸矩形的面积
                WxH_max_face = faces[0]
                for i in faces:
                    if (i[2] * i[3] > WxH_max):
                        WxH_max = i[2] * i[3]
                        WxH_max_face = i
                # 围绕脸的框
                x = WxH_max_face[0]
                y = WxH_max_face[1]
                w = WxH_max_face[2]
                h = WxH_max_face[3]

                self.count += 1
                # 将捕获的图像保存到指定的文件夹中
                print(self.file + "/User." + file_ID + '.' + str(self.count) + ".png")
                bool = cv2.imwrite(self.file + "/User." + file_ID + '.' + str(self.count) + ".png",
                                   gray[y:y + h, x:x + w])

                # 取60张人脸样本，停止录像
                if self.count >= 100:
                    print("人脸数据采集已完成!")
                    break

        #将数据存入数据库
        mysqlite.add_row(self.lineEdit_ID.text(),self.lineEdit_xuehao.text(),str(self.lineEdit_name.text()))


    def show_sqlitedata(self):
        self.logon = Fle_SQliteWindow()
        self.logon.show()
        #self.hide()


class Fle_SQliteWindow(QDialog,Ui_Dialog_SQliteWindow):#数据库查看窗口
    def __init__(self):
        super(Fle_SQliteWindow,self).__init__()
        self.setupUi(self)
        self.tableView.setModel(mysqlite.model)
        self.pushButton_add.clicked.connect(self.addrow)
        self.pushButton_delete.clicked.connect(lambda: mysqlite.model.removeRow(self.tableView.currentIndex().row()))
    def addrow(self):
        # 不是在QTableView上添加，而是在模型上添加,会自动将数据保存到数据库中！
        # 参数一：数据库共有几行数据  参数二：添加几行
        ret = mysqlite.model.insertRows(mysqlite.model.rowCount(), 1)  # 返回是否插入
        print('数据库共有%d行数据' % mysqlite.model.rowCount())
        print('insertRow=%s' % str(ret))



class Fle_Sqlite(): #与数据库交互操作
    def __init__(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./muttonDB.db')  
        if not self.db.open():
            print('无法建立与数据库的连接')
        query = QSqlQuery()
        query.exec('create table people(id varcahr(10),xuehao varcahr(15),name varcahr(50))')
        self.model = QSqlTableModel()  # MVC模式中的模型
        # 初始化将数据装载到模型当中
        self.initializeModel()

    # 初始化
    def initializeModel(self): 
        self.model.setTable('people')
        # 当字段变化时会触发一些事件
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        # 将整个数据装载到model中
        self.model.select()
        # 设置字段头
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'xuehao')
        self.model.setHeaderData(2, Qt.Horizontal, 'name')

    #找指定位置的数据
    def find_data(self, row, col):
        # 序号从0开始
        index = self.model.index(row, col)
        return self.model.data(index)

    #新加一行
    def add_row(self,ID,xuehao,name):
        row = self.model.rowCount()
        self.model.insertRow(row)  # 在第一行新增，避免翻页
        self.model.setData(self.model.index(row, 0), ID)  # 默认初始分类为重要紧急
        self.model.setData(self.model.index(row, 1), xuehao)  # 默认初始状态未完成
        self.model.setData(self.model.index(row, 2), name)  # 默认建立日期为当天
        self.model.submitAll()
        print(ID)
        print(xuehao)
        print(name)

    #删除最后一行
    def del_row(self):
        row = self.model.rowCount()-1
        self.model.removeRow(row)
        self.model.submitAll()

    def get_rows(self):
        #print(self.model.rowCount())
        return self.model.rowCount()


if __name__ == "__main__":
    mysqlite=Fle_Sqlite()
    app = QApplication(sys.argv)
    # s = Fle_Admin_enter()
    # s.show()
    # sys.exit(app.exec_())
    w = Fle_MainWindow()
    w.show()
    sys.exit(app.exec_())
    print("finish")
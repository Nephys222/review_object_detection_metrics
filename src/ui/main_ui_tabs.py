# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui_tabs.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1237, 635)
        Dialog.setMinimumSize(QtCore.QSize(1237, 635))
        Dialog.setMaximumSize(QtCore.QSize(1237, 635))
        self.frame_12 = QtWidgets.QFrame(Dialog)
        self.frame_12.setGeometry(QtCore.QRect(20, 430, 1191, 136))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.lbl_groundtruth_dir_26 = QtWidgets.QLabel(self.frame_12)
        self.lbl_groundtruth_dir_26.setGeometry(QtCore.QRect(10, 10, 281, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_groundtruth_dir_26.setFont(font)
        self.lbl_groundtruth_dir_26.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_groundtruth_dir_26.setObjectName("lbl_groundtruth_dir_26")
        self.chb_metric_AP75_coco = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AP75_coco.setGeometry(QtCore.QRect(10, 105, 191, 22))
        self.chb_metric_AP75_coco.setChecked(False)
        self.chb_metric_AP75_coco.setObjectName("chb_metric_AP75_coco")
        self.chb_metric_AP50_coco = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AP50_coco.setGeometry(QtCore.QRect(10, 75, 191, 22))
        self.chb_metric_AP50_coco.setChecked(False)
        self.chb_metric_AP50_coco.setObjectName("chb_metric_AP50_coco")
        self.chb_metric_AP_coco = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AP_coco.setGeometry(QtCore.QRect(10, 45, 191, 22))
        self.chb_metric_AP_coco.setChecked(False)
        self.chb_metric_AP_coco.setObjectName("chb_metric_AP_coco")
        self.chb_metric_AR_max100 = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AR_max100.setGeometry(QtCore.QRect(500, 105, 111, 22))
        self.chb_metric_AR_max100.setChecked(False)
        self.chb_metric_AR_max100.setObjectName("chb_metric_AR_max100")
        self.chb_metric_AR_max10 = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AR_max10.setGeometry(QtCore.QRect(500, 75, 111, 22))
        self.chb_metric_AR_max10.setChecked(False)
        self.chb_metric_AR_max10.setObjectName("chb_metric_AR_max10")
        self.chb_metric_AR_max1 = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AR_max1.setGeometry(QtCore.QRect(500, 45, 111, 22))
        self.chb_metric_AR_max1.setChecked(False)
        self.chb_metric_AR_max1.setObjectName("chb_metric_AR_max1")
        self.chb_metric_APmedium_coco = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_APmedium_coco.setGeometry(QtCore.QRect(180, 75, 191, 22))
        self.chb_metric_APmedium_coco.setChecked(False)
        self.chb_metric_APmedium_coco.setObjectName("chb_metric_APmedium_coco")
        self.chb_metric_APlarge_coco = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_APlarge_coco.setGeometry(QtCore.QRect(180, 105, 191, 22))
        self.chb_metric_APlarge_coco.setChecked(False)
        self.chb_metric_APlarge_coco.setObjectName("chb_metric_APlarge_coco")
        self.chb_metric_APsmall_coco = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_APsmall_coco.setGeometry(QtCore.QRect(180, 45, 191, 22))
        self.chb_metric_APsmall_coco.setChecked(False)
        self.chb_metric_APsmall_coco.setObjectName("chb_metric_APsmall_coco")
        self.chb_metric_AR_medium = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AR_medium.setGeometry(QtCore.QRect(640, 75, 111, 22))
        self.chb_metric_AR_medium.setChecked(False)
        self.chb_metric_AR_medium.setObjectName("chb_metric_AR_medium")
        self.chb_metric_AR_large = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AR_large.setGeometry(QtCore.QRect(640, 105, 111, 22))
        self.chb_metric_AR_large.setChecked(False)
        self.chb_metric_AR_large.setObjectName("chb_metric_AR_large")
        self.chb_metric_AR_small = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AR_small.setGeometry(QtCore.QRect(640, 45, 111, 22))
        self.chb_metric_AR_small.setChecked(False)
        self.chb_metric_AR_small.setObjectName("chb_metric_AR_small")
        self.lbl_groundtruth_dir_31 = QtWidgets.QLabel(self.frame_12)
        self.lbl_groundtruth_dir_31.setGeometry(QtCore.QRect(500, 10, 251, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_groundtruth_dir_31.setFont(font)
        self.lbl_groundtruth_dir_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_groundtruth_dir_31.setObjectName("lbl_groundtruth_dir_31")
        self.lbl_detections_dir_6 = QtWidgets.QLabel(self.frame_12)
        self.lbl_detections_dir_6.setGeometry(QtCore.QRect(920, 10, 191, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_detections_dir_6.setFont(font)
        self.lbl_detections_dir_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_detections_dir_6.setObjectName("lbl_detections_dir_6")
        self.dsb_IOU_pascal = QtWidgets.QDoubleSpinBox(self.frame_12)
        self.dsb_IOU_pascal.setGeometry(QtCore.QRect(1030, 40, 81, 27))
        self.dsb_IOU_pascal.setMaximum(1.0)
        self.dsb_IOU_pascal.setSingleStep(0.01)
        self.dsb_IOU_pascal.setProperty("value", 0.5)
        self.dsb_IOU_pascal.setObjectName("dsb_IOU_pascal")
        self.chb_metric_AP_pascal = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_AP_pascal.setGeometry(QtCore.QRect(920, 75, 121, 22))
        self.chb_metric_AP_pascal.setChecked(True)
        self.chb_metric_AP_pascal.setObjectName("chb_metric_AP_pascal")
        self.chb_metric_mAP_pascal = QtWidgets.QCheckBox(self.frame_12)
        self.chb_metric_mAP_pascal.setGeometry(QtCore.QRect(1050, 75, 71, 22))
        self.chb_metric_mAP_pascal.setChecked(True)
        self.chb_metric_mAP_pascal.setObjectName("chb_metric_mAP_pascal")
        self.lbl_IOU_thresh = QtWidgets.QLabel(self.frame_12)
        self.lbl_IOU_thresh.setGeometry(QtCore.QRect(920, 45, 101, 17))
        self.lbl_IOU_thresh.setObjectName("lbl_IOU_thresh")
        self.lbl_groundtruth_dir_26.raise_()
        self.chb_metric_AP75_coco.raise_()
        self.chb_metric_AP50_coco.raise_()
        self.chb_metric_AP_coco.raise_()
        self.chb_metric_AR_max100.raise_()
        self.chb_metric_AR_max10.raise_()
        self.chb_metric_AR_max1.raise_()
        self.chb_metric_APmedium_coco.raise_()
        self.chb_metric_APlarge_coco.raise_()
        self.chb_metric_APsmall_coco.raise_()
        self.chb_metric_AR_medium.raise_()
        self.chb_metric_AR_small.raise_()
        self.lbl_groundtruth_dir_31.raise_()
        self.lbl_detections_dir_6.raise_()
        self.dsb_IOU_pascal.raise_()
        self.chb_metric_AP_pascal.raise_()
        self.chb_metric_mAP_pascal.raise_()
        self.lbl_IOU_thresh.raise_()
        self.chb_metric_AR_large.raise_()
        self.lbl_groundtruth_dir_23 = QtWidgets.QLabel(Dialog)
        self.lbl_groundtruth_dir_23.setGeometry(QtCore.QRect(20, 400, 1191, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_groundtruth_dir_23.setFont(font)
        self.lbl_groundtruth_dir_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_groundtruth_dir_23.setObjectName("lbl_groundtruth_dir_23")
        self.btn_run = QtWidgets.QPushButton(Dialog)
        self.btn_run.setGeometry(QtCore.QRect(20, 600, 1191, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 181, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 255, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 218, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 90, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 121, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 181, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 119, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 218, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 181, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 255, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 218, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 90, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 121, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 181, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 152, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 218, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 90, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 181, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 255, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 218, 72))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 90, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 121, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 90, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(2, 90, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 181, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 181, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(5, 181, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.btn_run.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_run.setFont(font)
        self.btn_run.setObjectName("btn_run")
        self.btn_output_dir = QtWidgets.QPushButton(Dialog)
        self.btn_output_dir.setGeometry(QtCore.QRect(1180, 570, 31, 27))
        self.btn_output_dir.setObjectName("btn_output_dir")
        self.txb_output_dir = QtWidgets.QLineEdit(Dialog)
        self.txb_output_dir.setGeometry(QtCore.QRect(90, 570, 1081, 27))
        self.txb_output_dir.setReadOnly(True)
        self.txb_output_dir.setObjectName("txb_output_dir")
        self.lbl_groundtruth_dir_28 = QtWidgets.QLabel(Dialog)
        self.lbl_groundtruth_dir_28.setGeometry(QtCore.QRect(20, 575, 101, 17))
        self.lbl_groundtruth_dir_28.setObjectName("lbl_groundtruth_dir_28")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1221, 375))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_stats_gt = QtWidgets.QPushButton(self.tab)
        self.btn_stats_gt.setGeometry(QtCore.QRect(10, 280, 221, 27))
        self.btn_stats_gt.setObjectName("btn_stats_gt")
        self.txb_gt_images_dir = QtWidgets.QLineEdit(self.tab)
        self.txb_gt_images_dir.setGeometry(QtCore.QRect(110, 80, 1051, 27))
        self.txb_gt_images_dir.setReadOnly(True)
        self.txb_gt_images_dir.setObjectName("txb_gt_images_dir")
        self.lbl_groundtruth_dir = QtWidgets.QLabel(self.tab)
        self.lbl_groundtruth_dir.setGeometry(QtCore.QRect(10, 55, 101, 17))
        self.lbl_groundtruth_dir.setObjectName("lbl_groundtruth_dir")
        self.btn_gt_dir = QtWidgets.QPushButton(self.tab)
        self.btn_gt_dir.setGeometry(QtCore.QRect(1170, 50, 31, 27))
        self.btn_gt_dir.setObjectName("btn_gt_dir")
        self.lbl_groundtruth_dir_27 = QtWidgets.QLabel(self.tab)
        self.lbl_groundtruth_dir_27.setGeometry(QtCore.QRect(110, 140, 531, 21))
        self.lbl_groundtruth_dir_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_groundtruth_dir_27.setObjectName("lbl_groundtruth_dir_27")
        self.lbl_groundtruth_dir_25 = QtWidgets.QLabel(self.tab)
        self.lbl_groundtruth_dir_25.setGeometry(QtCore.QRect(10, 115, 101, 17))
        self.lbl_groundtruth_dir_25.setObjectName("lbl_groundtruth_dir_25")
        self.lbl_groundtruth_dir_3 = QtWidgets.QLabel(self.tab)
        self.lbl_groundtruth_dir_3.setGeometry(QtCore.QRect(10, 15, 1191, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_groundtruth_dir_3.setFont(font)
        self.lbl_groundtruth_dir_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_groundtruth_dir_3.setObjectName("lbl_groundtruth_dir_3")
        self.lbl_groundtruth_dir_2 = QtWidgets.QLabel(self.tab)
        self.lbl_groundtruth_dir_2.setGeometry(QtCore.QRect(10, 85, 101, 17))
        self.lbl_groundtruth_dir_2.setObjectName("lbl_groundtruth_dir_2")
        self.txb_gt_dir = QtWidgets.QLineEdit(self.tab)
        self.txb_gt_dir.setGeometry(QtCore.QRect(110, 50, 1051, 27))
        self.txb_gt_dir.setReadOnly(True)
        self.txb_gt_dir.setObjectName("txb_gt_dir")
        self.txb_classes_gt = QtWidgets.QLineEdit(self.tab)
        self.txb_classes_gt.setGeometry(QtCore.QRect(110, 110, 1051, 27))
        self.txb_classes_gt.setReadOnly(True)
        self.txb_classes_gt.setObjectName("txb_classes_gt")
        self.btn_gt_images_dir = QtWidgets.QPushButton(self.tab)
        self.btn_gt_images_dir.setGeometry(QtCore.QRect(1170, 80, 31, 27))
        self.btn_gt_images_dir.setObjectName("btn_gt_images_dir")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(10, 175, 1191, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.rad_gt_format_coco_json = QtWidgets.QRadioButton(self.frame)
        self.rad_gt_format_coco_json.setGeometry(QtCore.QRect(10, 40, 161, 22))
        self.rad_gt_format_coco_json.setChecked(True)
        self.rad_gt_format_coco_json.setObjectName("rad_gt_format_coco_json")
        self.lbl_detections_dir_3 = QtWidgets.QLabel(self.frame)
        self.lbl_detections_dir_3.setGeometry(QtCore.QRect(10, 10, 151, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_detections_dir_3.setFont(font)
        self.lbl_detections_dir_3.setObjectName("lbl_detections_dir_3")
        self.rad_gt_format_imagenet_xml = QtWidgets.QRadioButton(self.frame)
        self.rad_gt_format_imagenet_xml.setGeometry(QtCore.QRect(520, 40, 151, 22))
        self.rad_gt_format_imagenet_xml.setObjectName("rad_gt_format_imagenet_xml")
        self.rad_gt_format_openimages_csv = QtWidgets.QRadioButton(self.frame)
        self.rad_gt_format_openimages_csv.setGeometry(QtCore.QRect(220, 40, 231, 22))
        self.rad_gt_format_openimages_csv.setObjectName("rad_gt_format_openimages_csv")
        self.rad_gt_format_labelme_xml = QtWidgets.QRadioButton(self.frame)
        self.rad_gt_format_labelme_xml.setGeometry(QtCore.QRect(220, 70, 151, 22))
        self.rad_gt_format_labelme_xml.setChecked(False)
        self.rad_gt_format_labelme_xml.setObjectName("rad_gt_format_labelme_xml")
        self.rad_gt_format_pascalvoc_xml = QtWidgets.QRadioButton(self.frame)
        self.rad_gt_format_pascalvoc_xml.setGeometry(QtCore.QRect(10, 70, 181, 22))
        self.rad_gt_format_pascalvoc_xml.setChecked(False)
        self.rad_gt_format_pascalvoc_xml.setObjectName("rad_gt_format_pascalvoc_xml")
        self.rad_gt_format_abs_values_text = QtWidgets.QRadioButton(self.frame)
        self.rad_gt_format_abs_values_text.setGeometry(QtCore.QRect(750, 40, 181, 22))
        self.rad_gt_format_abs_values_text.setChecked(False)
        self.rad_gt_format_abs_values_text.setObjectName("rad_gt_format_abs_values_text")
        self.rad_gt_format_yolo_text = QtWidgets.QRadioButton(self.frame)
        self.rad_gt_format_yolo_text.setGeometry(QtCore.QRect(520, 70, 181, 22))
        self.rad_gt_format_yolo_text.setChecked(False)
        self.rad_gt_format_yolo_text.setObjectName("rad_gt_format_yolo_text")
        self.rad_gt_format_cvat_xml = QtWidgets.QRadioButton(self.frame)
        self.rad_gt_format_cvat_xml.setGeometry(QtCore.QRect(1010, 40, 161, 22))
        self.rad_gt_format_cvat_xml.setObjectName("rad_gt_format_cvat_xml")
        self.btn_groundtruth_dir_5 = QtWidgets.QPushButton(self.tab)
        self.btn_groundtruth_dir_5.setGeometry(QtCore.QRect(1170, 110, 31, 27))
        self.btn_groundtruth_dir_5.setObjectName("btn_groundtruth_dir_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_stats_det = QtWidgets.QPushButton(self.tab_2)
        self.btn_stats_det.setGeometry(QtCore.QRect(10, 310, 221, 27))
        self.btn_stats_det.setObjectName("btn_stats_det")
        self.lbl_groundtruth_dir_24 = QtWidgets.QLabel(self.tab_2)
        self.lbl_groundtruth_dir_24.setGeometry(QtCore.QRect(10, 85, 101, 17))
        self.lbl_groundtruth_dir_24.setObjectName("lbl_groundtruth_dir_24")
        self.btn_groundtruth_dir_4 = QtWidgets.QPushButton(self.tab_2)
        self.btn_groundtruth_dir_4.setGeometry(QtCore.QRect(1170, 80, 31, 27))
        self.btn_groundtruth_dir_4.setObjectName("btn_groundtruth_dir_4")
        self.txb_classes_det = QtWidgets.QLineEdit(self.tab_2)
        self.txb_classes_det.setGeometry(QtCore.QRect(110, 80, 1051, 27))
        self.txb_classes_det.setReadOnly(True)
        self.txb_classes_det.setObjectName("txb_classes_det")
        self.txb_det_dir = QtWidgets.QLineEdit(self.tab_2)
        self.txb_det_dir.setGeometry(QtCore.QRect(110, 50, 1051, 27))
        self.txb_det_dir.setReadOnly(True)
        self.txb_det_dir.setObjectName("txb_det_dir")
        self.lbl_groundtruth_dir_29 = QtWidgets.QLabel(self.tab_2)
        self.lbl_groundtruth_dir_29.setGeometry(QtCore.QRect(110, 110, 531, 21))
        self.lbl_groundtruth_dir_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_groundtruth_dir_29.setObjectName("lbl_groundtruth_dir_29")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setGeometry(QtCore.QRect(10, 145, 1191, 161))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.rad_det_ci_format_text_yolo_rel = QtWidgets.QRadioButton(self.frame_4)
        self.rad_det_ci_format_text_yolo_rel.setGeometry(QtCore.QRect(10, 40, 581, 22))
        self.rad_det_ci_format_text_yolo_rel.setToolTip("")
        self.rad_det_ci_format_text_yolo_rel.setChecked(True)
        self.rad_det_ci_format_text_yolo_rel.setObjectName("rad_det_ci_format_text_yolo_rel")
        self.lbl_detections_dir_5 = QtWidgets.QLabel(self.frame_4)
        self.lbl_detections_dir_5.setGeometry(QtCore.QRect(10, 10, 151, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_detections_dir_5.setFont(font)
        self.lbl_detections_dir_5.setObjectName("lbl_detections_dir_5")
        self.rad_det_ci_format_text_xywh_abs = QtWidgets.QRadioButton(self.frame_4)
        self.rad_det_ci_format_text_xywh_abs.setGeometry(QtCore.QRect(10, 100, 531, 22))
        self.rad_det_ci_format_text_xywh_abs.setObjectName("rad_det_ci_format_text_xywh_abs")
        self.rad_det_ci_format_text_xyx2y2_abs = QtWidgets.QRadioButton(self.frame_4)
        self.rad_det_ci_format_text_xyx2y2_abs.setGeometry(QtCore.QRect(10, 70, 531, 22))
        self.rad_det_ci_format_text_xyx2y2_abs.setChecked(False)
        self.rad_det_ci_format_text_xyx2y2_abs.setObjectName("rad_det_ci_format_text_xyx2y2_abs")
        self.rad_det_format_coco_json = QtWidgets.QRadioButton(self.frame_4)
        self.rad_det_format_coco_json.setGeometry(QtCore.QRect(10, 130, 181, 22))
        self.rad_det_format_coco_json.setObjectName("rad_det_format_coco_json")
        self.rad_det_cn_format_text_xyx2y2_abs = QtWidgets.QRadioButton(self.frame_4)
        self.rad_det_cn_format_text_xyx2y2_abs.setGeometry(QtCore.QRect(600, 70, 531, 22))
        self.rad_det_cn_format_text_xyx2y2_abs.setChecked(False)
        self.rad_det_cn_format_text_xyx2y2_abs.setObjectName("rad_det_cn_format_text_xyx2y2_abs")
        self.rad_det_cn_format_text_yolo_rel = QtWidgets.QRadioButton(self.frame_4)
        self.rad_det_cn_format_text_yolo_rel.setGeometry(QtCore.QRect(600, 40, 591, 22))
        self.rad_det_cn_format_text_yolo_rel.setChecked(False)
        self.rad_det_cn_format_text_yolo_rel.setObjectName("rad_det_cn_format_text_yolo_rel")
        self.rad_det_cn_format_text_xywh_abs = QtWidgets.QRadioButton(self.frame_4)
        self.rad_det_cn_format_text_xywh_abs.setGeometry(QtCore.QRect(600, 100, 531, 22))
        self.rad_det_cn_format_text_xywh_abs.setObjectName("rad_det_cn_format_text_xywh_abs")
        self.lbl_groundtruth_dir_22 = QtWidgets.QLabel(self.tab_2)
        self.lbl_groundtruth_dir_22.setGeometry(QtCore.QRect(10, 15, 1181, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_groundtruth_dir_22.setFont(font)
        self.lbl_groundtruth_dir_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_groundtruth_dir_22.setObjectName("lbl_groundtruth_dir_22")
        self.lbl_groundtruth_dir_4 = QtWidgets.QLabel(self.tab_2)
        self.lbl_groundtruth_dir_4.setGeometry(QtCore.QRect(10, 55, 101, 17))
        self.lbl_groundtruth_dir_4.setObjectName("lbl_groundtruth_dir_4")
        self.btn_groundtruth_dir_3 = QtWidgets.QPushButton(self.tab_2)
        self.btn_groundtruth_dir_3.setGeometry(QtCore.QRect(1170, 50, 31, 27))
        self.btn_groundtruth_dir_3.setObjectName("btn_groundtruth_dir_3")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.btn_gt_dir.clicked.connect(Dialog.btn_gt_dir_clicked)
        self.btn_gt_images_dir.clicked.connect(Dialog.btn_gt_images_dir_clicked)
        self.btn_stats_det.clicked.connect(Dialog.btn_statistics_det_clicked)
        self.btn_stats_gt.clicked.connect(Dialog.btn_gt_statistics_clicked)
        self.btn_groundtruth_dir_5.clicked.connect(Dialog.btn_gt_classes_clicked)
        self.btn_groundtruth_dir_3.clicked.connect(Dialog.btn_det_dir_clicked)
        self.btn_groundtruth_dir_4.clicked.connect(Dialog.btn_det_classes_clicked)
        self.btn_run.clicked.connect(Dialog.btn_run_clicked)
        self.btn_output_dir.clicked.connect(Dialog.btn_output_dir_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txb_gt_dir, self.btn_gt_dir)
        Dialog.setTabOrder(self.btn_gt_dir, self.txb_gt_images_dir)
        Dialog.setTabOrder(self.txb_gt_images_dir, self.btn_gt_images_dir)
        Dialog.setTabOrder(self.btn_gt_images_dir, self.rad_gt_format_coco_json)
        Dialog.setTabOrder(self.rad_gt_format_coco_json, self.rad_gt_format_openimages_csv)
        Dialog.setTabOrder(self.rad_gt_format_openimages_csv, self.rad_gt_format_labelme_xml)
        Dialog.setTabOrder(self.rad_gt_format_labelme_xml, self.rad_gt_format_yolo_text)
        Dialog.setTabOrder(self.rad_gt_format_yolo_text, self.rad_gt_format_imagenet_xml)
        Dialog.setTabOrder(self.rad_gt_format_imagenet_xml, self.rad_gt_format_pascalvoc_xml)
        Dialog.setTabOrder(self.rad_gt_format_pascalvoc_xml, self.rad_gt_format_abs_values_text)
        Dialog.setTabOrder(self.rad_gt_format_abs_values_text, self.btn_stats_gt)
        Dialog.setTabOrder(self.btn_stats_gt, self.btn_stats_det)
        Dialog.setTabOrder(self.btn_stats_det, self.txb_det_dir)
        Dialog.setTabOrder(self.txb_det_dir, self.btn_groundtruth_dir_3)
        Dialog.setTabOrder(self.btn_groundtruth_dir_3, self.rad_det_ci_format_text_yolo_rel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Object Detection Metrics"))
        self.lbl_groundtruth_dir_26.setText(_translate("Dialog", "COCO Average Precision (AP):"))
        self.chb_metric_AP75_coco.setText(_translate("Dialog", "AP@75"))
        self.chb_metric_AP50_coco.setText(_translate("Dialog", "AP@50"))
        self.chb_metric_AP_coco.setText(_translate("Dialog", "AP@[.50: .05: .95]"))
        self.chb_metric_AR_max100.setText(_translate("Dialog", "AR max=100"))
        self.chb_metric_AR_max10.setText(_translate("Dialog", "AR max=10"))
        self.chb_metric_AR_max1.setText(_translate("Dialog", "AR max=1"))
        self.chb_metric_APmedium_coco.setText(_translate("Dialog", "AP medium"))
        self.chb_metric_APlarge_coco.setText(_translate("Dialog", "AP large"))
        self.chb_metric_APsmall_coco.setText(_translate("Dialog", "AP small"))
        self.chb_metric_AR_medium.setText(_translate("Dialog", "AR medium"))
        self.chb_metric_AR_large.setText(_translate("Dialog", "AR large"))
        self.chb_metric_AR_small.setText(_translate("Dialog", "AR small"))
        self.lbl_groundtruth_dir_31.setText(_translate("Dialog", "COCO Average Recall (AR):"))
        self.lbl_detections_dir_6.setText(_translate("Dialog", "PASCAL VOC:"))
        self.chb_metric_AP_pascal.setText(_translate("Dialog", "AP per class"))
        self.chb_metric_mAP_pascal.setText(_translate("Dialog", "mAP"))
        self.lbl_IOU_thresh.setText(_translate("Dialog", "IOU threshold:"))
        self.lbl_groundtruth_dir_23.setText(_translate("Dialog", "Metrics"))
        self.btn_run.setToolTip(_translate("Dialog", "The configurations will be applied in a random ground truth image."))
        self.btn_run.setText(_translate("Dialog", "RUN"))
        self.btn_output_dir.setText(_translate("Dialog", "..."))
        self.lbl_groundtruth_dir_28.setText(_translate("Dialog", "Output:"))
        self.btn_stats_gt.setToolTip(_translate("Dialog", "The configurations will be applied in a random ground truth image."))
        self.btn_stats_gt.setText(_translate("Dialog", "show ground-truth statistics"))
        self.lbl_groundtruth_dir.setText(_translate("Dialog", "Annotations:"))
        self.btn_gt_dir.setText(_translate("Dialog", "..."))
        self.lbl_groundtruth_dir_27.setText(_translate("Dialog", "* required for yolo (.txt) format only."))
        self.lbl_groundtruth_dir_25.setText(_translate("Dialog", "Classes (*):"))
        self.lbl_groundtruth_dir_3.setText(_translate("Dialog", "Ground truth"))
        self.lbl_groundtruth_dir_2.setText(_translate("Dialog", "Images:"))
        self.btn_gt_images_dir.setText(_translate("Dialog", "..."))
        self.rad_gt_format_coco_json.setText(_translate("Dialog", "COCO (.json)"))
        self.lbl_detections_dir_3.setText(_translate("Dialog", "Coordinates format:"))
        self.rad_gt_format_imagenet_xml.setToolTip(_translate("Dialog", "<html><head/><body><p>Ground-truth format provided by PASCAL VOC annotated files (.XML):</p><p><span style=\" font-weight:600;\">Format: </span>&lt;class_name&gt; &lt;left&gt; &lt;top&gt; &lt;right&gt; &lt;bottom&gt;</p><p><span style=\" font-weight:600;\">Coordinates values:</span> Absolute</p><p><span style=\" font-weight:600;\">Reference: </span><a href=\"http://host.robots.ox.ac.uk/pascal/VOC/voc2012/htmldoc/index.html\"><span style=\" text-decoration: underline; color:#0000ff;\">http://host.robots.ox.ac.uk/pascal/VOC/voc2012/htmldoc/index.html</span></a>"))
        self.rad_gt_format_imagenet_xml.setText(_translate("Dialog", "ImageNet (.xml)"))
        self.rad_gt_format_openimages_csv.setText(_translate("Dialog", "OpenImage dataset (.csv)"))
        self.rad_gt_format_labelme_xml.setText(_translate("Dialog", "Label Me (.xml)"))
        self.rad_gt_format_pascalvoc_xml.setText(_translate("Dialog", "PASCAL VOC (.xml)"))
        self.rad_gt_format_abs_values_text.setToolTip(_translate("Dialog", "<html><head/><body><p>&lt;class&gt; &lt;left&gt; &lt;top&gt; &lt;right&gt; &lt;bottom&gt; (ABSOLUTE)</p></body></html>"))
        self.rad_gt_format_abs_values_text.setText(_translate("Dialog", "Absolute values (.txt)"))
        self.rad_gt_format_yolo_text.setText(_translate("Dialog", "(*) YOLO (.txt)"))
        self.rad_gt_format_cvat_xml.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Format:</span> A unique XML file containing all detections of the dataset in the CVAT format as described at <a href=\"https://github.com/openvinotoolkit/cvat/blob/7512fd6883829ff2692ef42a5a41a06f3805da14/cvat/apps/documentation/xml_format.md\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/openvinotoolkit/cvat/blob/7512fd6883829ff2692ef42a5a41a06f3805da14/cvat/apps/documentation/xml_format.md</span></a>"))
        self.rad_gt_format_cvat_xml.setText(_translate("Dialog", "CVAT format (.xml)"))
        self.btn_groundtruth_dir_5.setText(_translate("Dialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Ground truth"))
        self.btn_stats_det.setToolTip(_translate("Dialog", "The configurations will be applied in a random ground truth image."))
        self.btn_stats_det.setText(_translate("Dialog", "show detections statistics"))
        self.lbl_groundtruth_dir_24.setText(_translate("Dialog", "Classes (*):"))
        self.btn_groundtruth_dir_4.setText(_translate("Dialog", "..."))
        self.lbl_groundtruth_dir_29.setText(_translate("Dialog", "* required for formats with <class_id> only."))
        self.rad_det_ci_format_text_yolo_rel.setText(_translate("Dialog", "(*) <class_id> <confidence> <x_center> <y_center> <width> <height> (RELATIVE)"))
        self.lbl_detections_dir_5.setText(_translate("Dialog", "Coordinates format:"))
        self.rad_det_ci_format_text_xywh_abs.setText(_translate("Dialog", "(*) <class_id> <confidence> <left> <top> <width> <height> (ABSOLUTE)"))
        self.rad_det_ci_format_text_xyx2y2_abs.setText(_translate("Dialog", "(*) <class_id> <confidence> <left> <top> <right> <bottom> (ABSOLUTE)"))
        self.rad_det_format_coco_json.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Format:</span> A unique json file containing all detections of the dataset in the COCO detection format as described at<span style=\" font-weight:600;\"/><a href=\"https://cocodataset.org/#format-results\"><span style=\" text-decoration: underline; color:#0000ff;\">https://cocodataset.org/#format-results</span></a>"))
        self.rad_det_format_coco_json.setText(_translate("Dialog", "COCO format (.json)"))
        self.rad_det_cn_format_text_xyx2y2_abs.setText(_translate("Dialog", "<class_name> <confidence> <left> <top> <right> <bottom> (ABSOLUTE)"))
        self.rad_det_cn_format_text_yolo_rel.setText(_translate("Dialog", "<class_name> <confidence> <x_center> <y_center> <width> <height> (RELATIVE)"))
        self.rad_det_cn_format_text_xywh_abs.setText(_translate("Dialog", "<class_name> <confidence> <left> <top> <width> <height> (ABSOLUTE)"))
        self.lbl_groundtruth_dir_22.setText(_translate("Dialog", "Detections"))
        self.lbl_groundtruth_dir_4.setText(_translate("Dialog", "Annotations:"))
        self.btn_groundtruth_dir_3.setText(_translate("Dialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Detections"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

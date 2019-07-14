import sys
import Utils
import Train
from PyQt4 import QtCore, QtGui, uic
 
form_class = uic.loadUiType("MainWindow.ui")[0]      # Load the UI
 
class Main(QtGui.QDialog, form_class):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.dataBtn.clicked.connect(self.generateImage)  # Bind the event handlers
        self.trainBtn.clicked.connect(self.train)
        self.testBtn.clicked.connect(self.test)

        self.dataGV.setScene(QtGui.QGraphicsScene())
        self.trainGV.setScene(QtGui.QGraphicsScene())
        self.testGV.setScene(QtGui.QGraphicsScene())

        self.data = None
        self.training_set = None

    def generateImage(self):
        points = self.points.value()
        self.data = Utils.spiralDouble(256, 256, points, 0, 0.1, self.distance.value(), self.noise.value())
        self.draw(self.dataGV.scene(), self.data)


    def train(self):
        ibl = self.ibl1.isChecked()

        if (self.data):
            if (ibl):
                result = Train.ibl1_training_set(self.data)
            else:
                result = Train.ibl2_training_set(self.data)
        
            self.training_set = result['data']
            self.draw(self.trainGV.scene(), self.training_set)
            self.well.setText(str(result['well']))
            self.badly.setText(str(result['badly']))

    def test(self):
        if (self.training_set):
            data = Train.test(self.training_set, 256, 256, 1, self.step.value())
            self.draw(self.testGV.scene(),data)



    def draw(self,scene, data):
        colors = [QtGui.qRgb(255, 0,   0),
                  QtGui.qRgb(  0, 0, 255)]


        image = QtGui.QImage(256, 256, QtGui.QImage.Format_RGB32)
        image.fill(QtGui.qRgb(0, 0, 0))

        for d in data:
            image.setPixel(d['x'], d['y'], colors[d['class']])

        pixmap = QtGui.QPixmap(256, 256)
        pixmap.convertFromImage(image)
        pixItem = QtGui.QGraphicsPixmapItem(pixmap)
        
        scene.clear()
        scene.addItem(pixItem)


app = QtGui.QApplication(sys.argv)
myWindow = Main(None)
myWindow.show()
app.exec_()

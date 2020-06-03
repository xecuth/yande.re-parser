import sys
import gui


app = gui.QtWidgets.QApplication([])
application = gui.MyWindow()
application.show()

sys.exit(app.exec())

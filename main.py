from PySide6 import QtWidgets
import json

from untitled import Ui_MainWindow



class BreedSelector(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Dog Quiz")

        print("program launch succesful")

        self.data = json.load(open("data.json", "r"))

        self.ui.button_next_page_0.clicked.connect(self.next_page)
        self.ui.button_next_page_1.clicked.connect(self.next_page)
        self.ui.button_next_page_2.clicked.connect(self.next_page)
        self.ui.button_next_page_3.clicked.connect(self.next_page)
        self.ui.button_next_page_4.clicked.connect(self.next_page)
        self.ui.button_next_page_5.clicked.connect(self.next_page)
        self.ui.button_next_page_6.clicked.connect(self.next_page)

        self.ui.button_prev_page_1.clicked.connect(self.prev_page)
        self.ui.button_prev_page_2.clicked.connect(self.prev_page)
        self.ui.button_prev_page_3.clicked.connect(self.prev_page)
        self.ui.button_prev_page_4.clicked.connect(self.prev_page)
        self.ui.button_prev_page_5.clicked.connect(self.prev_page)
        self.ui.button_prev_page_6.clicked.connect(self.prev_page)
        self.ui.button_prev_page_7.clicked.connect(self.prev_page)

        self.ui.button_restart.clicked.connect(self.button_restart)

        

    def choose_breed(self):
        is_large = self.ui.radioButton_1_yes.isChecked()
        is_allergenic = self.ui.radioButton_2_yes.isChecked()
        is_personable = self.ui.radioButton_3_yes.isChecked()
        has_fur = self.ui.radioButton_4_yes.isChecked()
        is_working = self.ui.radioButton_5_yes.isChecked()
        is_protective = self.ui.radioButton_6_yes.isChecked()

    
        recommendations = []        
        for dog in self.data:
            if (dog['large'] == is_large and
                dog['allergy'] == is_allergenic and
                dog['others'] == is_personable and
                dog['fur'] == has_fur and
                dog['working'] == is_working and
                dog['temperment'] == is_protective):
                recommendations.append(dog)
                
        max_recommendations = 7

        unique_recommendations = list({v['name']:v for v in recommendations}.values())

        if len(unique_recommendations):
            limited_recommendations = unique_recommendations[:max_recommendations]
            breeds = " or \n".join([recomendation["name"] for recomendation in limited_recommendations])
            return breeds
        else:
            return "No recomendations available"




        
        
        
    def next_page(self):
        match self.ui.stackedWidget.currentIndex():
            case 1:
                if not self.ui.radioButton_1_yes.isChecked() and not self.ui.radioButton_1_no.isChecked():
                    QtWidgets.QMessageBox.critical(self, "Make a selection", "Size preference not selected")
                    return
            case 2:
                if not self.ui.radioButton_2_yes.isChecked() and not self.ui.radioButton_2_no.isChecked():
                    QtWidgets.QMessageBox.critical(self, "Make a selection", "Hypoallergenic preference not selected")
                    return
            case 3:
                if not self.ui.radioButton_3_yes.isChecked() and not self.ui.radioButton_3_no.isChecked():
                    QtWidgets.QMessageBox.critical(self, "Make a selection", "Good with other dogs preference not selected")
                    return
            case 4:
                if not self.ui.radioButton_4_yes.isChecked() and not self.ui.radioButton_4_no.isChecked():
                    QtWidgets.QMessageBox.critical(self, "Make a selection", "Straight or fuzzy fur preference not selected")
                    return
            case 5:
                if not self.ui.radioButton_5_yes.isChecked() and not self.ui.radioButton_5_no.isChecked():
                    QtWidgets.QMessageBox.critical(self, "Make a selection", "Working or house dog preference not selected")
                    return
            case 6:
                if not self.ui.radioButton_6_yes.isChecked() and not self.ui.radioButton_6_no.isChecked():
                    QtWidgets.QMessageBox.critical(self, "Make a selection", "Teperment preference not selected")
                    return
                
                chosen_breed = self.choose_breed()

                self.ui.label_7_detail.setText(chosen_breed)

        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex() + 1)
        
    def prev_page(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex() - 1)
        
    def button_restart(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex() - 7)
        self.ui.radioButton_1_yes.setAutoExclusive(False)
        self.ui.radioButton_1_yes.setChecked(False)
        self.ui.radioButton_1_yes.setAutoExclusive(True)
        self.ui.radioButton_1_no.setAutoExclusive(False)
        self.ui.radioButton_1_no.setChecked(False)
        self.ui.radioButton_1_no.setAutoExclusive(True)
        self.ui.radioButton_2_yes.setAutoExclusive(False)
        self.ui.radioButton_2_yes.setChecked(False)
        self.ui.radioButton_2_yes.setAutoExclusive(True)
        self.ui.radioButton_2_no.setAutoExclusive(False)
        self.ui.radioButton_2_no.setChecked(False)
        self.ui.radioButton_2_no.setAutoExclusive(True)
        self.ui.radioButton_3_yes.setAutoExclusive(False)
        self.ui.radioButton_3_yes.setChecked(False)
        self.ui.radioButton_3_yes.setAutoExclusive(True)
        self.ui.radioButton_3_no.setAutoExclusive(False)
        self.ui.radioButton_3_no.setChecked(False)
        self.ui.radioButton_3_no.setAutoExclusive(True)
        self.ui.radioButton_4_yes.setAutoExclusive(False)
        self.ui.radioButton_4_yes.setChecked(False)
        self.ui.radioButton_4_yes.setAutoExclusive(True)
        self.ui.radioButton_4_no.setAutoExclusive(False)
        self.ui.radioButton_4_no.setChecked(False)
        self.ui.radioButton_4_no.setAutoExclusive(True)
        self.ui.radioButton_5_yes.setAutoExclusive(False)
        self.ui.radioButton_5_yes.setChecked(False)
        self.ui.radioButton_5_yes.setAutoExclusive(True)
        self.ui.radioButton_5_no.setAutoExclusive(False)
        self.ui.radioButton_5_no.setChecked(False)
        self.ui.radioButton_5_no.setAutoExclusive(True)
        self.ui.radioButton_6_yes.setAutoExclusive(False)
        self.ui.radioButton_6_yes.setChecked(False)
        self.ui.radioButton_6_yes.setAutoExclusive(True)
        self.ui.radioButton_6_no.setAutoExclusive(False)
        self.ui.radioButton_6_no.setChecked(False)
        self.ui.radioButton_6_no.setAutoExclusive(True)
       


app = QtWidgets.QApplication()
main_window = BreedSelector()
main_window.show()
app.exec()

print("program completion")
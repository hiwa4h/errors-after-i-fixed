import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QTableView, QVBoxLayout, QWidget
import mysql.connector

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Connect to the MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="database_name"
        )

        # Retrieve the data from the database
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT * FROM table_name")
        self.data = self.cursor.fetchall()

        # Create the search bar
        self.search_bar = QLineEdit()
        self.search_bar.textChanged.connect(self.search)

        # Create the table view
        self.table_view = QTableView()

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.search_bar)
        layout.addWidget(self.table_view)
        self.setLayout(layout)

    def search(self, query):
        query = f"%{query}%"
        self.cursor.execute("SELECT * FROM table_name WHERE column_name LIKE %s", (query,))
        self.data = self.cursor.fetchall()
        self.table_view.setModel(self.data)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

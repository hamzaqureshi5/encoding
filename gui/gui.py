import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui.forms.main import Ui_MainWindow  # Import the UI class from the converted Python file
from core.generator.utils import EncodingUtils, DataGenerator
from pydantic import BaseModel, ValidationError, constr


# Define Pydantic models for input validation
class ICCID(BaseModel):
    iccid: constr(min_length=18, max_length=20)


class IMSI(BaseModel):
    imsi: constr(min_length=15, max_length=18)


class KEYS(BaseModel):
    k4: constr(min_length=32, max_length=64)
    op: constr(min_length=32, max_length=32)
    ki: constr(min_length=32, max_length=32)


# Utility function to generate keys
def gen_opc_eki(op: str, transport: str, ki: str) -> tuple[str, str, str]:
    return ki, DataGenerator.generate_opc(op, ki), DataGenerator.generate_eki(transport, ki)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()

        # Connect UI elements to their respective methods
        self.ui.k4.textChanged.connect(self.validate_k4_length)
        self.ui.ki.textChanged.connect(lambda: self.validate_text_length(self.ui.ki, 32))
        self.ui.op.textChanged.connect(lambda: self.validate_text_length(self.ui.op, 32))
        self.ui.iccid_enc_btn.clicked.connect(self.iccid_enc_function)
        self.ui.iccid_dec_btn.clicked.connect(self.iccid_dec_function)
        self.ui.imsi_enc_btn.clicked.connect(self.imsi_enc_function)
        self.ui.imsi_dec_btn.clicked.connect(self.imsi_dec_function)
        self.ui.enc_keys_conv_btn.clicked.connect(self.keys)

    def validate_text_length(self, widget, expected_length: int):
        """Validate the length of text in a QLineEdit and apply styles accordingly."""
        text = widget.text()
        widget.setStyleSheet(
            """
            QLineEdit {
                border: 2px solid {color};
                border-radius: 5px;
                padding: 5px;
            }
            """.format(color="green" if len(text) == expected_length else "red")
        )

    def validate_k4_length(self):
        """Validate that the length of k4 is a multiple of 32."""
        text = self.ui.k4.text()
        is_valid = len(text) > 0 and len(text) % 32 == 0
        self.ui.k4.setStyleSheet(
            """
            QLineEdit {
                border: 2px solid {color};
                border-radius: 5px;
            }
            """.format(color="green" if is_valid else "red")
        )

    def iccid_enc_function(self):
        """Handle ICCID encryption."""
        try:
            iccid = ICCID(iccid=self.ui.iccid_input.text())
            self.ui.iccid_output.setText(EncodingUtils.enc_iccid(iccid.iccid))
        except ValidationError as e:
            print(e)

    def iccid_dec_function(self):
        """Handle ICCID decryption."""
        try:
            iccid = ICCID(iccid=self.ui.iccid_input.text())
            self.ui.iccid_output.setText(EncodingUtils.dec_iccid(iccid.iccid))
        except ValidationError as e:
            print(e)

    def imsi_enc_function(self):
        """Handle IMSI encryption."""
        try:
            imsi = IMSI(imsi=self.ui.imsi_input.text())
            self.ui.imsi_output.setText(EncodingUtils.enc_imsi(imsi.imsi))
        except ValidationError as e:
            print(e)

    def imsi_dec_function(self):
        """Handle IMSI decryption."""
        try:
            imsi = IMSI(imsi=self.ui.imsi_input.text())
            self.ui.imsi_output.setText(EncodingUtils.dec_imsi(imsi.imsi))
        except ValidationError as e:
            print(e)

    def keys(self):
        """Generate and display EKI and OPC values."""
        try:
            k = KEYS(ki=self.ui.ki.text(), op=self.ui.op.text(), k4=self.ui.k4.text())
            ki, opc, eki = gen_opc_eki(k.op, k.k4, k.ki)

            self.ui.eki.setText(opc)
            self.ui.opc.setText(eki)
        except ValidationError as e:
            print(e)


# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow
# from gui.forms.main import Ui_MainWindow # Import the UI class from the converted Python file
# from core.generator.utils import EncodingUtils
# from core.generator.utils import DataGenerator
# from pydantic import BaseModel, Field, conint, constr
# from pydantic import ValidationError
#
#
# class ICCID(BaseModel):
#     iccid: constr(min_length=18, max_length=20)  # type: ignore
#
#
# class IMSI(BaseModel):
#     imsi: constr(min_length=15, max_length=15)  # type: ignore
#
#
# class KEYS(BaseModel):
#     k4: constr(min_length=32, max_length=64)  # type: ignore
#     op: constr(min_length=32, max_length=32)  # type: ignore
#     ki: constr(min_length=32, max_length=32)  # type: ignore
#
#
# def gen_opc_eki(op, transport, ki) -> (str, str, str):
#     return ki,DataGenerator.generate_opc(op, ki),DataGenerator.generate_eki(transport, ki)
#
#
# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.ui = self.setupUi(self)  # This sets up the UI created in the .ui file
#
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.showMaximized()
#         self.ui.k4.textChanged.connect(self.validate_k4_length)
#         self.ui.ki.textChanged.connect(self.on_ki_text_changed)
#         self.ui.op.textChanged.connect(self.on_op_text_changed)
#         self.ui.iccid_enc_btn.clicked.connect(self.iccid_enc_function)
#         self.ui.iccid_dec_btn.clicked.connect(self.iccid_dec_function)
#
#         self.ui.imsi_enc_btn.clicked.connect(self.imsi_enc_function)
#         self.ui.imsi_dec_btn.clicked.connect(self.imsi_dec_function)
#
#         self.ui.enc_keys_conv_btn.clicked.connect(self.keys)
#
#     def on_ki_text_changed(self):
#
#         text = self.ui.ki.text()
#
#         if len(text) == 32:
#             self.ui.ki.setStyleSheet("""
#                 QLineEdit {
#                     border: 2px solid green;
#                     border-radius: 5px;
#                     padding: 5px;
#                 }
#             """)
#         else:
#             self.ui.ki.setStyleSheet("""
#                 QLineEdit {
#                     border: 2px solid red;
#                     border-radius: 5px;
#                     padding: 5px;
#                 }
#             """)
#
#     def on_op_text_changed(self):
#
#         text = self.ui.op.text()
#
#         if len(text) == 32:
#             self.ui.op.setStyleSheet("""
#                 QLineEdit {
#                     border: 2px solid green;
#                     border-radius: 5px;
#                     padding: 5px;
#                 }
#             """)
#         else:
#             self.ui.op.setStyleSheet("""
#                 QLineEdit {
#                     border: 2px solid red;
#                     border-radius: 5px;
#                     padding: 5px;
#                 }
#             """)
#     def validate_k4_length(self):
#
#         text = self.ui.k4.text()
#         if len(text) % 32 == 0 and len(text) > 0:
#             self.ui.k4.setStyleSheet("""
#                 QLineEdit {
#                     border: 2px solid green;
#                     border-radius: 5px;
#                 }
#             """)
#         else:
#             self.ui.k4.setStyleSheet("""
#                 QLineEdit {
#                     border: 2px solid red;
#                     border-radius: 5px;
#                 }
#             """)
#     def gen_keys_function(self):
#         (ki, op, k4) = self.ui.ki, self.ui.op, self.ui.k4
#
#     def iccid_enc_function(self):
#         print(str(self.ui.iccid_input.text()))
#         try:
#             iccid = ICCID(iccid=str(self.ui.iccid_input.text()))
#
#             self.ui.iccid_output.setText(EncodingUtils.enc_iccid(str(iccid.iccid)))
#         except ValidationError as e:
#             print(e)
#
#     def iccid_dec_function(self):
#         print(str(self.ui.iccid_input.text()))
#         try:
#             iccid = ICCID(iccid=str(self.ui.iccid_input.text()))
#             self.ui.iccid_output.setText(EncodingUtils.dec_iccid(str(iccid.iccid)))
#         except ValidationError as e:
#             print(e)
#
#     def imsi_enc_function(self):
#         print(str(self.ui.imsi_input.text()))
#         try:
#             imsi = IMSI(imsi=str(self.ui.imsi_input.text()))
#             self.ui.imsi_output.setText(EncodingUtils.enc_imsi(str(imsi.imsi)))
#         except ValidationError as e:
#             print(e)
#
#     def imsi_dec_function(self):
#         print(str(self.ui.imsi_input.text()))
#         try:
#             imsi = IMSI(imsi=str(self.ui.imsi_input.text()))
#             self.ui.imsi_output.setText(EncodingUtils.dec_imsi("081911111111111"))
#         except ValidationError as e:
#             print(e)
#
#     def keys(self) -> None:
#         try:
#             k = KEYS(ki=self.ui.ki.text(), op=self.ui.op.text(), k4=self.ui.k4.text())
#
#             k_input = KEYS(ki=self.ui.ki.text(), op=self.ui.op.text(), k4=self.ui.k4.text())
#
#             k_out = gen_opc_eki(k_input.op, k_input.k4, k_input.ki)
#
#             self.ui.eki.setText(k_out[1])
#             self.ui.opc.setText(k_out[2])
#
#
#
#         except ValidationError as e:
#             print(e)

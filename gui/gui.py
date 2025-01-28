import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui.forms.main import Ui_MainWindow
from core.generator.utils import EncodingUtils, DataGenerator
from pydantic import BaseModel, Field, ValidationError, constr


# Validation Models
class ICCID_ENCODED(BaseModel):
    iccid: constr(min_length=20, max_length=20)  # type: ignore

class ICCID_DECODED(BaseModel):
    iccid: constr(min_length=18, max_length=19)  # type: ignore


class IMSI_ENCODED(BaseModel):
    imsi: constr(min_length=18, max_length=18)  # type: ignore

class IMSI_DECODED(BaseModel):
    imsi: constr(min_length=15, max_length=15)  # type: ignore


class KEYS(BaseModel):
    k4: constr(min_length=32, max_length=64)  # type: ignore
    op: constr(min_length=32, max_length=32)  # type: ignore
    ki: constr(min_length=32, max_length=32)  # type: ignore


# Business Logic
class KeyGenerator:
    @staticmethod
    def generate_opc_eki(op: str, transport: str, ki: str) -> tuple[str, str, str]:
        """
        Generate OPC and EKI values.
        """
        return ki, DataGenerator.generate_opc(op, ki), DataGenerator.generate_eki(transport, ki)


class Validator:
    @staticmethod
    def validate_iccid_encoded(iccid: str) -> ICCID_ENCODED:
        """
        Validate ICCID input.
        """
        return ICCID_ENCODED(iccid=iccid)

    @staticmethod
    def validate_iccid_decoded(iccid: str) -> ICCID_DECODED:
        """
        Validate ICCID input.
        """
        return ICCID_DECODED(iccid=iccid)
    @staticmethod
    def validate_imsi_encoded(imsi: str) -> IMSI_ENCODED:
        """
        Validate IMSI input.
        """
        return IMSI_ENCODED(imsi=imsi)

    @staticmethod
    def validate_imsi_decoded(imsi: str) -> IMSI_DECODED:
        """
        Validate IMSI input.
        """
        return IMSI_DECODED(imsi=imsi)

    @staticmethod
    def validate_keys(ki: str, op: str, k4: str) -> KEYS:
        """
        Validate key inputs.
        """
        return KEYS(ki=ki, op=op, k4=k4)


class Styler:
    @staticmethod
    def apply_style(widget, valid: bool) -> None:
        """
        Apply a green or red border style to a widget based on validation status.
        """
        color = "green" if valid else "red"
        widget.setStyleSheet(f"""
            QLineEdit {{
                border: 2px solid {color};
                border-radius: 5px;
                padding: 5px;
            }}
        """)


# Main Window Class
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()

        self.statusBar().showMessage("Ready", 3000)  # Show an initial message for 3 seconds

        # Connect UI signals to methods
        self._connect_signals()

    def _connect_signals(self) -> None:
        """
        Connect signals to appropriate methods.
        """
        self.ui.k4.textChanged.connect(self._validate_k4)
        self.ui.ki.textChanged.connect(self._validate_ki)
        self.ui.op.textChanged.connect(self._validate_op)
        self.ui.iccid_enc_btn.clicked.connect(self._iccid_enc_function)
        self.ui.iccid_dec_btn.clicked.connect(self._iccid_dec_function)
        self.ui.imsi_enc_btn.clicked.connect(self._imsi_enc_function)
        self.ui.imsi_dec_btn.clicked.connect(self._imsi_dec_function)
        self.ui.enc_keys_conv_btn.clicked.connect(self._generate_keys)

    # Validation Methods
    def _validate_ki(self):
        self._validate_input(self.ui.ki, len(self.ui.ki.text()) == 32)

    def _validate_op(self):
        self._validate_input(self.ui.op, len(self.ui.op.text()) == 32)

    def _validate_k4(self):
        text = self.ui.k4.text()
        is_valid = len(text) % 32 == 0 and len(text) > 0
        self._validate_input(self.ui.k4, is_valid)

    def _validate_input(self, widget, is_valid: bool) -> None:
        """
        Validate input and apply styles.
        """
        Styler.apply_style(widget, is_valid)

    def _iccid_enc_function(self):
        try:
            iccid = Validator.validate_iccid_decoded(self.ui.iccid_input.text())
            encoded = EncodingUtils.enc_iccid(iccid.iccid)
            self.ui.iccid_output.setText(encoded)
            self._show_status_message("ICCID encoded successfully.", is_error=False)
        except ValidationError as e:
            self._show_status_message(f"ICCID Validation Error: {str(e)}", is_error=True)

    def _iccid_dec_function(self):
        try:
            iccid = Validator.validate_iccid_encoded(self.ui.iccid_input.text())
            decoded = EncodingUtils.dec_iccid(iccid.iccid)
            self.ui.iccid_output.setText(decoded)
            self._show_status_message("ICCID decoded successfully.", is_error=False)
        except ValidationError as e:
            self._show_status_message(f"ICCID Validation Error: {str(e)}", is_error=True)

    def _imsi_enc_function(self):
        try:
            imsi = Validator.validate_imsi_decoded(self.ui.imsi_input.text())
            encoded = EncodingUtils.enc_imsi(imsi.imsi)
            self.ui.imsi_output.setText(encoded)
            self._show_status_message("IMSI encoded successfully.", is_error=False)
        except ValidationError as e:
            self._show_status_message(f"IMSI Validation Error: {str(e)}", is_error=True)

    def _imsi_dec_function(self):
        try:
            imsi = Validator.validate_imsi_encoded(self.ui.imsi_input.text())
            decoded = EncodingUtils.dec_imsi(imsi.imsi)
            self.ui.imsi_output.setText(decoded)
            self._show_status_message("IMSI decoded successfully.", is_error=False)
        except ValidationError as e:
            self._show_status_message(f"IMSI Validation Error: {str(e)}", is_error=True)

    def _generate_keys(self):
        try:
            keys = Validator.validate_keys(
                self.ui.ki.text(), self.ui.op.text(), self.ui.k4.text()
            )
            ki, opc, eki = KeyGenerator.generate_opc_eki(keys.op, keys.k4, keys.ki)
            self.ui.eki.setText(eki)
            self.ui.opc.setText(opc)
            self._show_status_message("Keys generated successfully.", is_error=False)
        except ValidationError as e:
            self._show_status_message(f"Key Validation Error: {str(e)}", is_error=True)

    def _show_status_message(self, message: str, is_error: bool = True, timeout: int = 5000) -> None:
        """
        Display a status message in the status bar.
        """
        if is_error:
            self.statusBar().setStyleSheet("color: red;")

        else:
            self.statusBar().setStyleSheet("color: green;")
        self.statusBar().showMessage(message, timeout)

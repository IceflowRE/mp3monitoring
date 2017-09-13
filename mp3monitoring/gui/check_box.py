from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtWidgets import QStyle, QStyleOptionButton, QStyledItemDelegate


class CheckBoxDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        check_box_style_option = QStyleOptionButton()
        check_box_style_option.rect = self.get_check_box_rect(option)
        check_box_style_option.state = QStyle.State_Enabled
        self.QApplication.style().drawControl(QStyle.CE_CheckBox, check_box_style_option, painter)

    def get_check_box_rect(self, option):
        check_box_style_option = QStyleOptionButton()
        check_box_rect = self.QApplication.style().subElementRect(QStyle.SE_CheckBoxIndicator, check_box_style_option,
                                                                  None)
        check_box_point = QPoint(option.rect.x() + option.rect.width() / 2 - check_box_rect.width() / 2,
                                 option.rect.y() + option.rect.height() / 2 - check_box_rect.height() / 2)
        return QRect(check_box_point, check_box_rect.size())

import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget, QLabel

import enemydata as Bestiary


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        app_font: QFont = QFont("Helvetica", 9)

        app_resolution: tuple = (975, 400)
        self.bestiary_selector = Bestiary.Bestiary.bestiary_list

        self.setWindowTitle("Final Fantasy VI Advance Bestiary")
        self.setFixedSize(app_resolution[0], app_resolution[1])

        self.enemy_list: QListWidget = QListWidget(self)
        self.enemy_list.setFixedHeight(290)
        self.enemy_list.setFixedWidth(200)
        self.enemy_list.setFont(app_font)
        self.enemy_list.adjustSize()
        self.enemy_list.move(25, 50)

        enemy_counter: int = 1
        for enemy in Bestiary.Bestiary.bestiary_list:
            if enemy_counter <= 9:
                self.enemy_list.addItem(f"00{enemy_counter} {enemy.name}")
            elif 10 <= enemy_counter <= 99:
                self.enemy_list.addItem(f"0{enemy_counter} {enemy.name}")
            else:
                self.enemy_list.addItem(f"{enemy_counter} {enemy.name}")
            enemy_counter += 1

        # Main Labels

        list_label: QLabel = QLabel("Enemy List", self)
        list_label.move(self.enemy_list.pos().x(), self.enemy_list.pos().y() - 25)

        self.enemy_level_label: QLabel = QLabel("Level", self)

        health_label: QLabel = QLabel("HP", self)

        mana_label: QLabel = QLabel("MP", self)

        attack_label: QLabel = QLabel("Attack", self)

        defense_label: QLabel = QLabel("Defense", self)

        evasion_label: QLabel = QLabel("Evasion", self)

        magicpower_label: QLabel = QLabel("Magic", self)

        magicdefense_label: QLabel = QLabel("Magic Defense", self)

        magicevasion_label: QLabel = QLabel("Magic Evasion", self)

        gil_label: QLabel = QLabel("Gil", self)

        exp_label: QLabel = QLabel("EXP", self)

        label_bundle: tuple = (self.enemy_level_label, health_label, mana_label, attack_label,
                               defense_label, evasion_label, magicpower_label,
                               magicdefense_label, magicevasion_label, gil_label,
                               exp_label)

        # Used for the for loop to get info from previous labels and modify screen positions effectively
        index_counter: int = 0
        for label in label_bundle:
            if index_counter == 0:
                label.setFont(app_font)
                label.adjustSize()
                label.move(280, 50)
            else:
                label.setFont(app_font)
                label.adjustSize()
                label.move(label_bundle[int(index_counter - 1)].pos().x(),
                           label_bundle[int(index_counter - 1)].pos().y() + 15)
            index_counter += 1

        steal_label: QLabel = QLabel("Steal", self)
        steal_label.move(exp_label.pos().x(), exp_label.pos().y() + 30)

        drops_label: QLabel = QLabel("Drops", self)
        drops_label.move(steal_label.pos().x(), steal_label.pos().y() + 45)

        immune_section_label: QLabel = QLabel("Immune To", self)
        immune_section_label.move(self.enemy_level_label.pos().x() + 300, self.enemy_level_label.pos().y())

        weaknesses_section_label: QLabel = QLabel("Weak Against", self)
        weaknesses_section_label.move(immune_section_label.pos().x(), immune_section_label.pos().y() + 75)

        absorption_section_label: QLabel = QLabel("Absorbs", self)
        absorption_section_label.move(weaknesses_section_label.pos().x(), weaknesses_section_label.pos().y() + 90)

        enemy_type_section_label: QLabel = QLabel("Type", self)
        enemy_type_section_label.move(immune_section_label.pos().x() + 200, immune_section_label.pos().y())

        status_immunity_label: QLabel = QLabel("Status Immunity", self)
        status_immunity_label.move(enemy_type_section_label.pos().x(),
                                   weaknesses_section_label.pos().y())

        section_label_bundle: tuple = (steal_label, drops_label, immune_section_label, absorption_section_label,
                                       weaknesses_section_label, enemy_type_section_label,
                                       status_immunity_label)

        for sectionlabels in section_label_bundle:
            sectionlabels.setFont(app_font)
            sectionlabels.adjustSize()

        # Value Labels

        self.enemylvl: QLabel = QLabel(self)
        self.enemy_list.clicked.connect(self.enemy_data_change)

        self.enemyhealth: QLabel = QLabel(self)

        self.enemymana: QLabel = QLabel(self)

        self.enemyattack: QLabel = QLabel(self)

        self.enemydefense: QLabel = QLabel(self)

        self.enemyevasion: QLabel = QLabel(self)

        self.enemymagic: QLabel = QLabel(self)

        self.enemymagicdefense: QLabel = QLabel(self)

        self.enemymagicevasion: QLabel = QLabel(self)

        self.enemygil: QLabel = QLabel(self)

        self.enemyexp: QLabel = QLabel(self)

        self.widget_bundle: tuple = (self.enemylvl, self.enemyhealth, self.enemymana, self.enemyattack,
                                     self.enemydefense, self.enemyevasion, self.enemymagic,
                                     self.enemymagicdefense, self.enemymagicevasion, self.enemygil,
                                     self.enemyexp)
        value_widget_counter: int = 0

        for value_label in self.widget_bundle:
            if value_widget_counter == 0:
                value_label.move(self.enemy_level_label.pos().x() + 150, self.enemy_level_label.pos().y())
                value_label.setFont(app_font)
                value_label.adjustSize()
            else:
                value_label.move(self.enemylvl.pos().x(),
                                 self.widget_bundle[value_widget_counter - 1].pos().y() + 15)
                value_label.setFont(app_font)
                value_label.adjustSize()
            value_widget_counter += 1

        self.steal_list_label: QLabel = QLabel(self)
        self.steal_list_label.setFont(app_font)
        self.steal_list_label.adjustSize()
        self.steal_list_label.move(steal_label.pos().x(), steal_label.pos().y() + 15)

        self.drops_list_label: QLabel = QLabel(self)
        self.drops_list_label.setFont(app_font)
        self.drops_list_label.adjustSize()
        self.drops_list_label.move(drops_label.pos().x(), drops_label.pos().y() + 15)

        self.left_column_elemental_immunities: QLabel = QLabel(self)
        self.left_column_elemental_immunities.setFont(app_font)
        self.left_column_elemental_immunities.adjustSize()
        self.left_column_elemental_immunities.move(immune_section_label.pos().x() + 4,
                                                   immune_section_label.pos().y() + 15)

        self.right_column_ele_immunities: QLabel = QLabel(self)
        self.right_column_ele_immunities.setFont(app_font)
        self.right_column_ele_immunities.adjustSize()
        self.right_column_ele_immunities.move(self.left_column_elemental_immunities.pos().x() + 75,
                                              self.left_column_elemental_immunities.pos().y())

        self.enemy_weaknesses_left_column: QLabel = QLabel(self)
        self.enemy_weaknesses_left_column.move(self.left_column_elemental_immunities.pos().x(),
                                               self.left_column_elemental_immunities.pos().y() + 75)

        self.enemy_weaknesses_right_column: QLabel = QLabel(self)
        self.enemy_weaknesses_right_column.move(self.right_column_ele_immunities.pos().x(),
                                                self.right_column_ele_immunities.pos().y() + 75)

        self.weakness_bundle: tuple = (self.enemy_weaknesses_left_column, self.enemy_weaknesses_right_column)

        for weakness in self.weakness_bundle:
            weakness.setFont(app_font)
            weakness.adjustSize()

        self.left_column_absorb_elements_label: QLabel = QLabel(self)
        self.left_column_absorb_elements_label.move(absorption_section_label.pos().x() + 4,
                                                    absorption_section_label.pos().y() + 15)

        self.right_column_absorb_elements_label: QLabel = QLabel(self)
        self.right_column_absorb_elements_label.move(
            self.left_column_absorb_elements_label.pos().x() + 75,
            self.left_column_absorb_elements_label.pos().y()
        )

        self.absorptionbundle: tuple = (self.left_column_absorb_elements_label,
                                        self.right_column_absorb_elements_label)

        for element in self.absorptionbundle:
            element.setFont(app_font)
            element.adjustSize()

        # Enemy Type
        self.first_enemy_type_label: QLabel = QLabel(self)
        self.first_enemy_type_label.move(enemy_type_section_label.pos().x() + 6,
                                         enemy_type_section_label.pos().y() + 15)

        self.second_enemy_type_label: QLabel = QLabel(self)
        self.second_enemy_type_label.move(self.first_enemy_type_label.pos().x() + 75,
                                          self.first_enemy_type_label.pos().y())

        self.enemy_type_bundle: tuple = (self.first_enemy_type_label, self.second_enemy_type_label)

        for enemytype in self.enemy_type_bundle:
            enemytype.setFont(app_font)
            enemytype.adjustSize()

        self.left_side_status_immunities: QLabel = QLabel(self)
        self.left_side_status_immunities.move(status_immunity_label.pos().x() + 6,
                                              status_immunity_label.pos().y() + 15)

        self.right_side_status_immunities: QLabel = QLabel(self)
        self.right_side_status_immunities.move(self.left_side_status_immunities.pos().x()+75,
                                               self.left_side_status_immunities.pos().y())


        self.status_immunity_bundle: tuple = (self.left_side_status_immunities,
                                              self.right_side_status_immunities)

        for immunity in self.status_immunity_bundle:
            immunity.setFont(app_font)
            immunity.adjustSize()

        self.enemy_data_change()

    def enemy_data_change(self):

        self.enemylvl.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].level}")
        self.enemyhealth.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].health}")
        self.enemymana.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].mana}")
        self.enemyattack.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].attack}")
        self.enemydefense.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].defense}")
        self.enemyevasion.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].evasion}")
        self.enemymagic.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].magic_power}")
        self.enemymagicdefense.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].magic_defense}")
        self.enemymagicevasion.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].magic_evasion}")
        self.enemygil.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].gil}")
        self.enemyexp.setText(f"{self.bestiary_selector[int(self.enemy_list.currentRow())].experience}")
        for value_widget in self.widget_bundle:
            value_widget.adjustSize()

        #  Steal Table
        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].steal_table, str):
            self.steal_list_label.setText(f"\t{self.bestiary_selector[int(self.enemy_list.currentRow())].steal_table}")
            self.steal_list_label.adjustSize()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].steal_table, tuple):
            self.steal_list_label.setText(
                f"\t{self.bestiary_selector[int(self.enemy_list.currentRow())].steal_table[0]}\n"
                f"\t{self.bestiary_selector[int(self.enemy_list.currentRow())].steal_table[1]}")
            self.steal_list_label.adjustSize()

        if self.bestiary_selector[int(self.enemy_list.currentRow())].steal_table is None:
            self.steal_list_label.setText("\t---")
            self.steal_list_label.adjustSize()

        #  Drop Table
        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].drop_table, str):
            self.drops_list_label.setText(f"\t{self.bestiary_selector[int(self.enemy_list.currentRow())].drop_table}")
            self.drops_list_label.adjustSize()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].drop_table, tuple):
            self.drops_list_label.setText(
                f"\t{self.bestiary_selector[int(self.enemy_list.currentRow())].drop_table[0]}\n"
                f"\t{self.bestiary_selector[int(self.enemy_list.currentRow())].drop_table[1]}")
            self.drops_list_label.adjustSize()

        if self.bestiary_selector[int(self.enemy_list.currentRow())].drop_table is None:
            self.drops_list_label.setText("\t---")
            self.drops_list_label.adjustSize()

        #  Immunities

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].immunity_list, tuple):
            elements_list: list = list(self.bestiary_selector[int(self.enemy_list.currentRow())].immunity_list)

            # This is used to better format element spacing so it doesn't bug out like the FF4 program did.
            left_element_list = elements_list[0::2]
            right_element_list = elements_list[1::2]

            left_column_full_string: str = ""
            right_column_full_string: str = ""
            for element in left_element_list:
                left_column_full_string += f"{element}\n"

            for element in right_element_list:
                right_column_full_string += f"{element}\n"

            self.left_column_elemental_immunities.setText(f"{left_column_full_string}")
            self.right_column_ele_immunities.setText(f"{right_column_full_string}")

            self.left_column_elemental_immunities.adjustSize()
            self.right_column_ele_immunities.adjustSize()
            self.right_column_ele_immunities.show()

        if self.bestiary_selector[int(self.enemy_list.currentRow())].immunity_list is None:
            self.left_column_elemental_immunities.clear()
            self.left_column_elemental_immunities.setText("---")
            self.left_column_elemental_immunities.adjustSize()
            self.right_column_ele_immunities.hide()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].immunity_list, str):
            self.left_column_elemental_immunities.setText(
                f"{self.bestiary_selector[int(self.enemy_list.currentRow())].immunity_list}")
            self.left_column_elemental_immunities.adjustSize()
            self.right_column_ele_immunities.hide()

        # Enemy Weaknesses

        if self.bestiary_selector[int(self.enemy_list.currentRow())].weakness_list is None:
            self.enemy_weaknesses_left_column.setText("---")
            self.enemy_weaknesses_left_column.adjustSize()
            self.enemy_weaknesses_right_column.hide()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].weakness_list, str):
            self.enemy_weaknesses_left_column.setText(
                f"{self.bestiary_selector[int(self.enemy_list.currentRow())].weakness_list}")
            self.enemy_weaknesses_left_column.adjustSize()
            self.enemy_weaknesses_right_column.hide()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].weakness_list, tuple):
            left_side_weaknesses: list = list(
                self.bestiary_selector[int(self.enemy_list.currentRow())].weakness_list[0::2])
            right_side_weaknesses: list = list(
                self.bestiary_selector[int(self.enemy_list.currentRow())].weakness_list[1::2])

            left_column_weakness_string: str = ""
            right_column_weakness_string: str = ""

            for weakness in left_side_weaknesses:
                left_column_weakness_string += f"{weakness}\n"

            for weakness in right_side_weaknesses:
                right_column_weakness_string += f"{weakness}\n"

            self.enemy_weaknesses_left_column.setText(left_column_weakness_string)
            self.enemy_weaknesses_right_column.setText(right_column_weakness_string)
            for weakness in self.weakness_bundle:
                weakness.adjustSize()
                weakness.show()

        # Elemental Absorption
        if self.bestiary_selector[int(self.enemy_list.currentRow())].absorption_list is None:
            self.right_column_absorb_elements_label.hide()
            self.left_column_absorb_elements_label.setText("---")
            self.left_column_absorb_elements_label.adjustSize()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].absorption_list, str):
            self.right_column_absorb_elements_label.hide()
            self.left_column_absorb_elements_label.setText(
                f"{self.bestiary_selector[int(self.enemy_list.currentRow())].absorption_list}")
            self.left_column_absorb_elements_label.adjustSize()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].absorption_list, tuple):
            left_element_absorption_list = self.bestiary_selector[int(self.enemy_list.currentRow())].absorption_list[
                                           0::2]
            right_element_absorption_list = self.bestiary_selector[int(self.enemy_list.currentRow())].absorption_list[
                                            1::2]

            print(left_element_absorption_list)
            print(right_element_absorption_list)

            self.right_column_absorb_elements_label.show()

            left_side_absorption_text: str = ""
            right_side_absorption_text: str = ""

            for element in left_element_absorption_list:
                left_side_absorption_text += f"{element}\n"

            for element in right_element_absorption_list:
                right_side_absorption_text += f"{element}\n"

            self.left_column_absorb_elements_label.setText(left_side_absorption_text)
            self.right_column_absorb_elements_label.setText(right_side_absorption_text)

            for element in self.absorptionbundle:
                element.adjustSize()

        # Enemy Typing

        if self.bestiary_selector[int(self.enemy_list.currentRow())].enemy_type is None:
            self.first_enemy_type_label.setText("---")
            self.first_enemy_type_label.adjustSize()
            self.second_enemy_type_label.hide()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].enemy_type, str):
            self.first_enemy_type_label.setText(
                f"{self.bestiary_selector[int(self.enemy_list.currentRow())].enemy_type}")
            self.first_enemy_type_label.adjustSize()
            self.second_enemy_type_label.hide()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].enemy_type, tuple):
            self.second_enemy_type_label.show()
            self.first_enemy_type_label.setText(
                f"{self.bestiary_selector[int(self.enemy_list.currentRow())].enemy_type[0]}"
            )
            self.second_enemy_type_label.setText(
                f"{self.bestiary_selector[int(self.enemy_list.currentRow())].enemy_type[1]}"
            )
            for enemytype in self.enemy_type_bundle:
                enemytype.adjustSize()

        # Status Immunities

        if self.bestiary_selector[int(self.enemy_list.currentRow())].status_immunities is None:
            self.left_side_status_immunities.setText("---")
            self.left_side_status_immunities.adjustSize()
            self.right_side_status_immunities.hide()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].status_immunities, str):
            self.left_side_status_immunities.setText(
                f"{self.bestiary_selector[int(self.enemy_list.currentRow())].status_immunities}")
            self.left_side_status_immunities.adjustSize()
            self.right_side_status_immunities.hide()

        if isinstance(self.bestiary_selector[int(self.enemy_list.currentRow())].status_immunities, tuple):
            left_side_status_immunities_list = self.bestiary_selector[
                                              int(self.enemy_list.currentRow())].status_immunities[0::2]
            right_side_status_immunities_list = self.bestiary_selector[
                                                    int(self.enemy_list.currentRow())].status_immunities[1::2]

            left_column_statimmune_text: str = ""
            right_column_statimmune_text: str = ""

            for immunestatus in left_side_status_immunities_list:
                left_column_statimmune_text += f"{immunestatus}\n"

            for immunestatus in right_side_status_immunities_list:
                right_column_statimmune_text += f"{immunestatus}\n"

            self.right_side_status_immunities.show()
            self.left_side_status_immunities.setText(f"{left_column_statimmune_text}")
            self.right_side_status_immunities.setText(f"{right_column_statimmune_text}")

            for immunity in self.status_immunity_bundle:
                immunity.adjustSize()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

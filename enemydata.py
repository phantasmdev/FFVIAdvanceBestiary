class Bestiary:
    bestiary_list: list = []

    def __init__(self, name: str, level: int, health: int, mana: int, attack: int, defense: int, evasion: int,
                 magic_power: int, magic_defense: int, magic_evasion: int, gil: int, experience: int,
                 steal_table: str | tuple | None, drop_table: str | tuple | None,
                 immunity_list: tuple | str | None, weakness_list: tuple | str | None,
                 absorption_list: tuple | str | None, enemy_type: str | tuple | None,
                 status_immunities: tuple | str | None):
        self.name = name
        self.level = level
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.evasion = evasion
        self.magic_power = magic_power
        self.magic_defense = magic_defense
        self.magic_evasion = magic_evasion
        self.gil = gil
        self.experience = experience
        self.steal_table = steal_table
        self.drop_table = drop_table
        self.immunity_list = immunity_list
        self.weakness_list = weakness_list
        self.absorption_list = absorption_list
        self.enemy_type = enemy_type
        self.status_immunities = status_immunities

        self.bestiary_list.append(self)


Guard: Bestiary = Bestiary("Guard", 5, 40, 15, 16, 100, 0, 6,
                           140, 0, 48, 48, ("Hi-Potion", "Potion"),
                           "Potion", None, "Poison", None,
                           "Humanoid", None)

SilverLobo: Bestiary = Bestiary("Silver Lobo", 5, 27, 5, 20, 80, 0,
                                3, 120, 0, 30, 37,
                                "Potion", "Potion", None, "Fire",
                                None, None, None)

Megalodoth: Bestiary = Bestiary("Megalodoth", 1, 115, 30, 110, 75, 0,
                                0, 160, 0, 90, 50,
                                ("Hi-Potion", "Potion"), "Hi-Potion", None,
                                "Fire", None, None, "Sleep")

Wererat: Bestiary = Bestiary("Wererat", 4, 24, 0, 13, 100, 0,
                             10, 150, 0, 22, 21,
                             "Potion", "Potion", None, "Fire",
                             "Poison", None, ("Darkness", "Sleep"))

Spritzer: Bestiary = Bestiary("Spritzer", 5, 15, 0, 13, 95, 0,
                              10, 150, 0, 29, 23, "Potion",
                              "Potion", None, ("Fire", "Holy"),
                              "Lightning", "Undead",
                              ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Bandit: Bestiary = Bestiary("Bandit", 5, 35, 0, 19, 90, 0, 10,
                            120, 0, 25, 25, "Potion",
                            "Potion", None, "Poison", None,
                            "Humanoid", None)

LeafBunny: Bestiary = Bestiary("Leaf Bunny", 5, 33, 0, 13, 60, 0,
                               10, 140, 0, 45, 24,
                               "Potion", "Potion", None, ("Fire", "Water"),
                               "Ice", None, None)

Darkwind: Bestiary = Bestiary("Darkwind", 5, 34, 0, 13, 55, 0,
                              10, 140, 0, 41, 28, "Potion",
                              None, None, "Fire", None, None,
                              "Imp")

SandRay: Bestiary = Bestiary("Sand Ray", 6, 67, 10, 20, 110, 0,
                             10, 145, 0, 54, 41,
                             "Antidote", "Antidote", None,
                             ("Ice", "Water"), None, None, None)

Alacran: Bestiary = Bestiary("Alacran", 6, 87, 15, 20, 80, 0,
                             10, 135, 0, 94, 37, "Potion",
                             "Potion", None, ("Ice", "Water"), None,
                             None, None)

Foper: Bestiary = Bestiary("Foper", 7, 119, 10, 13, 100, 0,
                           10, 155, 0, 80, 53, "Potion",
                           "Potion", None, "Fire", None,
                           None, None)

Hornet: Bestiary = Bestiary("Hornet", 6, 92, 0, 16, 100, 0,
                            10, 150, 0, 64, 48, "Potion",
                            None, None, "Fire", None, None,
                            "Imp")

Urok: Bestiary = Bestiary("Urok", 7, 122, 0, 13, 45, 0, 10,
                          155, 0, 120, 71, ("Remedy", "Potion"),
                          None, None, "Fire", None, None,
                          None)

Belmodar: Bestiary = Bestiary("Belmodar", 8, 232, 100, 25, 100, 0,
                              10, 155, 0, 186, 246,
                              ("Mythril Claws", "Potion"), "Hi-Potion", None,
                              None, "Lightning", None,
                              ("Petrify", "Slow", "Stop"))

Unseelie: Bestiary = Bestiary("Unseelie", 8, 132, 100, 15, 100, 0,
                              10, 150, 0, 256, 53,
                              ("Buckler", "Potion"), None, None, "Poison",
                              None, "Humanoid", None)

Mu: Bestiary = Bestiary("Mu", 7, 119, 100, 11, 100, 0, 10,
                        155, 0, 80, 59, ("Potion", "Antidote"),
                        None, None, None, None, None,
                        ("Darkness", "Silence", "Berserk"))

Zaghrem: Bestiary = Bestiary("Zaghrem", 9, 137, 100, 14, 100, 0,
                             10, 70, 0, 84, 79, "Bandana",
                             "Potion", None, "Ice", "Poison",
                             "Humanoid", "Poison")

Trillium: Bestiary = Bestiary("Trillium", 9, 147, 100, 13, 102, 0,
                              10, 170, 0, 134, 97,
                              ("Remedy", "Potion"), None, None, "Fire",
                              "Water", None, "Imp")

Gorgias: Bestiary = Bestiary("Gorgias", 10, 270, 100, 28, 100, 0,
                             10, 135, 0, 102, 163,
                             ("Hi-Potion", "Potion"), "Gold Needle", None,
                             "Fire", None, None, None)

Cirpius: Bestiary = Bestiary("Cirpius", 10, 134, 100, 13, 80, 0,
                             10, 110, 0, 102, 82,
                             ("Potion", "Antidote"), None, None, None,
                             None, None, "Imp")

LesserLopros: Bestiary = Bestiary("Lesser Lopros", 12, 380, 70, 25, 65,
                                  0, 10, 180, 0, 325, 464,
                                  ("Main Gauche", "Mythril Knife"), "Hi-Potion", None,
                                  "Fire", None, None, "Imp")

Nautiloid: Bestiary = Bestiary("Nautiloid", 11, 236, 100, 18, 100, 0,
                               10, 150, 0, 173, 216,
                               ("Hi-Potion", "Potion"), "Eye Drops", None,
                               ("Fire", "Lightning"), "Water", None,
                               "Imp")

Exocite: Bestiary = Bestiary("Exocite", 11, 196, 100, 19, 100, 0,
                             10, 150, 0, 153, 162,
                             ("Mythril Claws", "Potion"), "Potion", None,
                             ("Fire", "Lightning"), "Water", None,
                             ("Darkness", "Imp"))

HeavyArmor: Bestiary = Bestiary("Heavy Armor", 13, 495, 150, 53, 150, 0,
                                11, 110, 0, 195, 80,
                                ("Iron Helm", "Potion"), None, None,
                                ("Lightning", "Water"), None, None,
                                ("Poison", "Imp", "Petrify"))

Commander: Bestiary = Bestiary("Commander", 10, 102, 50, 13, 100, 0,
                               10, 150, 0, 153, 85,
                               "Potion", None, None, "Poison",
                               None, "Humanoid", None)

VectorHound: Bestiary = Bestiary("Vector Hound", 11, 166, 10, 14, 80, 0,
                                 10, 150, 0, 83, 128,
                                 "Potion", None, None, "Fire",
                                 None, None, None)

Cartagra: Bestiary = Bestiary("Cartagra", 12, 150, 20, 11, 90, 0,
                              10, 150, 0, 135, 105,
                              ("Potion", "Antidote"), None, None, None,
                              None, None, "Imp")

Acrophies: Bestiary = Bestiary("Acrophies", 11, 145, 10, 13, 50, 0,
                               10, 150, 0, 115, 90,
                               ("Potion", "Eye Drops"), None, None,
                               "Lightning", None, None, "Imp")

GoldBear: Bestiary = Bestiary("Gold Bear", 13, 275, 0, 13, 40, 0,
                              10, 140, 0, 185, 160,
                              ("Hi-Potion", "Potion"), "Hi-Potion", None,
                              None, None, None, None)

Valeor: Bestiary = Bestiary("Valeor", 11, 180, 25, 13, 55, 0,
                            10, 135, 0, 112, 117,
                            "Potion", None, None, "Poison",
                            None, "Humanoid", None)

WildRat: Bestiary = Bestiary("Wild Rat", 12, 160, 10, 10, 85, 0,
                             10, 100, 0, 135, 135,
                             "Potion", None, None, "Fire",
                             "Poison", None, None)

StrayCat: Bestiary = Bestiary("Stray Cat", 10, 156, 30, 9, 10, 0,
                              10, 135, 0, 90, 42,
                              "Hi-Potion", "Potion", None, None,
                              None, None, None)

Aepyornis: Bestiary = Bestiary("Aepyornis", 11, 290, 30, 12, 80, 0,
                               10, 150, 0, 135, 108,
                               ("Hi-Potion", "Eye Drops"), "Hi-Potion", None,
                               "Fire", "None", None, "Imp")

Nettlehopper: Bestiary = Bestiary("Nettlehopper", 11, 243, 80, 10, 50, 0,
                                  10, 155, 0, 145, 89,
                                  "Antidote", "Hi-Potion", None,
                                  ("Fire", "Wind"), None, None,
                                  ("Imp", "Sleep"))

Chippirabbit: Bestiary = Bestiary("Chippirabbit", 10, 135, 40, 9, 70, 0,
                                  10, 140, 0, 110, 53,
                                  "Hi-Potion", "Potion", None, "Water",
                                  None, None, None)

Captain: Bestiary = Bestiary("Captain", 12, 456, 20, 18, 5, 0,
                             10, 110, 0, 50, 0, None,
                             ("Phoenix Down", "Black Belt"), None, None,
                             None, "Humanoid", None)

ImperialSoldier: Bestiary = Bestiary("Imperial Soldier", 11, 100, 15, 12, 80,
                                     0, 10, 150, 0, 48, 0,
                                     ("Potion", "Hi-Potion"), "Potion", None,
                                     "Poison", None, "Humanoid",
                                     ("Darkness", "Sleep"))

Templar: Bestiary = Bestiary("Templar", 11, 205, 50, 16, 50, 0,
                             10, 150, 0, 96, 0,
                             "Potion", "Hi-Potion", None, "Poison",
                             None, "Humanoid", None)

Satellite: Bestiary = Bestiary("Satellite", 14, 1800, 250, 20, 120, 0,
                               13, 150, 0, 0, 0,
                               "X-Potion", "Green Beret", None,
                               ("Lightning", "Water"), None, None,
                               ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence",
                                "Berserk", "Confusion", "Sleep"))

Ghost: Bestiary = Bestiary("Ghost", 10, 226, 70, 1, 105, 0, 1,
                           150, 0, 75, 48, "Potion", "Potion",
                           None, ("Fire", "Holy"), "Poison", "Undead",
                           ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Poplium: Bestiary = Bestiary("Poplium", 11, 145, 25, 13, 55, 0,
                             10, 150, 0, 55, 55,
                             "Hi-Potion", "Potion",
                             None, ("Fire", "Holy"), "Poison", "Undead",
                             ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Cloud: Bestiary = Bestiary("Cloud", 12, 120, 100, 5, 110, 0,
                           7, 150, 0, 101, 35,
                           "Hi-Potion", "Potion", None, "Holy",
                           None, "Humanoid", ("Imp", "Death"))

AngelWhisper: Bestiary = Bestiary("Angel Whisper", 12, 230, 90, 12, 95,
                                  0, 10, 150, 0, 125, 42,
                                  "Hi-Pottion", "Gold Needle", None,
                                  ("Fire", "Holy"), "Poison", "Undead",
                                  ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Oversoul: Bestiary = Bestiary("Oversoul", 13, 390, 190, 12, 55, 0,
                              7, 150, 0, 228, 65,
                              "Hi-Potion", ("Holy Water", "Green Cherry"), None,
                              ("Fire", "Holy"), "Poison", "Undead",
                              ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Bomb: Bestiary = Bestiary("Bomb", 8, 160, 50, 10, 90, 0, 1,
                          150, 0, 80, 35,
                          ("Hi-Potion", "Potion"), "Hi-Potion", None,
                          ("Ice", "Water"), "Fire", None,
                          ("Darkness", "Poison", "Imp", "Petrify"))

LivingDead: Bestiary = Bestiary("Living Dead", 12, 200, 84, 10, 100, 0,
                                10, 150, 0, 135, 54, None,
                                "Hi-Potion", None, ("Fire", "Holy"),
                                "Poison", ("Undead", "Humanoid"),
                                ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Apparition: Bestiary = Bestiary("Apparition", 19, 1500, 10000, 15, 120, 0,
                                8, 180, 0, 0, 0, None,
                                "Hyper Wrist", None, ("Fire", "Holy"),
                                "Poison", "Undead",
                                ("Darkness", "Imp", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Siegfried: Bestiary = Bestiary("Siegfried", 7, 100, 5, 1, 50, 0,
                               10, 150, 0, 1, 0, None,
                               "Green Cherry", None, None, None,
                               None, ("Darkness", "Poison", "Imp", "Petrify", "Death",
                                      "Silence", "Berserk", "Confusion", "Sleep"))

OpinicusFish: Bestiary = Bestiary("Opinicus Fish", 9, 10, 60, 13, 100, 0,
                                  10, 150, 0, 0, 0, None,
                                  "Potion", None, "Lightning", None,
                                  None, ("Poison", "Imp", "Petrify", "Death"))

Anguiform: Bestiary = Bestiary("Anguiform", 13, 315, 150, 14, 80, 0,
                               6, 150, 0, 358, 96,
                               "Hi-Potion", "Phoenix Down", None,
                               "Lightning", "Water", None, "Imp")

Aspiran: Bestiary = Bestiary("Aspiran", 12, 220, 330, 2, 100, 0,
                             2, 150, 0, 115, 48, "Potion",
                             "X-Potion", None, "Fire", "Water",
                             None, ("Darkness", "Imp", "Silence", "Confusion", "Sleep"))

Actinian: Bestiary = Bestiary("Actinian", 12, 230, 98, 13, 100, 0,
                              10, 150, 0, 125, 57,
                              "Hi-Potion", None, None, ("Fire", "Lightning"),
                              "Water", None, ("Imp", "Silence", "Berserk",
                                              "Confusion", "Sleep"))

Fidor: Bestiary = Bestiary("Fidor", 13, 355, 80, 25, 55, 0,
                           10, 170, 0, 180, 160,
                           ("Hi-Potion", "Phoenix Down"), None,
                           None, "Fire", None, None,
                           ("Petrify", "Sleep"))

Corporal: Bestiary = Bestiary("Corporal", 13, 255, 60, 15, 100, 0,
                              10, 125, 0, 96, 90,
                              ("Mythril Sword", "Potion"), None, None,
                              "Poison", None, "Humanoid", None)

HuntingHound: Bestiary = Bestiary("Hunting Hound", 13, 285, 50, 16, 75, 0,
                                  10, 140, 0, 55, 115, "Hi-Potion",
                                  None, None, "Fire", None,
                                  None, None)

FossilDragon: Bestiary = Bestiary("Fossil Dragon", 20, 1399, 219, 25, 100,
                                  0, 3, 165, 0, 1870, 380,
                                  ("Remedy", "Holy Water"), None, None,
                                  ("Fire", "Ice", "Holy", "Water"), "Poison",
                                  "Undead",
                                  ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Vulture: Bestiary = Bestiary("Vulture", 15, 412, 60, 13, 100, 0,
                             10, 155, 0, 486, 160,
                             ("Phoenix Down", "Hi-Potion"), "Phoenix Down", None,
                             "Wind", None, None, "Imp")

IronFist: Bestiary = Bestiary("Iron Fist", 15, 333, 65, 13, 75, 0,
                              10, 145, 0, 249, 144,
                              ("Twist Headband", "Potion"), "Mythril Knife", None,
                              None, "Poison", "Humanoid", None)

Bloodfang: Bestiary = Bestiary("Bloodfang", 14, 325, 20, 13, 95, 0,
                               10, 150, 0, 185, 135,
                               "Potion", "Dried Meat", None, None,
                               None, None, None)

RockWasp: Bestiary = Bestiary("Rock Wasp", 15, 290, 100, 14, 105, 0,
                              10, 165, 0, 168, 128,
                              ("Potion", "Gold Needle"), "Gold Needle", None,
                              ("Fire", "Wind"), None, None,
                              ("Imp", "Sleep"))

Paraladia: Bestiary = Bestiary("Paraladia", 15, 492, 100, 13, 125, 0,
                               10, 125, 0, 365, 219,
                               ("Remedy", "Hi-Potion"), None, None, "Fire",
                               None, None, ("Darkness", "Imp", "Berserk",
                                            "Confusion", "Sleep"))

Harvester: Bestiary = Bestiary("Harvester", 16, 428, 85, 13, 105, 0,
                               10, 150, 0, 314, 291,
                               ("Dragoon Boots", "Silver Spectacles"), "Barrier Ring",
                               None, "Poison", None, "Humanoid",
                               ("Imp", "Slow", "Stop"))

HillGigas: Bestiary = Bestiary("Hill Gigas", 16, 1200, 60, 18, 125, 0,
                               5, 115, 0, 600, 550,
                               "Gigas Glove", None, None, "Poison",
                               "Earth", "Humanoid", None)

Gobbledygook: Bestiary = Bestiary("Gobbledygook", 15, 350, 20, 13, 85, 0,
                                  10, 155, 0, 126, 104,
                                  ("Phoenix Down", "Eye Drops"), None, None,
                                  "Poison", None, "Humanoid", None)

VeilDancer: Bestiary = Bestiary("Veil Dancer", 15, 392, 120, 13, 115, 0,
                                10, 145, 0, 296, 224,
                                ("Thief's Knife", "Hi-Potion"), None, None,
                                "Poison", None, "Humanoid",
                                ("Poison", "Imp", "Berserk", "Confusion"))

Stunner: Bestiary = Bestiary("Stunner", 16, 299, 20, 13, 110, 0,
                             10, 160, 0, 156, 108,
                             "Hi-Potion", None, None, "Fire",
                             "Poison", None, None)

Goetia: Bestiary = Bestiary("Goetia", 16, 499, 40, 20, 120, 0,
                            10, 190, 0, 235, 145,
                            ("Antidote", "Hi-Potion"), "Hi-Potion", None,
                            "Ice", "Poison", None, None)

LitworChicken: Bestiary = Bestiary("Litwor Chicken", 18, 545, 155, 11, 150,
                                   0, 3, 150, 0, 279, 190,
                                   ("Sleeping Bag", "Potion"), None, None,
                                   "Ice", None, None,
                                   ("Poison", "Imp", "Petrify", "Death", "Silence", "Sleep"))

Joker: Bestiary = Bestiary("Joker", 17, 467, 90, 13, 125, 0,
                           10, 150, 0, 320, 194,
                           ("Green Beret", "Potion"), "Mythril Rod", None,
                           ("Lightning", "Poison"), None, "Humanoid",
                           "Imp")

Don: Bestiary = Bestiary("Don", 17, 620, 10, 14, 135, 0,
                         10, 145, 0, 345, 255,
                         ("Tiger Mask", "Potion"), "Hi-Potion", None,
                         None, None, None, "Petrify")

Wyvern: Bestiary = Bestiary("Wyvern", 18, 892, 95, 15, 140, 0,
                            10, 155, 0, 434, 484,
                            ("Dragoon Boots", "Potion"), None, None,
                            "Ice", None, None, "Imp")

Grasswyrm: Bestiary = Bestiary("Grasswyrm", 17, 480, 20, 13, 115,
                               0, 10, 150, 0, 234, 278,
                               "Antidote", "Echo Screen", None,
                               ("Fire", "Wind"), None, None,
                               ("Darkness", "Imp", "Silence", "Sleep"))

Grenade: Bestiary = Bestiary("Grenade", 17, 3000, 500, 13, 0, 0,
                             10, 150, 0, 500, 190,
                             "Flame Scroll", None, None,
                             ("Ice", "Water"), "Fire", None,
                             ("Imp", "Petrify"))

Bug: Bestiary = Bestiary("Bug", 16, 310, 20, 13, 120, 0,
                         10, 150, 0, 210, 165,
                         ("Hi-Potion", "Gold Needle"), None, None,
                         ("Ice", "Water"), None, None,
                         ("Darkness", "Imp", "Silence", "Sleep"))

OnionKnight: Bestiary = Bestiary("Onion Knight", 18, 250, 50, 13, 200, 0,
                                 10, 150, 0, 100, 115,
                                 "Potion", None, None,
                                 ("Lightning", "Water"), None, "Humanoid",
                                 ("Poison", "Imp", "Petrify"))

Sergeant: Bestiary = Bestiary("Sergeant", 18, 580, 35, 13, 210, 0,
                              10, 145, 0, 273, 252,
                              ("Mythril Vest", "Tent"), "Tent", None,
                              ("Lightning", "Water"), None, "Humanoid",
                              ("Poison", "Imp", "Petrify"))

Belzecue: Bestiary = Bestiary("Belzecue", 190, 615, 45, 13, 220, 0,
                              10, 140, 0, 343, 228,
                              ("Phoenix Down", "Potion"), None, None,
                              ("Lightning", "Water"), None, None,
                              ("Poison", "Imp", "Petrify"))

ProtoArmor: Bestiary = Bestiary("Proto Armor", 19, 670, 125, 12, 230, 0,
                                7, 110, 0, 296, 499,
                                ("Mythril Mail", "Hi-Potion"), "Bioblaster", None,
                                "Lightning", None, None,
                                ("Poison", "Imp", "Petrify"))

Trapper: Bestiary = Bestiary("Trapper", 19, 555, 80, 13, 180, 0,
                             10, 135, 0, 200, 235,
                             "Auto Crossbow", None, None,
                             ("Lightning", "Water"), None, None,
                             ("Poison", "Imp", "Petrify"))

Flan: Bestiary = Bestiary("Flan", 19, 255, 110, 13, 13, 0, 10,
                          100, 0, 120, 160,
                          ("Magicite Shard", "Potion"), None,
                          ("Poison", "Wind", "Holy", "Earth", "Water"), "Fire",
                          None, None, ("Darkness", "Poison", "Imp", "Petrify"))

General: Bestiary = Bestiary("General", 19, 650, 30, 13, 155, 0,
                             10, 105, 0, 308, 232,
                             ("Mythril Shield", "Potion"), "Green Cherry", None,
                             "Poison", None, "Humanoid", None)

Destroyer: Bestiary = Bestiary("Destroyer", 19, 800, 35, 13, 200, 0,
                               10, 100, 0, 400, 592,
                               "Flash", None, None, None,
                               "Lightning", None, ("Petrify", "Death"))

Lenergia: Bestiary = Bestiary("Lenergia", 19, 470, 63, 13, 170, 0,
                              8, 120, 0, 250, 438,
                              ("Hi-Potion", "Green Cherry"), None, None,
                              None, None, None, "Imp")

MagnaRoaderPurple: Bestiary = Bestiary("Magna Roader", 19, 420, 100, 12, 25,
                                       0, 1, 140, 0, 277, 232,
                                       ("Shuriken", "Lightning Scroll"), "Water Scroll", None,
                                       "Fire", "Ice", None,
                                       ("Imp", "Petrify", "Death", "Silence", "Confusion", "Sleep"))

MagnaRoaderRed: Bestiary = Bestiary("Magna Roader", 18, 250, 100, 10, 20,
                                    0, 1, 140, 0, 300, 198,
                                    ("Shuriken", "Lightning Scroll"), "Flame Scroll",
                                    None, "Ice", None, None,
                                    ("Imp", "Petrify", "Death", "Berserk", "Sleep"))

Chaser: Bestiary = Bestiary("Chaser", 19, 1202, 140, 13, 200, 0,
                            8, 150, 0, 380, 691,
                            "Bioblaster", None, None,
                            ("Lightning", "Water"), None, None,
                            ("Poison", "Imp", "Petrify"))

Outcast: Bestiary = Bestiary("Outcast", 21, 1100, 50, 18, 110, 0,
                             12, 150, 0, 442, 740,
                             "Amulet", "Holy Water", None,
                             ("Holy", "Water"), ("Fire", "Poison"), "Undead",
                             ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Provoker: Bestiary = Bestiary("Provoker", 20, 781, 60, 17, 110, 0,
                              10, 150, 0, 300, 415,
                              ("Hi-Potion", "Holy Water"), "Holy Water", None,
                              ("Ice", "Holy"), ("Fire", "Poison"), "Undead",
                              ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep",
                               "Slow", "Stop"))

ZombieDragon: Bestiary = Bestiary("Zombie Dragon", 21, 1991, 160, 29, 150,
                                  0, 10, 100, 0, 309, 1072,
                                  ("Hi-Potion", "Phoenix Down"), "Phoenix Down", None,
                                  ("Fire", "Holy"), "Poison", "Undead",
                                  ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Antares: Bestiary = Bestiary("Antares", 20, 480, 15, 20, 120,
                             0, 10, 130, 0, 270, 290,
                             ("Hi-Potion", "Antidote"), "Antidote", None,
                             "Ice", "Fire", None,
                             ("Darkness", "Imp", "Silence", "Berserk", "Confusion", "Sleep"))

Lich: Bestiary = Bestiary("Lich", 20, 590, 90, 1, 50, 0,
                          10, 190, 0, 350, 374,
                          ("Poison Rod", "Green Cherry"), "Green Cherry", None,
                          "Holy", ("Fire", "Poison"), "Undead",
                          ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep",
                           "Slow", "Stop"))

ImperialElite: Bestiary = Bestiary("Imperial Elite", 21, 700, 20, 13, 100,
                                   0, 10, 140, 0, 0, 200,
                                   "Potion", "Magicite Shard", None,
                                   "Poison", None, "Humanoid",
                                   ("Darkness", "Poison", "Petrify", "Death", "Silence", "Berserk",
                                    "Confusion", "Sleep", "Slow", "Stop"))

MegaArmor: Bestiary = Bestiary("Mega Armor", 21, 1000, 50, 19, 120, 0,
                               10, 100, 0, 0, 350,
                               "Hi-Potion", None, None,
                               ("Lightning", "Water"), None, None,
                               ("Poison", "Imp", "Petrify"))

Briareus: Bestiary = Bestiary("Briareus", 22, 750, 100, 17, 110, 0,
                              10, 120, 0, 458, 465,
                              "Gaia Gear", "Hi-Potion", None, None,
                              None, None, ("Poison", "Death"))

Devourer: Bestiary = Bestiary("Devourer", 21, 420, 100, 10, 100, 0,
                              10, 140, 0, 280, 214,
                              ("Remedy", "Hi-Potion"), None, None,
                              "Lightning", None, None,
                              ("Imp", "Death", "Confusion"))

Chimera: Bestiary = Bestiary("Chimera", 22, 2237, 100, 25, 100, 0,
                             10, 110, 0, 760, 1144,
                             "Hyper Wrist", "Golden Armor", None, None,
                             None, None,
                             ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence",
                              "Confusion", "Sleep", "Slow", "Stop"))

# Absorption list maxes out at 8 elements

Intangir: Bestiary = Bestiary("Intangir", 26, 32000, 16000, 25, 150, 50,
                              10, 150, 0, 0, 0,
                              "Magicite Shard", "Antidote", None, None,
                              ("Fire", "Ice", "Lighting", "Poison", "Wind", "Holy", "Earth", "Water"),
                              None, ("Darkness", "Poison", "Imp", "Petrify", "Death",
                                     "Silence", "Berserk", "Confusion", "Sleep"))

Balloon: Bestiary = Bestiary("Balloon", 22, 555, 80, 11, 20, 0,
                             10, 130, 0, 300, 369,
                             "Phoenix Down", None, None, ("Ice", "Water"),
                             "Fire", None, ("Imp", "Sleep"))

Bonnacon: Bestiary = Bestiary("Bonnacon", 23, 505, 20, 12, 50, 0,
                              10, 50, 0, 270, 232,
                              "Hi-Potion", None, None, "Fire",
                              None, None, ("Darkness", "Imp", "Silence",
                                           "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

LandGrillon: Bestiary = Bestiary("Land Grillon", 23, 977, 80, 15, 115,
                                 0, 10, 155, 0, 410, 292,
                                 "Echo Screen", "Smoke Bomb", None,
                                 ("Fire", "Wind"), None, None,
                                 ("Darkness", "Imp", "Silence", "Confusion", "Sleep"))

Adamankary: Bestiary = Bestiary("Adamankary", 24, 1305, 50, 22, 225,
                                0, 10, 45, 0, 189, 1450,
                                "Golden Shield", None, None, None,
                                None, None, ("Petrify", "Death", "Confusion"))

Mandrake: Bestiary = Bestiary("Mandrake", 23, 1150, 104, 16, 115, 0,
                              10, 125, 0, 450, 378,
                              "Hi-Potion", "Remedy", None, "Fire",
                              "Water", None,
                              ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                               "Sleep"))

Venobennu: Bestiary = Bestiary("Venobennu", 24, 860, 82, 16, 125, 0,
                               10, 150, 0, 525, 485,
                               "Antidote", "Phoenix Down", None, None,
                               None, None, ("Imp", "Petrify", "Silence",
                                            "Sleep"))

SkyArmor: Bestiary = Bestiary("Sky Armor", 24, 900, 170, 16, 150, 0,
                              7, 120, 0, 400, 350, "Ether",
                              None, ("Lightning", "Wind"), None, None,
                              None, ("Poison", "Imp", "Petrify"))

Spitfire: Bestiary = Bestiary("Spitfire", 25, 1400, 180, 17, 155, 0,
                              4, 130, 0, 300, 550,
                              ("Elixir", "Ether"), "Ether", None,
                              ("Lightning", "Wind"), None, None,
                              ("Poison", "Imp", "Petrify", "Slow", "Stop"))

Brainpan: Bestiary = Bestiary("Brainpan", 25, 1300, 1000, 24, 120, 0,
                              10, 110, 0, 600, 550,
                              "Earring", None, None,
                              ("Fire", "Lighting", "Holy"), "Poison", "Undead",
                              ("Darkness", "Poison", "Imp", "Silence", "Berserk", "Sleep"))

Misfit: Bestiary = Bestiary("Misfit", 26, 1750, 140, 26, 105, 0,
                            10, 155, 0, 786, 750,
                            "Alarm Earring", None, None, ("Fire", "Holy"),
                            "Poison", "Undead", ("Darkness", "Poison", "Imp",
                                                 "Silence", "Berserk", "Sleep"))

Apocrypha: Bestiary = Bestiary("Apocrypha", 26, 1900, 195, 18, 80, 0,
                               10, 150, 0, 525, 1200,
                               "Angel Ring", None, None, ("Lightning",
                                                          "Holy", "Water"), None, None,
                               ("Poison", "Imp", "Berserk", "Confusion"))

Dragon: Bestiary = Bestiary("Dragon", 29, 7000, 850, 45, 130, 40,
                            10, 110, 0, 0, 2931,
                            ("Genji Glove", "Hi-Potion"), None, None,
                            "Lightning", None, None,
                            ("Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion"))

PlatinumDragon: Bestiary = Bestiary("Platinum Dragon", 26, 2802, 200, 35, 150,
                                    0, 10, 115, 0, 1300, 895,
                                    "Dragoon Boots", None, None, None,
                                    None, None, "Imp")

Behemoth: Bestiary = Bestiary("Behemoth", 28, 5800, 180, 25, 100, 0,
                              7, 135, 0, 0, 2055,
                              "Hermes Sandals", "X-Potion", None, "Ice",
                              None, None, ("Darkness", "Poison", "Imp",
                                           "Silence", "Confusion", "Sleep", "Slow", "Stop"))

Ninja: Bestiary = Bestiary("Ninja", 27, 1650, 130, 22, 135, 50,
                           5, 140, 0, 520, 694,
                           "Angel Wings", "Fuma Shuriken", None,
                           ("Lightning", "Holy"), "Poison", "Humanoid",
                           ("Darkness", "Petrify", "Confusion", "Sleep", "Slow", "Stop"))

Naude: Bestiary = Bestiary("Naude", 24, 3000, 195, 11, 115, 0,
                           10, 145, 0, 0, 0, None,
                           None, ("Poison", "Wind", "Earth", "Water"),
                           ("Fire", "Lightning", "Holy"), "Ice", "Humanoid",
                           ("Death", "Berserk", "Confusion", "Slow", "Stop"))

Fafnir: Bestiary = Bestiary("Fafnir", 26, 1112, 130, 13, 110,
                            0, 10, 150, 0, 456, 459,
                            "Antidote", None, None, "Ice", None,
                            None, None)

KillerMantis: Bestiary = Bestiary("Killer Mantis", 26, 1412, 110, 16, 115,
                                  0, 10, 140, 0, 756, 559,
                                  "Venom Claws", None, None, "Fire",
                                  None, None, ("Imp", "Death", "Confusion",
                                               "Sleep"))

Peeper: Bestiary = Bestiary("Peeper", 23, 1, 19, 7, 5, 0,
                            10, 5, 0, 0, 2, "Elixir",
                            None, None, ("Ice", "Water"), None,
                            None, "Poison")

Murussu: Bestiary = Bestiary("Murussu", 26, 1111, 60, 13, 140, 0,
                             10, 80, 0, 356, 321,
                             "Hi-Potion", "Remedy", None, "Lightning",
                             None, None, ("Petrify", "Death", "Silence"))

Gigantoad: Bestiary = Bestiary("Gigantoad", 26, 458, 20, 11, 100, 0,
                               10, 130, 0, 340, 235,
                               None, "Sleeping Bag", None, "Ice",
                               None, None, ("Poison", "Death"))

LandRay: Bestiary = Bestiary("Land Ray", 23, 1, 18, 6, 5, 0,
                             10, 5, 0, 0, 1,
                             "Megalixir", None, None, "Water",
                             None, None, ("Darkness", "Imp",
                                          "Petrify", "Sleep"))

LunaWolf: Bestiary = Bestiary("Luna Wolf", 26, 582, 25, 13, 155, 0,
                              10, 145, 0, 247, 308,
                              "Hi-Potion", None, None, None,
                              None, None, ("Death", "Silence",
                                           "Sleep"))
BlackDragon: Bestiary = Bestiary("Black Dragon", 26, 4000, 600, 14, 102,
                                 0, 10, 20, 0, 502, 780,
                                 "Holy Water", "Tent", None,
                                 ("Fire", "Holy"), "Poison", "Undead",
                                 ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk",
                                  "Sleep"))

Rukh: Bestiary = Bestiary("Rukh", 26, 850, 100, 12, 105, 0,
                          10, 120, 0, 596, 249,
                          None, "Echo Screen", None, "Ice",
                          None, None, ("Imp", "Petrify", "Silence",
                                       "Sleep"))

Zokka: Bestiary = Bestiary("Zokka", 26, 305, 35, 5, 150, 0,
                           5, 80, 0, 400, 267, "Hi-Potion",
                           "Teleport Stone", None, "Water", None,
                           None, ("Darkness", "Imp", "Petrify", "Silence", "Sleep"))

Nightwalker: Bestiary = Bestiary("Nightwalker", 26, 265, 190, 9, 140, 0,
                                 6, 115, 0, 491, 258,
                                 "X-Potion", None, None, ("Fire", "Holy"),
                                 "Poison", "Undead", ("Darkness", "Poison",
                                                      "Imp", "Petrify", "Silence", "Berserk"))

Scorpion: Bestiary = Bestiary("Scorpion", 26, 290, 19, 10, 5, 0,
                              9, 215, 0, 336, 199,
                              "Potion", "Potion", None, None,
                              None, None, ("Darkness", "Imp",
                                           "Petrify", "Silence", "Berserk", "Confusion", "Sleep"))

DeltaBeetle: Bestiary = Bestiary("Delta Beetle", 26, 612, 80, 11, 220, 0,
                                 10, 5, 0, 211, 288,
                                 "Potion", "Sleeping Bag", None, "Fire",
                                 None, None, ("Darkness", "Poison", "Imp",
                                              "Berserk", "Confusion"))

VampireThorn: Bestiary = Bestiary("Vampire Thorn", 26, 12, 400, 13, 254,
                                  0, 10, 254, 0, 896, 510,
                                  "Echo Screen", "Smoke Bomb", None, "Fire",
                                  "Water", "Undead", ("Darkness", "Poison",
                                                      "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Lizard: Bestiary = Bestiary("Lizard", 26, 1280, 70, 14, 102, 0,
                            10, 153, 0, 356, 297,
                            "Blood Sword", "Gold Needle", None, "Ice",
                            "Poison", None, ("Petrify", "Silence"))

Devoahan: Bestiary = Bestiary("Devoahan", 26, 2252, 218, 15, 100, 0,
                              10, 150, 0, 458, 562,
                              ("Diamond Vest", "Ether"), None, None,
                              ("Fire", "Water"), None, None,
                              ("Petrify", "Sleep"))

Sandhorse: Bestiary = Bestiary("Sandhorse", 27, 1025, 100, 15, 135, 0,
                               9, 155, 0, 726, 475,
                               "Hi-Potion", None, None, ("Ice", "Water"),
                               None, None, ("Darkness", "Imp", "Petrify",
                                            "Death", "Silence", "Berserk", "Confusion", "Sleep"))

Cancer: Bestiary = Bestiary("Cancer", 26, 952, 100, 15, 110, 0,
                            10, 145, 0, 576, 360,
                            "Potion", None, None, ("Ice", "Lightning",
                                                   "Water"), None, None,
                            ("Darkness", "Imp", "Petrify", "Silence", "Berserk", "Confusiuon", "Sleep"))

Oceanus: Bestiary = Bestiary("Oceanus", 27, 1700, 100, 15, 125, 0,
                             9, 140, 0, 971, 612,
                             "Gaia Gear", "Antidote", None, "Lightning",
                             None, None, ("Darkness", "Poison", "Imp", "Death",
                                          "Berserk", "Sleep"))

DesertHare: Bestiary = Bestiary("Desert Hare", 26, 75, 200, 7, 100, 0,
                                30, 100, 0, 0, 0, "Remedy",
                                "Hi-Potion", None, "Water", None,
                                None, ("Silence", "Berserk"))

Humpty: Bestiary = Bestiary("Humpty", 27, 800, 100, 8, 145, 0,
                            10, 135, 0, 326, 421,
                            "Green Cherry", None, None, ("Fire", "Holy"),
                            "Poison", "Undead", ("Darkness", "Poison",
                                                 "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Cruller: Bestiary = Bestiary("Cruller", 28, 1334, 100, 11, 110, 100,
                             4, 70, 0, 797, 419, "Potion",
                             None, None, ("Fire", "Holy"), "Poison",
                             "Undead", ("Darkness", "Poison", "Imp", "Petrify", "Silence",
                                        "Berserk", "Sleep", "Slow", "Stop"))

Dropper: Bestiary = Bestiary("Dropper", 27, 1000, 80, 6, 100, 0,
                             10, 150, 0, 427, 398,
                             "Ether", "Ether", None, ("Lightning", "Water"),
                             None, None, ("Darkness", "Poison", "Imp",
                                          "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep"))

NeckHunter: Bestiary = Bestiary("Neck Hunter", 28, 1334, 150, 5, 102, 0,
                                10, 153, 0, 1330, 588,
                                "Black Cowl", "Peace Ring", None, "Poison",
                                None, "Humanoid", "Imp")

Dante: Bestiary = Bestiary("Dante", 28, 1945, 200, 17, 105, 0,
                           10, 150, 0, 712, 1150,
                           "Diamond Helm", "Golden Shield", None, "Poison",
                           None, ("Undead", "Humanoid"),
                           ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Bogy: Bestiary = Bestiary("Bogy", 29, 1318, 100, 15, 102, 0,
                          10, 153, 0, 1200, 532,
                          "Hi-Potion", None, None, None, None,
                          None, "Petrify")

Marchosias: Bestiary = Bestiary("Marchosias", 29, 1418, 100, 19, 102, 0,
                                10, 153, 0, 909, 449,
                                "Phoenix Down", None, None, "Wind",
                                None, None, ("Imp", "Petrify", "Death",
                                             "Confusion", "Sleep", "Slow", "Stop"))

Deepeye: Bestiary = Bestiary("Deepeye", 28, 1334, 100, 14, 100, 0,
                             10, 150, 0, 485, 385,
                             "Eye Drops", None, None, "Fire",
                             None, None, ("Imp", "Sleep"))

Mousse: Bestiary = Bestiary("Mousse", 28, 900, 100, 11, 110, 0,
                            10, 105, 0, 287, 189,
                            "Magicite Shard", None, ("Poison", "Wind",
                                                     "Holy", "Earth", "Water"), None, None,
                            None, ("Darkness", "Poison", "Imp", "Petrify", "Death",
                                   "Berserk", "Confusion", "Sleep"))

Borghese: Bestiary = Bestiary("Borghese", 30, 1584, 250, 45, 105, 0,
                              10, 140, 0, 716, 510,
                              "Amulet", ("Amulet", "Holy Water"), None,
                              ("Fire", "Holy"), "Poison",
                              ("Undead", "Humanoid"), ("Darkness", "Poison", "Imp",
                                                       "Petrify", "Silence", "Berserk", "Sleep"))

Malboro: Bestiary = Bestiary("Malboro", 30, 2900, 980, 20, 95, 0,
                             10, 145, 0, 2292, 780,
                             "X-Potion", ("Remedy", "Holy Water"), None,
                             "Fire", ("Poison", "Water"), None,
                             ("Imp", "Silence", "Sleep"))

Cloudwraith: Bestiary = Bestiary("Cloudwraith", 29, 2058, 360, 13, 145, 0,
                                 10, 140, 0, 385, 485,
                                 ("Diamond Vest", "Hi-Potion"), ("Amulet", "Holy Water"),
                                 None, ("Fire", "Holy"), "Poison",
                                 "Undead", ("Darkness", "Poison", "Imp", "Petrify",
                                            "Silence", "Berserk", "Sleep", "Slow", "Stop"))

Exoray: Bestiary = Bestiary("Exoray", 29, 1200, 112, 13, 105, 0,
                            10, 105, 0, 370, 449,
                            None, "Holy Water", None, ("Fire", "Holy"),
                            "Poison", "Undead", ("Darkness", "Imp",
                                                 "Petrify", "Silence", "Berserk", "Confusion", "Sleep"))

SkeletalHorror: Bestiary = Bestiary("Skeletal Horror", 30, 1584, 143, 45, 115,
                                    0, 10, 155, 0, 542, 770,
                                    "Remedy", "Holy Water", None,
                                    ("Fire", "Holy"), "Poison", "Undead",
                                    ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk",
                                     "Sleep"))

Mugbear: Bestiary = Bestiary("Mugbear", 34, 2409, 74, 15, 165, 110,
                             10, 140, 0, 2000, 882,
                             "Thief's Bracer", None, None, "Fire",
                             None, None, ("Poison", "Silence", "Confusion"))

DevilFist: Bestiary = Bestiary("Devil Fist", 34, 1759, 68, 10, 125, 120,
                               10, 145, 0, 2000, 797,
                               "Brigand's Glove", "Air Knife", None, None,
                               "Poison", "Humanoid", ("Petrify", "Death",
                                                      "Berserk", "Confusion"))

Luridan: Bestiary = Bestiary("Luridan", 34, 2079, 122, 12, 210, 25,
                             10, 125, 0, 1000, 707,
                             "Hi-Potion", None, None, ("Fire", "Wind"),
                             None, None, ("Darkness", "Imp", "Berserk",
                                          "Confusion", "Sleep"))

Punisher: Bestiary = Bestiary("Punisher", 35, 2191, 136, 28, 100, 115,
                              10, 155, 0, 3000, 1242,
                              ("Bone Club", "Rising Sun"), None, None,
                              "Poison", None, "Humanoid",
                              ("Imp", "Sleep", "Slow", "Stop"))

GlasyaLabolas: Bestiary = Bestiary("Glasya Labolas", 35, 4771, 590, 23, 150,
                                   105, 10, 145, 10, 2500,
                                   2953, ("Muscle Belt", "Hi-Potion"), None,
                                   None, "Poison", None, "Humanoid",
                                   ("Death", "Silence"))

Gorgimera: Bestiary = Bestiary("Gorgimera", 36, 7191, 354, 40, 150, 0,
                               15, 160, 0, 1889, 4928,
                               "Golden Spear", None, None, None,
                               None, None, ("Darkness", "Imp", "Petrify",
                                            "Death", "Silence", "Berserk", "Confusion"))

Twinscythe: Bestiary = Bestiary("Twinscythe", 36, 2500, 187, 21, 125,
                                20, 21, 140, 0, 726, 1753,
                                "Poison Rod", "Poison Rod", None,
                                ("Fire", "Wind"), "Ice", None,
                                ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence",
                                 "Berserk", "Confusion", "Sleep"))

DeathWarden: Bestiary = Bestiary("Death Warden", 19, 8000, 8000, 13, 140,
                                 0, 55, 160, 0, 0, 0,
                                 ("Hi-Potion", "Potion"), "Tigerfang", None,
                                 ("Fire", "Holy"), "Poison", ("Undead", "Humanoid"),
                                 ("Poison", "Imp", "Silence", "Berserk", "Sleep", "Stop"))

Misty: Bestiary = Bestiary("Misty", 37, 3580, 500, 1, 110, 20, 8,
                           145, 0, 1260, 1151, "Moogle Suit",
                           None, None, "Poison", None, "Humanoid",
                           ("Darkness", "Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                            "Sleep"))

Rafflesia: Bestiary = Bestiary("Rafflesia", 37, 2200, 305, 13, 110, 0,
                               9, 140, 0, 767, 872,
                               "Nutkin Suit", None, None, "Fire",
                               "Water", None, ("Darkness", "Poison", "Imp",
                                               "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                               "Slow", "Stop"))

StillLife: Bestiary = Bestiary("Still Life", 37, 4889, 390, 13, 150, 0,
                               10, 150, 0, 1574, 2331,
                               "Fake Mustache", None, None, "Fire",
                               None, None, ("Darkness", "Poison", "Imp",
                                            "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                            "Slow", "Stop"))

CoeurlCat: Bestiary = Bestiary("Coeurl Cat", 36, 1115, 78, 17, 100, 10,
                               10, 140, 0, 416, 701,
                               "Tabby Suit", None, None, ("Fire", "Water"),
                               None, None, "Silence")

Crusher: Bestiary = Bestiary("Crusher", 36, 2095, 340, 13, 145, 0,
                             5, 85, 0, 577, 788,
                             "Super Ball", "Super Ball", None, "Fire",
                             None, None, ("Darkness", "Imp", "Petrify", "Death",
                                          "Berserk", "Confusion", "Sleep"))

BladeDancer: Bestiary = Bestiary("Blade Dancer", 22, 2539, 100, 1, 60, 0,
                                 30, 170, 0, 769, 1531,
                                 "Moogle Suit", None, None, "Poison",
                                 None, "Humanoid", ("Imp", "Petrify", "Death"))

Caladrius: Bestiary = Bestiary("Caladrius", 36, 885, 87, 14, 100, 90,
                               10, 150, 0, 497, 653,
                               "Chocobo Suit", None, None, "Fire",
                               None, None, ("Imp", "Sleep"))

Ouroboros: Bestiary = Bestiary("Ouroboros", 48, 50, 760, 13, 252, 0,
                               10, 252, 0, 390, 1780,
                               "Phoenix Down", "Phoenix Down", None, "Ice",
                               "Fire", None, ("Darkness", "Imp", "Petrify",
                                              "Silence", "Sleep"))

Face: Bestiary = Bestiary("Face", 47, 4550, 1700, 11, 105, 0,
                          10, 150, 0, 890, 2600,
                          "Phoenix Down", "Phoenix Down", None, "Ice",
                          "Fire", None, ("Imp", "Petrify", "Death", "Silence",
                                         "Sleep"))

Zeveak: Bestiary = Bestiary("Zeveak", 47, 2077, 500, 13, 80, 0,
                            10, 150, 0, 674, 1620,
                            "Phoenix Down", "Phoenix Down", None, "Ice",
                            "Fire", "Humanoid", ("Imp", "Petrify", "Silence",
                                                 "Slow", "Stop"))

Seaflower: Bestiary = Bestiary("Seaflower", 47, 4200, 200, 13, 135, 0,
                               10, 100, 0, 670, 1315,
                               "Phoenix Down", "Phoenix Down", None,
                               ("Ice", "Lightning"), ("Fire", "Water"), None,
                               ("Darkness", "Poison", "Imp", "Silence", "Berserk", "Confusion", "Sleep"))

Galypdes: Bestiary = Bestiary("Galypdes", 49, 6013, 820, 13, 120, 30,
                              10, 145, 0, 906, 2781,
                              ("Celestriad", "Phoenix Down"), "Phoenix Down", None,
                              "Ice", "Fire", None, ("Imp", "Petrify",
                                                    "Death", "Sleep"))

Necromancer: Bestiary = Bestiary("Necromancer", 48, 3525, 900, 13, 100, 0,
                                 7, 150, 0, 791, 1510,
                                 "Phoenix Down", "Holy Water", None,
                                 ("Fire", "Holy"), "Poison", ("Undead", "Humanoid"),
                                 ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Clymenus: Bestiary = Bestiary("Clymenus", 49, 3815, 9900, 13, 120, 0,
                              7, 165, 0, 826, 1698,
                              "Phoenix Down", "Phoenix Down", None, "Holy",
                              None, "Humanoid", ("Darkness", "Imp", "Death",
                                                 "Silence", "Confusion", "Sleep", "Stop"))

ChaosDragon: Bestiary = Bestiary("Chaos Dragon", 44, 9013, 1300, 13, 5,
                                 0, 10, 85, 0, 1000, 4881,
                                 "Phoenix Down", "Phoenix Down", None, "Ice",
                                 "Fire", None, ("Petrify", "Death", "Confusion",
                                                "Sleep"))

Brachiosaur: Bestiary = Bestiary("Brachiosaur", 77, 46050, 51420, 55, 190,
                                 70, 25, 145, 50, 0,
                                 14396, "Ribbon", "Celestriad", None,
                                 "Ice", None, None, ("Darkness",
                                                     "Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                                                     "Sleep", "Stop"))

Tyrannosaur: Bestiary = Bestiary("Tyrannosaur", 57, 12770, 420, 33, 125,
                                 0, 16, 160, 0, 0, 8800,
                                 "Reed Cloak", "Impartisan", None, "Ice",
                                 None, None, ("Darkness", "Poison", "Imp",
                                              "Petrify", "Death", "Silence", "Berserk", "Confusion", "Stop"))

Tumbleweed: Bestiary = Bestiary("Tumbleweed", 55, 6200, 600, 10, 120,
                                0, 10, 90, 0, 1333, 2554,
                                "Saucer", None, None, "Fire",
                                "Water", None, ("Darkness", "Poison", "Imp",
                                                "Silence", "Berserk", "Confusion", "Sleep"))

LeapFrog: Bestiary = Bestiary("Leap Frog", 52, 3511, 220, 13, 130, 0,
                              7, 145, 0, 2600, 1550,
                              ("Pinwheel", "Hi-Potion"), None, None, "Ice",
                              None, None, ("Poison", "Berserk", "Confusion",
                                           "Sleep"))

Slagworm: Bestiary = Bestiary("Slagworm", 49, 12018, 10500, 54, 130, 30,
                              22, 60, 0, 10000, 7524,
                              "Remedy", None, None, ("Ice", "Water"),
                              None, None, ("Imp", "Petrify", "Sleep"))

Cactuar: Bestiary = Bestiary("Cactuar", 27, 3, 60000, 1, 255, 250,
                             50, 255, 250, 10000, 0,
                             "Gold Needle", "Gold Needle", None,
                             ("Ice", "Water"), None, None,
                             ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk",
                              "Confusion", "Sleep"))

Crawler: Bestiary = Bestiary("Crawler", 51, 3200, 620, 13, 115, 0,
                             8, 150, 0, 1224, 1456,
                             "Remedy", None, None, "Ice", None,
                             None, "Poison")

Sprinter: Bestiary = Bestiary("Sprinter", 53, 4500, 350, 13, 100, 0,
                              10, 150, 0, 1420, 2293,
                              None, "Reed Cloak", None, "Lightning",
                              None, None, ("Darkness", "Poison", "Imp",
                                           "Petrify", "Slow", "Stop"))

Basilisk: Bestiary = Bestiary("Basilisk", 54, 5000, 1020, 13, 135, 10,
                              10, 155, 10, 1120, 2400,
                              "Tortoise Shield", "Tortoise Shield", None,
                              "Ice", None, None, "Petrify")

Lycaon: Bestiary = Bestiary("Lycaon", 50, 250, 20, 30, 100, 50,
                            10, 200, 0, 1524, 1356,
                            "X-Potion", None, None, "Water",
                            None, None, ("Death", "Silence"))

GreaterMantis: Bestiary = Bestiary("Greater Mantis", 54, 4500, 420, 180, 145,
                                   0, 10, 100, 0, 501, 4612,
                                   "Impartisan", None, None, "Fire",
                                   None, None, ("Darkness", "Imp",
                                                "Petrify", "Death", "Sleep"))

TestRider: Bestiary = Bestiary("Test Rider", 32, 3100, 220, 27, 135,
                               0, 10, 155, 0, 520, 1947,
                               "Partisan", "Heavy Lance", None, "Poison",
                               None, "Humanoid", ("Imp", "Petrify", "Death",
                                                  "Silence", "Confusion"))

Wizard: Bestiary = Bestiary("Wizard", 32, 1677, 200, 13, 50, 0,
                            10, 160, 0, 388, 587,
                            ("Ice Rod", "Thunder Rod"), "Flame Rod", None,
                            ("Lightning", "Poison"), None, "Humanoid",
                            ("Darkness", "Imp", "Petrify", "Death", "Berserk", "Confusion"))

Lukhavi: Bestiary = Bestiary("Lukhavi", 32, 1877, 100, 13, 145, 0,
                             10, 105, 0, 298, 697,
                             ("Hi-Potion", "Potion"), "Hi-Potion", None, "Fire",
                             None, None, "Death")

YellowMagnaRoader: Bestiary = Bestiary("Magna Roader", 32, 1777, 100, 13, 115,
                                       0, 10, 145, 0, 352, 621,
                                       ("Shuriken", "Lightning Scroll"), "Water Scroll",
                                       None, None, None, None,
                                       ("Poison", "Imp", "Petrify", "Silence"))

GoldMagnaRoader: Bestiary = Bestiary("Magna Roader", 32, 180, 70, 14, 105,
                                     0, 10, 150, 0, 284, 647,
                                     ("Shuriken", "Lightning Scroll"), "Flame Scroll",
                                     None, None, None, None,
                                     ("Darkness", "Poison", "Imp", "Silence"))

Psychos: Bestiary = Bestiary("Psychos", 32, 900, 55, 14, 165, 0,
                             10, 125, 0, 275, 347,
                             "Potion", "Potion", None, "Ice",
                             "Fire", None, ("Darkness", "Poison",
                                            "Imp", "Petrify", "Death", "Sleep"))

Garm: Bestiary = Bestiary("Garm", 32, 1510, 110, 10, 155, 0,
                          10, 140, 0, 412, 687,
                          "Potion", "Potion", None, None,
                          None, None, ("Darkness", "Poison", "Petrify",
                                       "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Tonberry: Bestiary = Bestiary("Tonberry", 27, 8000, 15500, 13, 150, 50,
                              10, 180, 50, 3333, 1200,
                              None, "Tintinnabulum", None,
                              ("Fire", "Lightning"), "Water", None,
                              ("Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

OnionDasher: Bestiary = Bestiary("Onion Dasher", 33, 2000, 100, 10, 150,
                                 0, 10, 120, 0, 150, 500,
                                 None, "Green Cherry", None,
                                 ("Lighting", "Water"), None, "Humanoid",
                                 ("Poison", "Imp", "Petrify"))

Anemone: Bestiary = Bestiary("Anemone", 33, 2000, 100, 10, 115, 0,
                             10, 145, 0, 550, 1000,
                             None, "Green Cherry", None, "Fire",
                             ("Lightning", "Water"), None, ("Darkness", "Imp",
                                                            "Berserk", "Confusion", "Sleep"))

Illuyankas: Bestiary = Bestiary("Illuyankas", 33, 2000, 100, 10, 130, 0,
                                10, 150, 0, 850, 1000,
                                None, ("White Cape", "Green Cherry"), None,
                                "Fire", "Lightning", None,
                                ("Darkness", "Poison", "Petrify", "Death", "Confusion"))

Knotty: Bestiary = Bestiary("Knotty", 33, 1000, 100, 5, 120, 0,
                            10, 140, 0, 350, 800, None,
                            "Green Cherry", None, "Fire", None,
                            None, "Imp")

Tzakmaqiel: Bestiary = Bestiary("Tzakmaqiel", 33, 2000, 100, 10, 105,
                                0, 10, 145, 0, 750, 1000,
                                None, ("White Cape", "Green Cherry"), None,
                                "Ice", None, None, ("Imp",
                                                    "Petrify", "Silence"))

ZoneEater: Bestiary = Bestiary("Zone Eater", 61, 7700, 57000, 23, 120, 0,
                               10, 150, 0, 2000, 2000,
                               "Teleport Stone", None,
                               ("Fire", "Lightning", "Poison", "Wind", "Earth", "Water"),
                               "Holy", "Ice", None,
                               ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence",
                                "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Vasegiatta: Bestiary = Bestiary("Vasegiatta", 42, 3615, 233, 13, 115, 0,
                                10, 145, 0, 1221, 1994,
                                "Phoenix Down", None, None, None,
                                None, None, ("Imp", "Petrify", "Death",
                                             "Sleep"))

Gloomwind: Bestiary = Bestiary("Gloomwind", 41, 2905, 175, 13, 115, 0,
                               10, 150, 0, 421, 1096,
                               "Hi-Potion", None, None, "Ice",
                               None, None, ("Darkness", "Poison", "Imp",
                                            "Petrify", "Berserk", "Confusion", "Sleep"))

Purusa: Bestiary = Bestiary("Purusa", 41, 3300, 188, 13, 115, 0,
                            10, 155, 0, 773, 1396,
                            "Moonring Blade", None, None, None,
                            None, None, ("Petrify", "Confusion"))

Covert: Bestiary = Bestiary("Covert", 44, 4530, 240, 25, 100, 50,
                            11, 150, 0, 1768, 1757,
                            ("Pinwheel", "Shuriken"), None, None,
                            "Holy", "Poison", "Humanoid",
                            ("Petrify", "Death", "Silence", "Confusion"))

Kamui: Bestiary = Bestiary("Kamui", 44, 4211, 219, 19, 100, 30,
                           11, 150, 30, 869, 1583,
                           ("Murasame", "Ashura"), "Holy Water", None,
                           ("Lightning", "Poison"), None, "Humanoid",
                           ("Petrify", "Death", "Silence", "Sleep"))

Wartpuck: Bestiary = Bestiary("Wartpuck", 44, 3559, 330, 15, 120, 0,
                              11, 160, 0, 1169, 1595,
                              ("Dried Meat", "Chain Flail"), None, None,
                              "Fire", None, None,
                              ("Poison", "Imp", "Death", "Berserk", "Confusion", "Slow", "Stop"))

ShamblingCorpse: Bestiary = Bestiary("Shambling Corpse", 43, 3850, 185, 13, 105,
                                     0, 10, 155, 0, 826, 1399,
                                     ("Soul Sabre", "Mythril Sword"), None, None,
                                     ("Fire", "Holy"), "Poison", "Undead",
                                     ("Darkness", "Imp", "Death", "Berserk", "Confusion", "Sleep"))

Amduscias: Bestiary = Bestiary("Amduscias", 43, 4452, 270, 13, 105, 0,
                               11, 150, 0, 526, 1727,
                               ("Swordbreaker", "Dagger"), None, None,
                               "Poison", None, "Humanoid",
                               ("Darkness", "Poison", "Imp", "Petrify", "Berserk", "Confusion", "Sleep"))

Baalzephon: Bestiary = Bestiary("Baalzephon", 43, 3609, 300, 17, 105, 20,
                                11, 150, 0, 826, 1385,
                                ("Sasuke", "Kunai"), None, None, "Fire",
                                ("Ice", "Lightning", "Poison", "Wind", "Earth", "Water"),
                                "Humanoid", ("Darkness", "Poison", "Imp", "Petrify",
                                             "Berserk", "Confusion", "Slow", "Stop"))

Samurai: Bestiary = Bestiary("Samurai", 40, 3000, 500, 13, 10, 0,
                             10, 20, 0, 791, 1545,
                             None, None, None, "Poison", None,
                             "Humanoid", ("Imp", "Petrify", "Death", "Silence",
                                          "Berserk", "Confusion"))

AlJabr: Bestiary = Bestiary("Al Jabr", 39, 2722, 180, 13, 110, 0,
                            10, 145, 30, 485, 890,
                            None, None, None, ("Ice", "Holy", "Water"),
                            None, "Humanoid", ("Imp", "Petrify", "Silence",
                                               "Berserk", "Sleep"))

Suriander: Bestiary = Bestiary("Suriander", 40, 2912, 228, 13, 105, 0,
                               10, 155, 0, 435, 1150,
                               None, None, None, "Holy",
                               None, None, ("Imp", "Death", "Berserk",
                                            "Confusion", "Slow", "Stop"))

Weredragon: Bestiary = Bestiary("Weredragon", 38, 3000, 300, 10, 105, 0,
                                3, 50, 0, 731, 953, None,
                                None, None, ("Fire", "Holy"), None,
                                None, ("Darkness", "Poison", "Imp", "Petrify",
                                       "Silence", "Berserk", "Sleep"))

Schmidt: Bestiary = Bestiary("Schmidt", 40, 3262, 200, 13, 105, 0,
                             8, 150, 0, 441, 1253, None,
                             None, None, ("Lightning", "Wind", "Water"),
                             None, None, ("Poison", "Imp", "Petrify"))

PlutoArmor: Bestiary = Bestiary("Pluto Armor", 39, 2850, 220, 13, 105, 0,
                                9, 150, 0, 629, 853, None,
                                None, None, ("Lightning", "Water"), None,
                                None, ("Poison", "Imp", "Petrify"))

AlluringRider: Bestiary = Bestiary("Alluring Rider", 40, 1200, 330, 13, 125,
                                   0, 10, 150, 0, 531, 1323,
                                   None, None, None, None, None,
                                   "Humanoid", ("Darkness", "Poison", "Imp",
                                                "Petrify", "Silence", "Berserk", "Sleep", "Slow", "Stop"))

Pandora: Bestiary = Bestiary("Pandora", 39, 1522, 350, 13, 140, 0,
                             10, 80, 0, 461, 622,
                             None, None, None, ("Fire", "Holy"),
                             "Poison", "Undead", ("Darkness", "Poison",
                                                  "Imp", "Petrify", "Silence", "Berserk", "Sleep"))

Parasite: Bestiary = Bestiary("Parasite", 39, 1000, 230, 1, 140, 0,
                              1, 5, 0, 461, 455, None,
                              None, None, "Fire", "None",
                              None, ("Darkness", "Poison", "Imp", "Petrify", "Silence",
                                     "Berserk", "Sleep"))

Coco: Bestiary = Bestiary("Coco", 39, 3062, 198, 13, 100, 0,
                          10, 160, 0, 631, 1410, None,
                          None, None, "Poison", None,
                          "Humanoid", ("Darkness", "Poison", "Imp", "Petrify", "Death",
                                       "Silence", "Berserk", "Confusion", "Sleep"))

Io_Enemy: Bestiary = Bestiary("Io", 39, 7862, 1550, 13, 110, 0,
                              10, 150, 0, 1995, 3253,
                              None, None, ("Poison", "Wind", "Earth"),
                              ("Lightning", "Holy", "Water"), None, None,
                              ("Darkness", "Poison", "Imp", "Silence", "Berserk", "Confusion",
                               "Sleep", "Stop"))

ArmoredWeapon: Bestiary = Bestiary("Armored Weapon", 47, 9200, 1956, 18, 190,
                                   10, 15, 125, 10, 1189,
                                   5848, "Debilitator", None, None,
                                   ("Lightning", "Water"), None, None,
                                   ("Darkness", "Poison", "Imp", "Petrify", "Silence",
                                    "Berserk", "Confusion", "Sleep"))

Lunatys: Bestiary = Bestiary("Lunatys", 45, 4020, 105, 13, 90, 0,
                             7, 250, 0, 465, 1504,
                             "Antidote", None, None, "Holy",
                             None, None, ("Poison", "Imp"))

FigaroLizard: Bestiary = Bestiary("Figaro Lizard", 45, 4220, 140, 29, 90,
                                  0, 10, 250, 0, 554, 1219,
                                  "Hi-Potion", None, None, "Ice",
                                  None, None, ("Poison", "Sleep"))

Devil: Bestiary = Bestiary("Devil", 46, 5555, 1150, 18, 70, 0,
                           7, 250, 0, 960, 2189,
                           "Mythril Glove", None, None, "Holy",
                           None, None, ("Imp", "Silence", "Berserk",
                                        "Sleep"))

Enuo: Bestiary = Bestiary("Enuo", 46, 4635, 280, 13, 50, 0,
                          10, 250, 0, 968, 1429,
                          "X-Potion", None, None, "Holy",
                          None, None, ("Darkness", "Poison", "Imp",
                                       "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

MagicUrn: Bestiary = Bestiary("Magic Urn", 31, 100, 10000, 5, 220,
                              100, 35, 190, 0, 0, 0,
                              ("Elixir", "Potion"), None, None, None,
                              ("Fire", "Ice", "Lightning", "Poison", "Wind", "Holy", "Earth", "Water"),
                              None, ("Darkness", "Poison", "Imp", "Petrify", "Death",
                                     "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

LvlTenMagic: Bestiary = Bestiary("Level 10 Magic", 48, 1000, 300, 10, 200,
                                 100, 22, 150, 0, 0, 0,
                                 "Ether", "Ether", None, ("Fire", "Holy"),
                                 "Poison", ("Undead", "Humanoid"), ("Imp",
                                                                    "Death", "Sleep", "Slow", "Stop"))

LvlTwentyMagic: Bestiary = Bestiary("Level 20 Magic", 51, 2000, 500, 10, 200,
                                    100, 21, 145, 0, 0, 0,
                                    "Ether", "Ether", None, None,
                                    "Poison", "Humanoid", ("Imp", "Petrify",
                                                           "Silence", "Berserk", "Sleep", "Stop"))

LvlThirtyMagic: Bestiary = Bestiary("Level 30 Magic", 54, 3000, 700, 10, 200,
                                    100, 20, 140, 0, 0, 0,
                                    "Ether", "Ether", None, "Poison",
                                    "Holy", None, ("Darkness", "Imp",
                                                   "Silence", "Confusion", "Stop"))

LvlFourtyMagic: Bestiary = Bestiary("Level 40 Magic", 55, 4000, 1000, 10, 200,
                                    100, 19, 135, 0, 0, 0,
                                    "Ether", "Ether", None, "Lightning",
                                    "Poison", "Humanoid", ("Darkness", "Imp",
                                                           "Death", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

LvlFiftyMagic: Bestiary = Bestiary("Level 50 Magic", 57, 5000, 2000, 10, 200,
                                   100, 18, 130, 0, 0, 0,
                                   "Hi-Ether", "Ether", None,
                                   ("Fire", "Holy"), "Poison", "Undead",
                                   ("Darkness", "Poison", "Imp", "Petrify", "Berserk", "Sleep"))

LvlSixtyMagic: Bestiary = Bestiary("Level 60 Magic", 58, 6000, 5000, 10, 200,
                                   100, 17, 125, 0, 0, 0,
                                   "Hi-Ether", "Ether", None, "Fire",
                                   "Ice", "Humanoid", ("Darkness", "Poison",
                                                       "Imp", "Death", "Berserk", "Confusion", "Stop"))

LvlSeventyMagic: Bestiary = Bestiary("Level 70 Magic", 56, 7000, 3000, 10, 200,
                                     100, 16, 120, 0, 0, 0,
                                     "Hi-Ether", "Ether", None,
                                     ("Ice", "Water"), "Fire", "Humanoid",
                                     ("Poison", "Imp", "Berserk", "Confusion", "Sleep"))

LvlEightyMagic: Bestiary = Bestiary("Level 80 Magic", 53, 8000, 2800, 10, 200,
                                    100, 15, 115, 0, 0, 0,
                                    "Hi-Ether", "Ether", None, "Poison",
                                    None, "Humanoid", ("Imp", "Silence",
                                                       "Berserk", "Confusion", "Slow", "Stop"))

LvlNinetyMagic: Bestiary = Bestiary("Level 90 Magic", 55, 9000, 9000, 10, 200,
                                    100, 14, 110, 0, 0, 0,
                                    "Hi-Ether", "Ether", ("Holy", "Earth", "Water"),
                                    None, "Wind", "Humanoid",
                                    ("Imp", "Petrify", "Death", "Silence", "Sleep"))

Warlock: Bestiary = Bestiary("Warlock", 38, 1300, 1250, 10, 180, 0,
                             10, 225, 0, 333, 970,
                             "Teleport Stone", "Teleport Stone", None,
                             ("Lightning", "Poison"), None, "Humanoid",
                             ("Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion"))

Mahadeva: Bestiary = Bestiary("Mahadeva", 38, 3826, 1327, 13, 150, 30,
                              10, 135, 0, 393, 1510,
                              "Teleport Stone", "Teleport Stone", None,
                              ("Fire", "Holy"), "Poison", "Undead",
                              ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk",
                               "Sleep"))

Sorath: Bestiary = Bestiary("Sorath", 37, 2600, 97, 13, 125, 20,
                            10, 145, 10, 415, 830,
                            "Teleport Stone", "Teleport Stone", None,
                            "Holy", None, None, ("Petrify", "Death",
                                                 "Silence"))

MedusaChicken: Bestiary = Bestiary("Medusa Chicken", 38, 2366, 185, 13, 105,
                                   0, 10, 155, 0, 422, 770,
                                   "Teleport Stone", "Teleport Stone", None,
                                   "Ice", "Poison", None,
                                   ("Darkness", "Poison", "Imp", "Petrify", "Silence",
                                    "Berserk", "Confusion", "Sleep"))

Creature: Bestiary = Bestiary("Creature", 37, 2470, 145, 13, 110, 10,
                              10, 155, 0, 550, 775,
                              "Teleport Stone", "Teleport Stone", None,
                              "Lightning", None, None,
                              ("Imp", "Sleep"))

Moonform: Bestiary = Bestiary("Moonform", 37, 2444, 82, 15, 115, 0,
                              0, 160, 0, 669, 981,
                              "Teleport Stone", "Teleport Stone", None,
                              ("Fire", "Holy"), "Poison", "Undead",
                              ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk",
                               "Sleep", "Slow", "Stop"))

Aspidochelon: Bestiary = Bestiary("Aspidochelon", 38, 3210, 514, 22, 135,
                                  0, 10, 150, 20, 519, 1270,
                                  "Teleport Stone", "Teleport Stone", None,
                                  ("Fire", "Holy"), "Poison", "Undead",
                                  ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk",
                                   "Sleep"))

SiegfriedColiseum: Bestiary = Bestiary("Siegfried", 53, 32760, 6000, 53, 160, 25,
                                       25, 150, 25, 0, 0, None,
                                       None, None, ("Fire", "Ice", "Lightning", "Poison",
                                                    "Wind", "Holy", "Earth", "Water"), None,
                                       "Humanoid", ("Petrify", "Death"))

Yojimbo: Bestiary = Bestiary("Yojimbo", 59, 7050, 2600, 13, 100, 40,
                             5, 180, 0, 2000, 2300,
                             "Masamune", None, None, "Poison",
                             None, "Humanoid", ("Darkness", "Petrify",
                                                "Death", "Confusion", "Sleep"))

DarkForce: Bestiary = Bestiary("Dark Force", 55, 8940, 700, 12, 105, 0,
                               7, 155, 0, 600, 2950,
                               "Crystal Sword", None, None, "Holy",
                               None, "Humanoid", ("Imp", "Silence",
                                                  "Berserk", "Confusion", "Sleep", "Stop"))

MuudSuud: Bestiary = Bestiary("Muud Suud", 54, 25000, 350, 13, 5, 0,
                              15, 70, 0, 100, 4200,
                              "Thunder Shield", None, None, "Holy",
                              None, None, ("Darkness", "Poison", "Imp",
                                           "Petrify", "Death", "Silence", "Sleep"))

FiendDragon: Bestiary = Bestiary("Fiend Dragon", 54, 18008, 10000, 13, 110,
                                 0, 13, 90, 0, 2700, 8500,
                                 "Guard Bracelet", None, None, None,
                                 None, None, ("Imp", "Petrify", "Death",
                                              "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Mover: Bestiary = Bestiary("Mover", 51, 120, 10500, 20, 115, 225,
                           10, 254, 0, 0, 1500,
                           "Super Ball", "Magicite Shard", None, None,
                           "Poison", None, ("Imp", "Petrify", "Silence",
                                            "Berserk", "Confusion", "Sleep"))

Cherry: Bestiary = Bestiary("Cherry", 53, 8150, 900, 8, 100, 0,
                            12, 155, 0, 700, 2200,
                            "Silver Spectacles", None, None, "Poison",
                            None, "Humanoid", ("Darkness", "Petrify",
                                               "Death", "Silence"))

VectorLythos: Bestiary = Bestiary("Vector Lythos", 59, 2800, 180, 13, 110,
                                  0, 7, 150, 0, 350, 1400,
                                  "Fuma Shuriken", None, None,
                                  ("Ice", "Water"), None, None,
                                  ("Darkness", "Poison", "Death", "Berserk", "Confusion",
                                   "Sleep", "Slow", "Stop"))

PrimevalDragon: Bestiary = Bestiary("Primeval Dragon", 50, 10050, 12850, 15, 130,
                                    0, 12, 110, 0, 1200, 3000,
                                    "Dried Meat", None, None, "Ice",
                                    None, None, ("Death", "Berserk", "Confusion"))

Landworm: Bestiary = Bestiary("Landworm", 59, 12000, 1300, 13, 80, 0,
                              8, 120, 0, 0, 4600,
                              "X-Potion", None, None, "Ice",
                              "Earth", None, "Imp")

Gamma: Bestiary = Bestiary("Gamma", 57, 27000, 9000, 13, 175, 0,
                           15, 145, 0, 0, 9000,
                           "Air Anchor", None, None, ("Lightning", "Water"),
                           None, None, ("Darkness", "Poison", "Imp", "Petrify",
                                        "Death", "Silence", "Berserk", "Confusion", "Sleep"))

GreatMalboro: Bestiary = Bestiary("Great Malboro", 56, 7000, 500, 13, 115,
                                  0, 6, 105, 0, 1320, 2800,
                                  "Teleport Stone", None, None, "Fire",
                                  ("Ice", "Lightning", "Poison", "Wind", "Holy", "Earth", "Water"),
                                  None, ("Darkness", "Silence"))

Outsider: Bestiary = Bestiary("Outsider", 18, 8050, 400, 15, 105, 0,
                              4, 155, 0, 2800, 2600,
                              "Stoneblade", None, None, "Holy",
                              "Poison", "Humanoid", ("Darkness", "Poison",
                                                     "Imp", "Berserk", "Confusion", "Sleep"))

DemonKnight: Bestiary = Bestiary("Demon Knight", 56, 6800, 1600, 12, 110,
                                 0, 14, 145, 0, 200, 3090,
                                 "Pinwheel", None, None, None,
                                 None, "Humanoid", ("Imp", "Petrify", "Death"))

DuelArmor: Bestiary = Bestiary("Duel Armor", 53, 7200, 1600, 13, 185,
                               0, 10, 145, 0, 800, 2500,
                               "Chainsaw", None, None,
                               ("Lightning", "Water"), None, None,
                               ("Poison", "Imp", "Petrify"))

GreatBehemoth: Bestiary = Bestiary("Great Behemoth", 58, 11000, 700, 7, 90,
                                   0, 10, 105, 0, 2900, 4100,
                                   "Tigerfang", None, None, None,
                                   None, None, ("Darkness", "Imp", "Petrify",
                                                "Death", "Silence", "Confusion"))

VectorChimera: Bestiary = Bestiary("Vector Chimera", 57, 7500, 880, 22, 110,
                                   30, 9, 150, 30, 900, 2900,
                                   "Swordbreaker", None, None, None,
                                   None, None, ("Darkness", "Imp", "Petrify",
                                                "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow",
                                                "Stop"))

Fortis: Bestiary = Bestiary("Fortis", 54, 9800, 700, 5, 160, 0,
                            10, 150, 0, 250, 3500,
                            "Drill", None, None, ("Lightning", "Water"),
                            None, None, ("Poison", "Imp", "Petrify"))

Junk: Bestiary = Bestiary("Junk", 53, 2000, 200, 2, 190, 0, 10,
                          170, 0, 1100, 2200, "Noiseblaster",
                          None, None, ("Lightning", "Water"), None,
                          None, ("Poison", "Imp", "Petrify"))

InnoSent: Bestiary = Bestiary("InnoSent", 52, 6600, 390, 13, 155, 0,
                              12, 155, 0, 1950, 2400,
                              "Bioblaster", None, None,
                              ("Lightning", "Water"), None, None,
                              ("Poison", "Imp", "Petrify", "Stop"))

Daedalus: Bestiary = Bestiary("Daedalus", 59, 12280, 100, 13, 105, 0,
                              12, 150, 0, 0, 3500, None,
                              None, None, ("Fire", "Holy"), "Poison",
                              "Undead", ("Darkness", "Poison", "Imp", "Petrify", "Silence",
                                         "Berserk", "Sleep", "Stop"))

Ahriman: Bestiary = Bestiary("Ahriman", 51, 10000, 300, 11, 110, 0,
                             17, 145, 0, 0, 2820, "Earring",
                             None, None, None, None, None,
                             ("Imp", "Petrify", "Death"))

DeathMachine: Bestiary = Bestiary("Death Machine", 52, 6000, 550, 10, 140,
                                  0, 5, 140, 0, 670, 2300,
                                  "Flash", None, None,
                                  ("Lightning", "Water"), None, None,
                                  ("Poison", "Imp", "Petrify"))

MetalHitman: Bestiary = Bestiary("Metal Hitman", 52, 2000, 800, 13, 20, 0,
                                 25, 165, 0, 700, 2000,
                                 "Auto Crossbow", None, None,
                                 ("Lightning", "Water"), None, None,
                                 ("Poison", "Imp", "Petrify"))

Prometheus: Bestiary = Bestiary("Prometheus", 56, 14500, 2050, 13, 170, 0,
                                10, 150, 0, 1300, 5200,
                                "Debilitator", None, None, ("Lightning", "Water"),
                                None, None, ("Darkness", "Poison", "Imp",
                                             "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                             "Stop"))

Zurvan: Bestiary = Bestiary("Zurvan", 72, 24000, 300, 33, 80, 0,
                            8, 150, 0, 5200, 5000,
                            "X-Potion", None, None, ("Lightning", "Holy",
                                                     "Water"), None, None,
                            ("Poison", "Imp", "Petrify", "Berserk", "Confusion", "Stop"))

Vilia: Bestiary = Bestiary("Vilia", 81, 23000, 1800, 22, 100, 10,
                           14, 160, 0, 3333, 5000,
                           "X-Ether", None, None, "Poison",
                           None, "Humanoid", ("Darkness", "Poison", "Imp",
                                              "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                              "Stop"))

GreatDragon: Bestiary = Bestiary("Great Dragon", 77, 28000, 2200, 53, 155,
                                 0, 11, 100, 0, 0, 5000,
                                 ("Elixir", "Phoenix Down"), "Dragon Horn", None,
                                 "Lightning", None, None,
                                 ("Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion"))

Abaddon: Bestiary = Bestiary("Abaddon", 71, 25000, 8000, 30, 160, 0,
                             30, 180, 0, 0, 5000,
                             "Hi-Ether", "Lich Ring", None,
                             ("Fire", "Holy"), "Poison", ("Undead", "Humnaoid"),
                             ("Poison", "Imp", "Petrify", "Death", "Silence", "Confusion", "Sleep",
                              "Slow", "Stop"))

DragonAevis: Bestiary = Bestiary("Dragon Aevis", 77, 23000, 500, 25, 80,
                                 50, 15, 180, 20, 1200, 5000,
                                 "Dragon Horn", None, None, "Fire",
                                 None, None, ("Imp", "Petrify"))

Dinozombie: Bestiary = Bestiary("Dinozombie", 60, 25000, 600, 25, 150, 0,
                                3, 150, 0, 3700, 5000,
                                ("Hi-Ether", "Holy Water"), None, None,
                                ("Fire", "Ice", "Holy", "Water"), "Poison",
                                "Undead", "Imp")

DeathRider: Bestiary = Bestiary("Death Rider", 76, 30000, 1200, 48, 150,
                                20, 19, 150, 20, 6600, 5000,
                                None, "Red Jacket", None,
                                ("Fire", "Poison"), None, ("Undead", "Humanoid"),
                                ("Imp", "Petrify", "Confusion", "Stop"))

ShieldDragon: Bestiary = Bestiary("Shield Dragon", 71, 40000, 20000, 22, 200,
                                  0, 22, 120, 0, 6300, 5000,
                                  None, "Force Armor", None, "Ice",
                                  None, None, ("Petrify", "Death", "Berserk",
                                               "Confusion"))

Maximera: Bestiary = Bestiary("Maximera", 89, 32000, 2000, 31, 110, 30,
                              9, 150, 30, 0, 5000,
                              "Hi-Ether", None, None, None,
                              None, None, ("Darkness", "Imp", "Petrify",
                                           "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                           "Slow", "Stop"))

Hexadragon: Bestiary = Bestiary("Hexadragon", 73, 26000, 750, 55, 95, 0,
                                16, 50, 0, 1500, 5000,
                                ("X-Potion", "Remedy"), None, None,
                                ("Fire", "Holy"), None, None,
                                ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk",
                                 "Sleep", "Slow", "Stop"))

MagicDragon: Bestiary = Bestiary("Magic Dragon", 72, 18000, 10000, 14, 180,
                                 0, 18, 150, 0, 950, 5000,
                                 "X-Ether", None, None, ("Ice", "Water"),
                                 None, None, ("Darkness", "Poison", "Death",
                                              "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Armodullahan: Bestiary = Bestiary("Armodullahan", 83, 35000, 2500, 60, 140,
                                  20, 22, 200, 0, 0, 5000,
                                  "Genji Glove", "X-Potion", None, "Fire",
                                  "Ice", "Undead", ("Poison", "Imp", "Petrify",
                                                    "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow",
                                                    "Stop"))

CrystalDragon: Bestiary = Bestiary("Crystal Dragon", 89, 32000, 30000, 35, 155,
                                   30, 26, 380, 10, 7700,
                                   5000, "Elixir", "X-Ether", None,
                                   None, None, None, ("Imp",
                                                      "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                                      "Slow", "Stop"))

YmirShell: Bestiary = Bestiary("Ymir", 4, 50000, 120, 13, 102, 0,
                               5, 155, 0, 0, 0, None,
                               "Ether", None, None, "Lightning",
                               None, ("Darkness", "Poison", "Imp", "Petrify",
                                      "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

YmirHead: Bestiary = Bestiary("Ymir", 6, 1600, 1000, 22, 100, 0,
                              10, 155, 0, 0, 0, None,
                              "Hi-Potion", None, None, None,
                              None, ("Darkness", "Poison", "Imp", "Petrify",
                                     "Death", "Silence", "Berserk", "Confusion", "Sleep"))

GuardLeader: Bestiary = Bestiary("Guard Leader", 8, 420, 150, 60, 110, 0,
                                 9, 140, 0, 350, 0,
                                 "Mythril Knife", "Hi-Potion", None,
                                 "Poison", None, "Humanoid", "Poison")

MagitekArmor: Bestiary = Bestiary("Magitek Armor", 8, 210, 250, 18, 30, 0,
                                  3, 130, 0, 0, 0,
                                  ("Hi-Potion", "Potion"), "Potion", None,
                                  "Lightning", None, None,
                                  ("Poison", "Imp", "Petrify", "Death"))

Vargas: Bestiary = Bestiary("Vargas", 12, 11600, 220, 13, 85, 0,
                            10, 150, 0, 0, 0,
                            ("Mythril Claws", "Potion"), None, None,
                            "Poison", None, "Humanoid",
                            ("Poison", "Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                             "Sleep"))

Ipooh: Bestiary = Bestiary("Ipooh", 11, 360, 60, 18, 105, 0,
                           10, 150, 0, 0, 0,
                           "Hi-Potion", None, None, "Fire", None,
                           None, ("Poison", "Petrify", "Death", "Berserk", "Confusion",
                                  "Sleep"))

UltrosLeteRiver: Bestiary = Bestiary("Ultros", 13, 3000, 640, 15, 40, 0,
                                     3, 140, 0, 0, 0,
                                     None, None, None, ("Fire", "Lightning"),
                                     "Water", None, ("Poison", "Imp", "Petrify",
                                                     "Death", "Silence", "Berserk", "Confusion", "Sleep"))

TunnelArmor: Bestiary = Bestiary("Tunnel Armor", 16, 1300, 900, 10, 29,
                                 0, 15, 145, 0, 250, 0,
                                 ("Bioblaster", "Air Knife"), "Elixir", None,
                                 ("Lightning", "Water"), None, None,
                                 ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence",
                                  "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

PhantomTrain: Bestiary = Bestiary("Phantom Train", 14, 1900, 350, 10, 30,
                                  0, 5, 210, 0, 0, 0,
                                  None, "Tent", None,
                                  ("Fire", "Lightning", "Holy"), "Poison",
                                  "Undead", ("Darkness", "Poison", "Imp", "Petrify",
                                             "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Rhizopas: Bestiary = Bestiary("Rhizopas", 13, 775, 39, 14, 110, 0,
                              3, 175, 0, 0, 0, None,
                              "Remedy", None, "Lightning", "Water",
                              None, ("Poison", "Imp", "Petrify", "Death", "Silence"))

HellsRider: Bestiary = Bestiary("Hell's Rider", 14, 1300, 170, 48, 120,
                                0, 10, 150, 0, 1290, 400,
                                ("Elixir", "Mythril Vest"), "Remedy", None,
                                ("Fire", "Poison"), None, "Humanoid",
                                ("Imp", "Confusion"))

KefkaNarshe: Bestiary = Bestiary("Kefka", 18, 3000, 3000, 25, 55, 30,
                                 9, 160, 30, 0, 0,
                                 ("Elixir", "Hi-Ether"), "Peace Ring", None,
                                 None, None, "Humanoid",
                                 ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Berserk",
                                  "Confusion", "Sleep"))

Dadaluma: Bestiary = Bestiary("Dadaluma", 22, 3270, 1005, 12, 85, 0,
                              3, 143, 10, 1210, 0,
                              ("Thief's Bracer", "Jeweled Ring"),
                              ("Thief's Knife", "Twist Headband"), None, "Poison",
                              None, "Humanoid", ("Poison", "Death",
                                                 "Berserk", "Confusion"))

UltrosOpera: Bestiary = Bestiary("Ultros", 19, 2550, 500, 13, 105, 0,
                                 4, 150, 0, 2, 0,
                                 None, None, None, ("Fire", "Lightning"),
                                 "Water", None, ("Poison", "Imp", "Petrify",
                                                 "Death", "Silence", "Berserk", "Confusion", "Sleep"))

Ifrit: Bestiary = Bestiary("Ifrit", 21, 3300, 600, 25, 215, 20,
                           7, 115, 0, 0, 0, None,
                           None, ("Lightning", "Poison", "Wind", "Holy", "Earth", "Water"),
                           "Ice", "Fire", None, ("Poison", "Imp",
                                                 "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                                 "Stop"))

Shiva: Bestiary = Bestiary("Shiva", 21, 3000, 500, 15, 200, 20,
                           7, 110, 0, 0, 0, None,
                           None, ("Lightning", "Poison", "Wind", "Holy", "Earth", "Water"),
                           "Fire", "Ice", None, ("Poison", "Imp",
                                                 "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                                 "Stop"))

NumberTwentyFour: Bestiary = Bestiary("Number 024", 24, 4777, 777, 20, 170, 0,
                                      3, 100, 0, 0, 0,
                                      ("Blood Sword", "Rune Blade"), ("Flametongue", "Icebrand"),
                                      "???", "???", "???", "Humanoid",
                                      ("Darkness", "Poison", "Petrify", "Death", "Silence", "Berserk",
                                       "Confusion", "Slow", "Stop"))

NumberOneTwentyEight: Bestiary = Bestiary("Number 128", 23, 3276, 810, 13, 120,
                                          0, 3, 125, 0, 0, 0,
                                          "Kazekiri", "Tent", None, None,
                                          "Ice", None, ("Poison", "Imp",
                                                        "Petrify", "Death", "Silence", "Confusion", "Sleep", "Stop"))

RightBlade: Bestiary = Bestiary("Right Blade", 21, 400, 150, 20, 120, 0,
                                5, 150, 0, 0, 0, "Ether",
                                None, None, None, "Ice", None,
                                ("Darkness", "Poison", "Imp", "Silence", "Berserk", "Confusion",
                                 "Sleep"))

LeftBlade: Bestiary = Bestiary("Left Blade", 22, 700, 470, 13, 120, 0,
                               5, 150, 0, 0, 0, "Ether",
                               None, None, None, "Ice", None,
                               ("Darkness", "Poison", "Imp", "Silence", "Berserk", "Confusion",
                                "Sleep"))

LeftCrane: Bestiary = Bestiary("Crane", 23, 1800, 447, 14, 145, 0,
                               4, 120, 0, 0, 0,
                               "Noiseblaster", None, None, "Water",
                               "Lightning", None, ("Darkness", "Poison",
                                                   "Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                                                   "Sleep", "Stop"))

RightCrane: Bestiary = Bestiary("Crane", 24, 1800, 447, 14, 125, 0,
                                4, 120, 0, 0, 0,
                                ("Debilitator", "Hi-Potion"), None, None,
                                ("Lightning", "Water"), "Fire", None,
                                ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                                 "Confusion", "Sleep", "Stop"))

FlameEater: Bestiary = Bestiary("Flame Eater", 26, 8400, 480, 13, 105, 20,
                                7, 150, 0, 0, 0,
                                "Flametongue", None, ("Lightning", "Poison", "Holy",
                                                      "Earth"), "Ice", "Fire", None,
                                ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                                 "Confusion", "Sleep", "Stop"))

UltrosThamasaCave: Bestiary = Bestiary("Ultros", 25, 22000, 750, 22, 95,
                                       0, 7, 155, 0, 3, 0,
                                       "White Cape", None, None,
                                       ("Fire", "Lightning"), "Water", None,
                                       ("Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                                        "Confusion", "Sleep"))

TyphonIAF: Bestiary = Bestiary("Typhon", 26, 10000, 40000, 13, 100, 0,
                               10, 55, 0, 0, 0, "Dagger",
                               None, None, ("Ice", "Water"), "Fire",
                               None, ("Poison", "Imp", "Petrify", "Death", "Confusion"))

FinalUltros: Bestiary = Bestiary("Ultros", 26, 17000, 8000, 10, 20, 0,
                                 3, 10, 0, 0, 0,
                                 "Dried Meat", None, None, ("Fire", "Poison"),
                                 "Water", None, ("Poison", "Imp", "Petrify",
                                                 "Death", "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

AirForce: Bestiary = Bestiary("Air Force", 25, 8000, 750, 10, 150, 0,
                              12, 120, 0, 0, 0, "Elixir",
                              "Princess Ring", None, ("Lightning", "Water"),
                              None, None, ("Darkness", "Poison", "Imp",
                                           "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow",
                                           "Stop"))

LaserGun: Bestiary = Bestiary("Laser Gun", 24, 3300, 335, 12, 130, 0,
                              9, 140, 0, 0, 0, "X-Ether",
                              None, None, ("Lightning", "Water"), None,
                              None, ("Darkness", "Poison", "Imp", "Petrify", "Death",
                                     "Silence", "Berserk", "Confusion", "Sleep"))

MissileBay: Bestiary = Bestiary("Missile Bay", 25, 3000, 7000, 12, 135, 0,
                                8, 150, 0, 0, 0,
                                "Debilitator", None, None,
                                ("Lightning", "Water"), None, None,
                                ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                                 "Confusion", "Sleep"))

BitEnemy: Bestiary = Bestiary("Bit", 25, 420, 285, 12, 230, 0,
                              10, 160, 0, 0, 0,
                              "Amulet", None, None, ("Lightning", "Water"),
                              None, None, ("Darkness", "Poison", "Imp", "Petrify",
                                           "Death", "Silence", "Berserk", "Confusion", "Sleep"))

Gigantos: Bestiary = Bestiary("Gigantos", 25, 6000, 1120, 20, 1, 0,
                              10, 1, 0, 0, 7550,
                              ("Elixir", "X-Potion"), "Sasuke", None,
                              "Poison", None, "Humanoid",
                              ("Confusion", "Sleep"))

UltimaWeaponFC: Bestiary = Bestiary("Ultima Weapon", 37, 24000, 5000, 45, 142,
                                    20, 5, 97, 10, 0, 0,
                                    ("Ribbon", "Elixir"), "Elixir", None,
                                    None, None, None, ("Poison", "Imp",
                                                       "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                                       "Stop"))

Nelapa: Bestiary = Bestiary("Nelapa", 26, 2800, 280, 11, 105, 0,
                            10, 150, 0, 0, 0, None,
                            None, ("Poison", "Wind", "Earth", "Water"),
                            ("Ice", "Lightning", "Holy"), "Fire", "Humanoid",
                            ("Darkness", "Poison", "Imp", "Petrify", "Silence", "Sleep", "Slow"))

Humbaba: Bestiary = Bestiary("Humbaba", 31, 26000, 10000, 15, 100, 0,
                             6, 130, 0, 0, 0, None,
                             None, None, "Poison", "Lightning",
                             None, ("Poison", "Imp", "Petrify", "Death", "Silence",
                                    "Berserk", "Confusion", "Slow", "Stop"))

# Tentacles Fight
# Bottom Right
TentacleBR: Bestiary = Bestiary("Tentacle", 31, 7000, 800, 13, 102, 0,
                                8, 153, 0, 0, 0, None,
                                None, None, ("Ice", "Water"), "Fire",
                                None, ("Imp", "Death", "Berserk", "Confusion", "Stop"))

# Top Right
TentacleTR: Bestiary = Bestiary("Tentacle", 33, 5000, 600, 13, 102, 0,
                                8, 153, 0, 0, 0, None,
                                None, None, None, ("Lightning", "Water"),
                                None, ("Imp", "Death", "Berserk", "Confusion", "Stop"))

# Bottom Left
TentacleBL: Bestiary = Bestiary("Tentacle", 32, 6000, 700, 13, 102, 0,
                                8, 153, 0, 0, 0, None,
                                None, None, "Fire", ("Ice", "Water"),
                                None, ("Imp", "Petrify", "Silence", "Berserk", "Confusion",
                                       "Sleep", "Stop"))

# Top Left
TentacleTL: Bestiary = Bestiary("Tentacle", 34, 4000, 500, 13, 102, 0,
                                8, 153, 0, 0, 0, None,
                                None, None, None, ("Earth", "Water"),
                                None, ("Darkness", "Poison", "Imp", "Death", "Silence",
                                       "Berserk", "Confusion", "Sleep"))

AnglerWhelkShell: Bestiary = Bestiary("Angler Whelk", 19, 9230, 1600, 53, 160,
                                      0, 10, 195, 0, 1000, 0,
                                      None, "Dragon Claws", None, "Fire",
                                      ("Ice", "Lightning", "Water"), None,
                                      ("Darkness", "Poison", "Imp", "Silence", "Berserk", "Confusion",
                                       "Sleep", "Slow", "Stop"))

AnglerWhelkHead: Bestiary = Bestiary("Angler Whelk", 31, 9845, 1600, 75, 80,
                                     0, 7, 150, 0, 1000, 0,
                                     None, "Dragon Claws", "Poison", "Fire",
                                     ("Ice", "Lightning", "Water"), None,
                                     ("Poison", "Imp", "Berserk", "Confusion"))

Dullahan: Bestiary = Bestiary("Dullahan", 37, 23450, 1721, 55, 130,
                              10, 7, 160, 0, 0, 0,
                              ("Genji Glove", "X-Potion"), None, None,
                              "Fire", "Ice", None, ("Poison", "Imp",
                                                    "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                                    "Stop"))

BehemothKingLeft: Bestiary = Bestiary("Behemoth King", 43, 19000, 1600, 11, 120,
                                      0, 9, 130, 0, 0, 0,
                                      "Murasame", "Behemoth Suit", None,
                                      ("Fire", "Poison"), "Ice", None,
                                      ("Poison", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                                       "Sleep"))

BehemothKingRight: Bestiary = Bestiary("Behemoth King", 49, 19000, 9999, 27,
                                       105, 0, 10, 150, 0, 0,
                                       0, None, "Behemoth Suit", None,
                                       ("Fire", "Holy"), "Poison", "Undead",
                                       ("Poison", "Imp", "Petrify", "Silence", "Berserk", "Confusion",
                                        "Sleep", "Slow", "Stop"))

Chadarnook: Bestiary = Bestiary("Chadarnook", 37, 56000, 9400, 13, 140,
                                0, 10, 150, 0, 0, 0,
                                None, None, None, "Fire",
                                ("Holy", "Water"), None,
                                ("Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                                 "Confusion", "Sleep", "Stop"))

Valigarmanda: Bestiary = Bestiary("Valigarmanda", 62, 30000, 50000, 19, 254,
                                  0, 4, 70, 0, 0, 0,
                                  None, None, ("Lightning", "Poison", "Wind",
                                               "Holy", "Earth", "Water"), "Fire", "Ice",
                                  None, ("Poison", "Imp", "Petrify", "Death", "Silence",
                                         "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Tonberries: Bestiary = Bestiary("Tonberries", 99, 14001, 11000, 5, 100,
                                150, 1, 150, 0, 0, 0,
                                "Minvera Bustier", "Minvera Bustier", None,
                                "Fire", "Water", None,
                                ("Petrify", "Death", "Berserk", "Confusion", "Sleep", "Stop"))

UmaroDabbing: Bestiary = Bestiary("Yeti", 33, 17200, 6990, 25, 100, 0,
                                  11, 150, 0, 10, 0,
                                  None, None, None, ("Fire", "Poison"),
                                  "Ice", "Humanoid", ("Imp", "Petrify",
                                                      "Death", "Silence", "Confusion", "Stop"))

Curlax: Bestiary = Bestiary("Curlax", 47, 15000, 2000, 1, 100, 0,
                            4, 110, 0, 0, 0, None,
                            None, None, ("Ice", "Water"), "Fire",
                            "Humanoid", ("Poison", "Imp", "Petrify", "Death", "Silence",
                                         "Berserk", "Confusion", "Slow", "Stop"))

Laragorn: Bestiary = Bestiary("Laragorn", 47, 10000, 2000, 2, 90, 0,
                              5, 120, 0, 0, 0, None,
                              None, None, "Fire", ("Ice", "Wind"),
                              "Humanoid", ("Poison", "Imp", "Petrify", "Berserk",
                                           "Sleep", "Stop"))

Moebius: Bestiary = Bestiary("Moebius", 47, 12500, 2000, 4, 80, 0,
                             6, 130, 0, 0, 0, None,
                             None, None, None, "Lightning",
                             "Humanoid", ("Poison", "Imp", "Petrify", "Death", "Silence",
                                          "Confusion", "Sleep", "Slow"))

Wrexsoul: Bestiary = Bestiary("Wrexsoul", 53, 23066, 5066, 27, 70, 0,
                              5, 220, 0, 0, 0,
                              "Memento Ring", "Guard Bracelet", None,
                              "Ice", ("Fire", "Holy"), None,
                              ("Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                               "Confusion", "Sleep", "Slow", "Stop"))

SoulSaver: Bestiary = Bestiary("Soul Saver", 41, 3066, 566, 50, 150, 0,
                               3, 175, 0, 0, 0, None,
                               None, None, "Ice", ("Fire", "Holy"),
                               "Humanoid", ("Poison", "Imp", "Silence", "Sleep", "Stop"))

MasterTonberry: Bestiary = Bestiary("Master Tonberry", 73, 22000, 1200, 13, 100,
                                    0, 9, 165, 0, 0, 0,
                                    ("Megalixir", "Elixir"), "Gladius", "???",
                                    "???", "???", None,
                                    ("Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                                     "Stop"))

SamuraiSoul: Bestiary = Bestiary("Samurai Soul", 61, 37620, 7400, 25, 115,
                                 20, 11, 175, 0, 30000, 0,
                                 ("Murakumo", "Murasame"), "Master's Scroll", None,
                                 "Poison", None, "Humanoid",
                                 ("Imp", "Petrify", "Death", "Silence", "Berserk", "Sleep",
                                  "Slow", "Stop"))

MagiMaster: Bestiary = Bestiary("Magic Master", 68, 50000, 50000, 1, 250,
                                100, 25, 100, 0, 0, 0,
                                ("Crystal Orb", "Elixir"), "Megalixir", "???",
                                "???", "???", "Humanoid",
                                ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence",
                                 "Confusion", "Sleep", "Slow", "Stop"))

DoomGaze: Bestiary = Bestiary("Deathgaze", 68, 55555, 38000, 35, 150, 30,
                              8, 170, 30, 0, 0, None,
                              None, None, ("Fire", "Holy"),
                              ("Ice", "Poison"), None, ("Darkness", "Poison",
                                                        "Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                                                        "Sleep", "Slow", "Stop"))

Hidon: Bestiary = Bestiary("Hidon", 43, 25000, 12500, 13, 110, 0,
                           10, 160, 0, 0, 0,
                           ("Thornlet", "Teleport Stone"), "Teleport Stone", None,
                           ("Fire", "Holy", "Earth"), "Poison", "Undead",
                           ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                            "Confusion", "Sleep", "Stop"))

Erebus: Bestiary = Bestiary("Erebus", 43, 3500, 1000, 13, 85, 0,
                            10, 150, 0, 0, 0, None,
                            None, None, "Earth", "Poison",
                            None, ("Imp", "Berserk", "Confusion", "Sleep"))

ErebusTwo: Bestiary = Bestiary("Erebus", 43, 3500, 1000, 13, 115,
                               0, 10, 120, 0, 0, 0,
                               None, None, None, None,
                               ("Fire", "Ice", "Lightning", "Poison", "Wind", "Holy", "Water"),
                               None, ("Imp", "Death", "Silence", "Confusion", "Sleep",
                                      "Slow", "Stop"))

ErebusThree: Bestiary = Bestiary("Erebus", 43, 3500, 1000, 13, 105, 0,
                                 10, 130, 0, 0, 0, None,
                                 None, None, ("Fire", "Holy"), "Poison",
                                 "Undead", ("Darkness", "Poison", "Imp", "Petrify",
                                            "Silence", "Berserk", "Sleep"))

ErebusFour: Bestiary = Bestiary("Erebus", 43, 3500, 1000, 13, 95, 0,
                                10, 140, 0, 0, 0, None,
                                None, None, ("Fire", "Ice", "Lightning", "Poison",
                                             "Wind", "Holy", "Earth", "Water"), None, None,
                                ("Imp", "Petrify"))

RedDragon: Bestiary = Bestiary("Red Dragon", 67, 30000, 1780, 13, 110, 0,
                               10, 150, 0, 0, 0,
                               None, "Murakumo", None, ("Ice", "Water"),
                               "Fire", None, ("Imp", "Petrify", "Death",
                                              "Silence", "Berserk", "Sleep", "Stop"))

BlueDragon: Bestiary = Bestiary("Blue Dragon", 65, 26900, 3800, 13, 110,
                                0, 10, 150, 0, 0, 0,
                                None, "Zantetsuken", None, "Lightning",
                                "Water", None, ("Imp", "Petrify", "Death",
                                                "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

GoldDragon: Bestiary = Bestiary("Gold Dragon", 62, 32400, 4000, 13, 110,
                                0, 10, 150, 0, 0, 0,
                                None, "Crystal Orb", None, "Water",
                                "Lightning", None, ("Imp", "Petrify",
                                                    "Death", "Silence", "Confusion", "Sleep", "Slow", "Stop"))

IceDragon: Bestiary = Bestiary("Ice Dragon", 74, 24400, 9000, 13, 110, 0,
                               10, 150, 0, 0, 0, None,
                               "Force Shield", None, "Fire", "Ice",
                               None, ("Imp", "Petrify", "Death", "Sleep", "Stop"))

StormDragon: Bestiary = Bestiary("Storm Dragon", 74, 42000, 1250, 13, 110,
                                 0, 9, 150, 0, 0, 0,
                                 None, "Force Armor", None, "Lightning",
                                 "Wind", None, ("Poison", "Imp", "Petrify",
                                                "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow",
                                                "Stop"))

EarthDragon: Bestiary = Bestiary("Earth Dragon", 53, 28500, 16500, 23, 110,
                                 0, 12, 150, 0, 0, 0,
                                 "X-Potion", "Magus Rod", None,
                                 ("Wind", "Water"), None, None,
                                 ("Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                                  "Stop"))

SkullDragon: Bestiary = Bestiary("Skull Dragon", 62, 32800, 1999, 15, 140,
                                 0, 10, 120, 0, 0, 0,
                                 None, "Muscle Belt", None, ("Fire", "Holy"),
                                 "Poison", None, ("Darkness", "Poison", "Imp",
                                                  "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep",
                                                  "Slow", "Stop"))

HolyDragon: Bestiary = Bestiary("Holy Dragon", 71, 18500, 12000, 13, 110,
                                0, 9, 150, 0, 0, 0,
                                ("Holy Lance", "X-Potion"), None, None,
                                None, "Holy", None, ("Poison", "Imp",
                                                     "Petrify", "Death", "Berserk", "Confusion", "Sleep"))

Gigantaur: Bestiary = Bestiary("Gigantaur", 91, 30000, 4500, 15, 200,
                               200, 18, 200, 200, 1111, 0,
                               None, None, "Fire", None, "Water",
                               None, ("Darkness", "Poison", "Imp", "Petrify", "Death",
                                      "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Leviathan: Bestiary = Bestiary("Leviathan", 91, 32000, 7000, 22, 140, 20,
                               14, 120, 20, 10000, 0,
                               None, None, None, None, "Water",
                               None, ("Darkness", "Poison", "Imp", "Petrify", "Death",
                                      "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Gilgamesh: Bestiary = Bestiary("Gilgamesh", 97, 38000, 3200, 51, 173, 45,
                               8, 212, 30, 0, 0,
                               ("Genji Shield", "Genji Glove"), ("Genji Armor", "Genji Helm"),
                               None, None, None, "Humanoid",
                               ("Darkness", "Poison", "Imp", "Petrify", "Death",
                                "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop")
                               )

Inferno: Bestiary = Bestiary("Inferno", 67, 30800, 9700, 13, 130, 0,
                             10, 145, 0, 0, 0,
                             "Ice Shield", None, None, "Lightning",
                             "Fire", None, ("Poison", "Imp", "Petrify", "Death",
                                            "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

Rahu: Bestiary = Bestiary("Rahu", 69, 8000, 770, 13, 80, 0,
                          10, 190, 0, 0, 0,
                          "Flame Shield", None, None, "Ice",
                          "Lighting", None, ("Darkness", "Poison",
                                             "Imp", "Silence", "Berserk", "Confusion", "Sleep"))

Ketu: Bestiary = Bestiary("Ketu", 67, 11000, 2600, 13, 75, 0,
                          7, 185, 0, 0, 0,
                          "Flame Shield", None, None, "Fire",
                          "Ice", None, ("Darkness", "Poison", "Imp",
                                        "Silence", "Berserk", "Confusion", "Sleep"))

UltimaBuster: Bestiary = Bestiary("Ultima Buster", 67, 55000, 19000, 20, 75,
                                  0, 10, 70, 0, 0, 0,
                                  ("Crystal Orb", "Blood Sword"), None, None,
                                  None, ("Poison", "Wind", "Holy", "Earth", "Water"),
                                  None, ("Poison", "Imp", "Petrify", "Death", "Silence",
                                         "Berserk", "Confusion", "Sleep", "Stop"))

Guardian: Bestiary = Bestiary("Guardian", 67, 60000, 5200, 13, 150, 0,
                              25, 150, 0, 0, 0,
                              ("Ribbon", "Force Armor"), None, None,
                              ("Lightning", "Water"), None, None,
                              ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                               "Confusion", "Sleep", "Stop"))

Doooooom: Bestiary = Bestiary("Fiend", 73, 63000, 4800, 60, 110, 0,
                              9, 160, 0, 0, 0,
                              "Safety Bit", "Mutsunokami", None,
                              "Holy", ("Ice", "Poison"), None,
                              ("Poison", "Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                               "Sleep", "Stop"))

Goddess: Bestiary = Bestiary("Goddess", 68, 44000, 19000, 13, 85, 0,
                             14, 150, 0, 0, 0,
                             "Minvera Bustier", "Excalibur", None,
                             None, ("Lightning", "Holy"), None,
                             ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                              "Confusion", "Sleep", "Slow", "Stop"))

Demon: Bestiary = Bestiary("Demon", 67, 58000, 18900, 15, 180, 0,
                           13, 145, 0, 0, 0,
                           "Red Jacket", "Radiant Lance", None,
                           "Poison", ("Fire", "Wind"), None,
                           ("Poison", "Imp", "Petrify", "Death", "Silence", "Berserk", "Confusion",
                            "Sleep"))

ShortArm: Bestiary = Bestiary("Short Arm", 73, 27000, 10000, 50, 115,
                              10, 10, 155, 0, 0, 0,
                              "Elixir", None, None, "Water",
                              None, None, ("Darkness", "Poison", "Imp", "Petrify",
                                           "Death", "Confusion", "Sleep", "Stop"))

LongArm: Bestiary = Bestiary("Long Arm", 73, 33000, 10000, 35, 110, 5,
                             30, 150, 0, 0, 0,
                             "Elixir", None, None, "Wind",
                             None, None, ("Darkness", "Poison", "Imp",
                                          "Silence", "Confusion", "Sleep", "Slow", "Stop"))

Visage: Bestiary = Bestiary("Visage", 74, 30000, 10000, 63, 140, 10,
                            12, 140, 0, 0, 0,
                            "Elixir", None, "Earth", "Fire",
                            None, "Humanoid", ("Poison", "Imp", "Petrify",
                                               "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Tiger: Bestiary = Bestiary("Tiger", 70, 30000, 10000, 13, 120, 0,
                           7, 153, 0, 0, 0,
                           "Elixir", None, None, "Ice",
                           "Earth", None, ("Darkness", "Imp", "Petrify", "Death",
                                           "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

Machine: Bestiary = Bestiary("Machine", 73, 24000, 10000, 13, 105, 0,
                             10, 153, 0, 0, 0,
                             "Elixir", None, None, "Lightning",
                             None, None, ("Darkness", "Poison", "Imp",
                                          "Petrify", "Silence", "Berserk", "Confusion", "Sleep"))

MagicFinalBoss: Bestiary = Bestiary("Magic", 72, 41000, 10000, 1, 145, 0,
                                    8, 125, 0, 0, 0,
                                    "Elixir", None, None, "Earth",
                                    None, "Humanoid", ("Darkness", "Poison",
                                                       "Imp", "Petrify", "Death", "Berserk", "Confusion", "Sleep",
                                                       "Slow", "Stop"))

PowerFinalBoss: Bestiary = Bestiary("Power", 73, 28000, 10000, 6, 115, 0,
                                    9, 153, 0, 0, 0,
                                    "Elixir", None, None, "Poison",
                                    None, "Humanoid", ("Darkness", "Poison",
                                                       "Imp", "Petrify", "Death", "Silence", "Confusion", "Sleep"))

LadyFinalBoss: Bestiary = Bestiary("Lady", 58, 9999, 10000, 73, 150, 0,
                                   9, 155, 0, 0, 0,
                                   "Ragnarok", None, None, None,
                                   ("Fire", "Ice", "Lightning", "Poison", "Wind", "Holy", "Earth", "Water"),
                                   None,
                                   ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence",
                                    "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

RestFinalBoss: Bestiary = Bestiary("Rest", 71, 40000, 10000, 63, 140, 0,
                                   6, 120, 0, 0, 0,
                                   "Ultima Weapon", None, None, None,
                                   None, "Humanoid", ("Darkness", "Poison", "Imp", "Petrify",
                                                      "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow",
                                                      "Stop"))

FinalKefka: Bestiary = Bestiary("Kefka", 71, 62000, 38000, 80, 117,
                                45, 8, 135, 0, 0, 0,
                                "Megalixir", None, "Poison", None,
                                None, None, ("Darkness", "Zombie", "Poison",
                                             "Vanish", "Imp", "Petrify", "Death", "Silence", "Confuse", "Berserk",
                                             "Sleep", "Slow", "Stop"))

Plague: Bestiary = Bestiary("Plague", 79, 22000, 12000, 31, 130, 250,
                            20, 160, 180, 0, 5000,
                            None, "Angel Brush", None, None,
                            None, None, ("Imp", "Petrify", 'Death', "Confusion"))

FlanPrincess: Bestiary = Bestiary("Flan Princess", 91, 12345, 1000, 13, 250,
                                  0, 15, 100, 0, 11111, 5000,
                                  ("Megalixir", "Super Ball"), "Oborozuki",
                                  ("Poison", "Wind", "Holy", "Earth", "Water"), "Fire",
                                  None, None, ("Darkness", "Poison",
                                               "Imp", "Petrify", "Stop"))

NeslugShell: Bestiary = Bestiary("Neslug", 97, 62000, 62000, 60, 255,
                                 0, 20, 255, 0, 50000, 0,
                                 None, None, None, "Fire",
                                 ("Ice", "Lightning", "Water"), None,
                                 ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                                  "Confusion", "Sleep", "Slow", "Stop"))

NeslugHead: Bestiary = Bestiary("Neslug", 97, 62000, 62000, 50, 180, 50,
                                20, 195, 50, 50000, 0, None,
                                "Gungnir", None, "Fire",
                                ("Ice", "Lightning", "Water"), None,
                                ("Darkness", "Poison", "Imp", "Petrify", "Death", "Silence", "Berserk",
                                 "Confusion", "Sleep", "Slow", "Stop"))

EarthEater: Bestiary = Bestiary("Earth Eater", 97, 36000, 1400, 70, 10, 0,
                                30, 80, 0, 0, 5000,
                                "Teleport Stone", None, None, "Holy",
                                None, None, ("Darkness", "Poison", "Imp",
                                             "Petrify", "Death", "Silence", "Sleep"))

Gargantua: Bestiary = Bestiary("Gargantua", 85, 30000, 1500, 67, 100, 55,
                               0, 100, 0, 0, 5000,
                               None, "Growth Egg", None, "Poison",
                               None, "Humanoid", ("Imp", "Petrify", "Death",
                                                  "Silence", "Stop"))

MalboroMenace: Bestiary = Bestiary("Malboro Menace", 92, 15000, 2000, 13, 144, 0,
                                   9, 109, 0, 0, 5000,
                                   ("Hi-Potion", "Potion"), "Potion", None,
                                   "Fire", ("Ice", "Lightning", "Poison", "Wind", "Holy",
                                            "Earth", "Water"), None,
                                   ("Darkness", "Imp", "Petrify", "Silence", "Berserk", "Confusion",
                                    "Stop"))

AbyssWorm: Bestiary = Bestiary("Abyss Worm", 91, 34000, 60000, 23, 180,
                               0, 10, 150, 0, 0, 5000,
                               "Elixir", "Phoenix Down", ("Fire", "Lightning",
                                                          "Poison", "Wind", "Earth", "Water"), "Holy",
                               "Ice", None, ("Darkness", "Poison", "Imp",
                                             "Petrify", "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow",
                                             "Stop"))

DarkBehemoth: Bestiary = Bestiary("Dark Behemoth", 91, 38000, 9999, 27, 115,
                                  0, 15, 151, 0, 0, 5000,
                                  ("Behemoth Suit", "Phoenix Down"), "Phoenix Down",
                                  None, ("Fire", "Holy"), "Poison", None,
                                  ("Poison", "Imp", "Petrify", "Silence", "Berserk", "Confusion",
                                   "Sleep", "Slow", "Stop"))

RedDragonBonusDungeon: Bestiary = Bestiary("Red Dragon", 97, 59000, 12000, 40,
                                           150, 20, 15, 150, 10,
                                           0, 0, "X-Ether", "Apocalypse",
                                           None, ("Ice", "Water"), "Fire",
                                           None, ("Darkness", "Poison", "Imp", "Petrify",
                                                  "Death", "Silence", "Berserk", "Confusion", "Sleep", "Slow", "Stop"))

BlueDragonBonusDungeon: Bestiary = Bestiary("Blue Dragon", 97, 57000, 16000, 40,
                                            150, 20, 15, 150, 10,
                                            0, 0, "X-Potion", "Save the Queen",
                                            None, "Lightning", "Water",
                                            None, ("Imp", "Petrify", "Death", "Silence",
                                                   "Berserk", "Confusion", "Sleep", "Stop"))

GoldDragonBonusDungeon: Bestiary = Bestiary("Gold Dragon", 97, 60000, 18000, 40,
                                            150, 20, 15, 150, 10,
                                            0, 0, "X-Ether", "Zwill Crossblade",
                                            None, "Water", "Lightning",
                                            None, ("Darkness", "Poison", "Imp", "Petrify",
                                                   "Death", "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

IceDragonBonusDungeon: Bestiary = Bestiary("Ice Dragon", 97, 32000, 20000, 40,
                                           150, 20, 15, 150, 20,
                                           0, 0, None, "Final Trump",
                                           None, "Fire", "Ice",
                                           None, ("Darkness", "Poison", "Imp", "Petrify",
                                                  "Death", "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

StormDragonBonusDungeon: Bestiary = Bestiary("Storm Dragon", 97, 62000, 10000, 40,
                                             150, 200, 12, 150, 80,
                                             0, 0, "Hi-Ether", "Longinus",
                                             None, "Lightning", "Wind",
                                             None, ("Darkness", "Poison", "Imp", "Petrify",
                                                    "Death", "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

EarthDragonBonusDungeon: Bestiary = Bestiary("Earth Dragon", 97, 58000, 24000, 100,
                                             220, 10, 18, 150, 20,
                                             0, 0, "X-Potion", "Godhand",
                                             None, ("Wind", "Water"), "Earth",
                                             None, ("Darkness", "Poison", "Imp", "Petrify",
                                                    "Death", "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

SkullDragonBonusDungeon: Bestiary = Bestiary("Skull Dragon", 97, 61000, 14000, 40,
                                             200, 0, 15, 120, 20,
                                             0, 0, "Holy Water", "Scorpion Tail",
                                             None, ("Fire", "Holy"), "Poison",
                                             None, ("Darkness", "Poison", "Imp", "Petrify",
                                                    "Death", "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

HolyDragonBonusDungeon: Bestiary = Bestiary("Holy Dragon", 97, 55000, 22000, 30,
                                            150, 10, 22, 200, 40,
                                            0, 0, "Elixir", "Zanmato",
                                            None, None, "Holy",
                                            None, ("Darkness", "Poison", "Imp", "Petrify",
                                                   "Death", "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

KaiserDragon: Bestiary = Bestiary("Kaiser Dragon", 97, 327500, 60000, 30,
                                  200, 0, 22, 200, 0,
                                  0, 0, "Celestriad", None,
                                  "???", "???", "???", None,
                                  "???")

OmegaWeapon: Bestiary = Bestiary("Omega Weapon", 97, 65000, 65000, 111,
                                 222, 55, 30, 222, 55,
                                 0, 0, "Megalixir", "Murakumo",
                                 None, None, None, None,
                                 ("Darkness", "Poison", "Imp", "Petrify",
                                  "Death", "Silence", "Berserk", "Confusion", "Sleep", "Stop"))

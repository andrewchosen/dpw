# Data Template for Marvel Characters
class Character(object):
    def __init__(self):
        self.name = ""
        self.real_name = ""
        self.description = ""
        self.alignment = ""
        self.height = ""
        self.weight = 0
        self.powers = ""

    def print_weight(self):
        return str(self.weight) + " lbs"

class Data(object):
    def __init__(self):

        spiderman = Character()
        spiderman.name = "Spider-Man"
        spiderman.real_name = "Peter Parker"
        spiderman.description = "Bitten by a radioactive spider, high school student Peter Parker gained the speed, strength and powers of a spider. Adopting the name Spider-Man, Peter hoped to start a career using his new abilities. Taught that with great power comes great responsibility, Spidey has vowed to use his powers to help people."
        spiderman.alignment = "Hero"
        spiderman.height = "5ft 10in"
        spiderman.weight = 167
        spiderman.powers = "Superhuman Strength, Surface Clinging, Superhuman Agility, and Spider-Senses"

        daredevil = Character()
        daredevil.name = "Daredevil"
        daredevil.real_name = "Matthew Murdock"
        daredevil.description = "Abandoned by his mother, Matt Murdock was raised by his father, boxer 'Battling Jack' Murdock, in Hell's Kitchen. Realizing that rules were needed to prevent people from behaving badly, young Matt decided to study law; however, when he saved a man from an oncoming truck, it spilled a radioactive cargo that rendered Matt blind while enhancing his remaining senses. Under the harsh tutelage of blind martial arts master Stick, Matt mastered his heightened senses and became a formidable fighter."
        daredevil.alignment = "Hero"
        daredevil.height = "6'0"
        daredevil.weight = 200
        daredevil.powers = "Superhuman Senses (except sight)"

        iron_man = Character()
        iron_man.name = "Iron Man"
        iron_man.real_name = "Tony Stark"
        iron_man.description = "Wounded, captured and forced to build a weapon by his enemies, billionaire industrialist Tony Stark instead created an advanced suit of armor to save his life and escape captivity. Now with a new outlook on life, Tony uses his money and intelligence to make the world a safer, better place as Iron Man."
        iron_man.alignment = "Hero"
        iron_man.height = "6'1"
        iron_man.weight = 225
        iron_man.powers = "None; but he has an extremely high IQ which helps him invent and build gadgets and, of course, his Iron Man suits."

        wolverine = Character()
        wolverine.name = "Wolverine"
        wolverine.real_name = 'James "Logan" Howlett'
        wolverine.description = "Born with super-human senses and the power to heal from almost any wound, Wolverine was captured by a secret Canadian organization and given an unbreakable skeleton and claws. Treated like an animal, it took years for him to control himself. Now, he's a premiere member of both the X-Men and the Avengers."
        wolverine.alignment = "Hero"
        wolverine.height = "5'3"
        wolverine.weight = 300
        wolverine.powers = "Cellular Regeneration, Heightened Senses, and his Claws"

        magneto = Character()
        magneto.name = "Magneto"
        magneto.real_name = "Max Eisenhardt"
        magneto.description = ""
        magneto.alignment = "Villain"
        magneto.height = "6'2"
        magneto.weight = 190
        magneto.powers = "Magnetic Field Control & Manipulation"
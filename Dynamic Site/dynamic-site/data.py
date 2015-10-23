# Data Template for Marvel Characters
class Character(object):
    def __init__(self):
        self.url_code = ""
        self.name = ""
        self.real_name = ""
        self.description = ""
        self.alignment = ""
        self.height = ""
        self.weight = 0
        self.powers = ""

    # function to print and format weight
    def print_weight(self):
        return str(self.weight) + " lbs"

# Data object class
class Data(object):
    def __init__(self):
        
        # Data for Spider-Man
        spiderman = Character()
        spiderman.url_code = "spiderman"
        spiderman.name = "Spider-Man"
        spiderman.real_name = "Peter Parker"
        spiderman.description = "Bitten by a radioactive spider, high school student Peter Parker gained the speed, strength and powers of a spider. Adopting the name Spider-Man, Peter hoped to start a career using his new abilities. Taught that with great power comes great responsibility, Spidey has vowed to use his powers to help people. <small>[<a href='http://marvel.com/characters/54/spider-man'>Source</a>]</small>"
        spiderman.alignment = "Hero"
        spiderman.height = "5ft 10in"
        spiderman.weight = 167
        spiderman.powers = "Superhuman Strength, Surface Clinging, Superhuman Agility, and Spider-Senses"
        

        # Data for Daredevil
        daredevil = Character()
        daredevil.url_code = "daredevil"
        daredevil.name = "Daredevil"
        daredevil.real_name = "Matthew Murdock"
        daredevil.description = "Abandoned by his mother, Matt Murdock was raised by his father, boxer 'Battling Jack' Murdock, in Hell's Kitchen. Realizing that rules were needed to prevent people from behaving badly, young Matt decided to study law; however, when he saved a man from an oncoming truck, it spilled a radioactive cargo that rendered Matt blind while enhancing his remaining senses. Under the harsh tutelage of blind martial arts master Stick, Matt mastered his heightened senses and became a formidable fighter. <small>[<a href='http://marvel.com/characters/11/daredevil'>Source</a>]</small>"
        daredevil.alignment = "Hero"
        daredevil.height = "6'0"
        daredevil.weight = 200
        daredevil.powers = "Superhuman Senses (except sight)"

        # Data for Iron Man
        iron_man = Character()
        iron_man.url_code = "iron-man"
        iron_man.name = "Iron Man"
        iron_man.real_name = "Tony Stark"
        iron_man.description = "Wounded, captured and forced to build a weapon by his enemies, billionaire industrialist Tony Stark instead created an advanced suit of armor to save his life and escape captivity. Now with a new outlook on life, Tony uses his money and intelligence to make the world a safer, better place as Iron Man. <small>[<a href='http://marvel.com/characters/29/iron_man'>Source</a>]</small>"
        iron_man.alignment = "Hero"
        iron_man.height = "6'1"
        iron_man.weight = 225
        iron_man.powers = "None; but he has an extremely high IQ which helps him invent and build gadgets and, of course, his Iron Man suits."

        # Data for Wolverine
        wolverine = Character()
        wolverine.url_code = "wolverine"
        wolverine.name = "Wolverine"
        wolverine.real_name = 'James "Logan" Howlett'
        wolverine.description = "Born with super-human senses and the power to heal from almost any wound, Wolverine was captured by a secret Canadian organization and given an unbreakable skeleton and claws. Treated like an animal, it took years for him to control himself. Now, he's a premiere member of both the X-Men and the Avengers. <small>[<a href='http://marvel.com/characters/66/wolverine'>Source</a>]</small>"
        wolverine.alignment = "Hero"
        wolverine.height = "5'3"
        wolverine.weight = 300
        wolverine.powers = "Cellular Regeneration, Heightened Senses, and his Claws"

        # Data for Magneto
        magneto = Character()
        magneto.url_code = "magneto"
        magneto.name = "Magneto"
        magneto.real_name = "Max Eisenhardt"
        magneto.description = "The master of magnetism and one of the most infamous and powerful mutants, possessing mastery over magnetism. He has played many roles in his long life: prisoner, survivor, terrorist, savior, conqueror, teacher, villain, and anti-hero. <small>[<a href='http://www.comicvine.com/magneto/4005-1441/'>Source</a>]</small>"
        magneto.alignment = "Villain"
        magneto.height = "6'2"
        magneto.weight = 190
        magneto.powers = "Magnetic Field Control & Manipulation"
        
        # Compile character objects into array
        self.characters = [spiderman, daredevil, iron_man, wolverine, magneto]

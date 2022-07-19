from operator import itemgetter  # to import itemgetter which sorts the dictionary according to max value
from nltk.corpus import words  # to import the total words available in english language
import random  # ti generate a random number

gen_words = ["aah", "aal", "aas", "aba", "abs", "aby", "ace", "act", "add", "ado", "ads", "adz", "aff", "aft", "aga",
             "age",
             "ago", "ags", "aha", "ahi", "ahs", "aid", "ail", "aim", "ain", "air", "ais", "ait", "ala", "alb", "ale",
             "all",
             "alp", "als", "alt", "ama", "ami", "amp", "amu", "ana", "and", "ane", "ani", "ant", "any", "ape", "apo",
             "app",
             "apt", "arb", "arc", "are", "arf", "ark", "arm", "ars", "art", "ash", "ask", "asp", "ate", "att", "auk",
             "ava",
             "ave", "avo", "awa", "awe", "awl", "awn", "axe", "aye", "ays", "azo", "baa", "bad", "bag", "bah", "bal",
             "bam",
             "ban", "bap", "bar", "bas", "bat", "bay", "bed", "bee", "beg", "bel", "ben", "bes", "bet", "bey", "bib",
             "bid",
             "big", "bin", "bio", "bis", "bit", "biz", "boa", "bob", "bod", "bog", "boo", "bop", "bos", "bot", "bow",
             "box",
             "boy", "bra", "bro", "brr", "bub", "bud", "bug", "bun", "bur", "bus", "but", "buy", "bye", "bys", "cab",
             "cad",
             "cam", "can", "cap", "car", "cat", "caw", "cay", "cee", "cel", "cep", "chi", "cig", "cis", "cob", "cod",
             "cog",
             "col", "con", "coo", "cop", "cor", "cos", "cot", "cow", "coy", "coz", "cru", "cry", "cub", "cud", "cue",
             "cup",
             "cur", "cut", "cwm", "dab", "dad", "dag", "dah", "dak", "dal", "dam", "dan", "dap", "daw", "day", "deb",
             "dee",
             "def", "dei", "del", "den", "des", "dev", "dew", "dex", "dey", "dib", "did", "die", "dif", "dig", "dim",
             "din",
             "dip", "dis", "dit", "dna", "doc", "doe", "dog", "dol", "dom", "don", "dor", "dos", "dot", "dow", "dry",
             "dub",
             "dud", "due", "dug", "duh", "dui", "dun", "duo", "dup", "dux", "dye", "ear", "eat", "eau", "ebb", "ecu",
             "edh",
             "eds", "eek", "eel", "eff", "efs", "eft", "egg", "ego", "eke", "eld", "elf", "elk", "ell", "elm", "els",
             "eme",
             "emf", "ems", "emu", "end", "eng", "ens", "eon", "era", "ere", "erg", "ern", "err", "ers", "ess", "eta",
             "eth",
             "eve", "ewe", "eye", "fab", "fad", "fan", "far", "fas", "fat", "fax", "fay", "fed", "fee", "feh", "fem",
             "fen",
             "fer", "fes", "fet", "feu", "few", "fey", "fez", "fib", "fid", "fie", "fig", "fil", "fin", "fir", "fit",
             "fix",
             "fiz", "flu", "fly", "fob", "foe", "fog", "foh", "fon", "fop", "for", "fou", "fox", "foy", "fro", "fry",
             "fub",
             "fud", "fug", "fun", "fur", "gab", "gad", "gae", "gag", "gal", "gam", "gan", "gap", "gar", "gas", "gat",
             "gay",
             "ged", "gee", "gel", "gem", "gen", "get", "gey", "ghi", "gib", "gid", "gie", "gig", "gin", "gip", "git",
             "gnu",
             "goa", "gob", "god", "goo", "gor", "gos", "got", "gox", "goy", "gul", "gum", "gun", "gut", "guv", "guy",
             "gym",
             "gyp", "had", "hae", "hag", "hah", "haj", "ham", "hao", "hap", "has", "hat", "haw", "hay", "heh", "hem",
             "hen",
             "hep", "her", "hes", "het", "hew", "hex", "hey", "hic", "hid", "hie", "him", "hin", "hip", "his", "hit",
             "hmm",
             "hob", "hod", "hog", "hon", "hop", "hot", "how", "hoy", "hub", "hue", "hug", "huh", "hum", "hun", "hup",
             "hut",
             "hyp", "ice", "ich", "ick", "icy", "ids", "iff", "ifs", "igg", "ilk", "ill", "imp", "ink", "inn", "ins",
             "ion",
             "ire", "irk", "ism", "its", "ivy", "jab", "jag", "jam", "jar", "jaw", "jay", "jee", "jet", "jeu", "jib",
             "jig",
             "jin", "job", "joe", "jog", "jot", "jow", "joy", "jug", "jun", "jus", "jut", "kab", "kae", "kaf", "kas",
             "kat",
             "kay", "kea", "ked", "kef", "keg", "ken", "kep", "kev", "kex", "key", "khi", "kid", "kif", "kin", "kip",
             "kir",
             "kis", "kit", "koa", "kob", "koi", "kop", "kor", "kos", "kue", "kye", "lab", "lac", "lad", "lag", "lam",
             "lap",
             "lar", "las", "lat", "lav", "law", "lax", "lay", "lea", "led", "lee", "leg", "lei", "lek", "les", "let",
             "leu",
             "lev", "lex", "ley", "lez", "lib", "lid", "lie", "lin", "lip", "lis", "lit", "lob", "log", "loo", "lop",
             "lot",
             "low", "lox", "lug", "lum", "luv", "lux", "lye", "mac", "mad", "mae", "mag", "man", "map", "mar", "mas",
             "mat",
             "maw", "max", "may", "med", "meg", "mel", "mem", "men", "met", "mew", "mho", "mib", "mic", "mid", "mig",
             "mil",
             "mim", "mir", "mis", "mix", "moa", "mob", "moc", "mod", "mog", "mol", "mom", "mon", "moo", "mop", "mor",
             "mos",
             "mot", "mow", "mud", "mug", "mum", "mun", "mus", "mut", "myc", "nab", "nae", "nag", "nah", "nam", "nan",
             "nap",
             "naw", "nay", "neb", "nee", "neg", "net", "new", "nib", "nil", "nim", "nit", "nix", "nod", "nog", "noh",
             "nom",
             "noo", "nor", "nos", "not", "now", "nth", "nub", "nun", "nus", "nut", "oaf", "oak", "oar", "oat", "oba",
             "obe",
             "obi", "oca", "oda", "odd", "ode", "ods", "oes", "off", "oft", "ohm", "oho", "ohs", "oil", "oka", "oke",
             "old",
             "ole", "oms", "one", "ono", "ons", "ooh", "oot", "ope", "ops", "opt", "ora", "orb", "orc", "ore", "ors",
             "ort",
             "ose", "oud", "our", "out", "ova", "owe", "owl", "own", "oxo", "oxy", "pac", "pad", "pah", "pal", "pam",
             "pan",
             "pap", "par", "pas", "pat", "paw", "pax", "pay", "pea", "pec", "ped", "pee", "peg", "peh", "pen", "pep",
             "per",
             "pes", "pet", "pew", "phi", "pht", "pia", "pic", "pie", "pin", "pip", "pis", "pit", "piu", "pix", "ply",
             "pod",
             "poh", "poi", "pol", "pom", "poo", "pop", "pot", "pow", "pox", "pro", "pry", "psi", "pst", "pub", "pud",
             "pug",
             "pul", "pun", "pup", "pur", "pus", "put", "pya", "pye", "pyx", "qat", "qis", "qua", "rad", "rag", "rah",
             "rai",
             "raj", "ram", "ran", "rap", "ras", "rat", "raw", "rax", "ray", "reb", "rec", "red", "ree", "ref", "reg",
             "rei",
             "rem", "rep", "res", "ret", "rev", "rex", "rho", "ria", "rib", "rid", "rif", "rig", "rim", "rin", "rip",
             "rob",
             "roc", "rod", "roe", "rom", "rot", "row", "rub", "rue", "rug", "rum", "run", "rut", "rya", "rye", "sab",
             "sac",
             "sad", "sae", "sag", "sal", "sap", "sat", "sau", "saw", "sax", "say", "sea", "sec", "see", "seg", "sei",
             "sel",
             "sen", "ser", "set", "sew", "sha", "she", "shh", "shy", "sib", "sic", "sim", "sin", "sip", "sir", "sis",
             "sit",
             "six", "ska", "ski", "sky", "sly", "sob", "sod", "sol", "som", "son", "sop", "sos", "sot", "sou", "sow",
             "sox",
             "soy", "spa", "spy", "sri", "sty", "sub", "sue", "suk", "sum", "sun", "sup", "suq", "syn", "tab", "tad",
             "tae",
             "tag", "taj", "tam", "tan", "tao", "tap", "tar", "tas", "tat", "tau", "tav", "taw", "tax", "tea", "ted",
             "tee",
             "teg", "tel", "ten", "tet", "tew", "the", "tho", "thy", "tic", "tie", "til", "tin", "tip", "tis", "tod",
             "toe",
             "tog", "tom", "ton", "too", "top", "tor", "tot", "tow", "toy", "try", "tsk", "tub", "tug", "tui", "tun",
             "tup",
             "tut", "tux", "twa", "two", "tye", "udo", "ugh", "uke", "ulu", "umm", "ump", "uns", "upo", "ups", "urb",
             "urd",
             "urn", "urp", "use", "uta", "ute", "uts", "vac", "van", "var", "vas", "vat", "vau", "vav", "vaw", "vee",
             "veg",
             "vet", "vex", "via", "vid", "vie", "vig", "vim", "vin", "vis", "voe", "von", "vow", "vox", "vug", "vum",
             "wab",
             "wad", "wae", "wag", "wan", "wap", "war", "was", "wat", "waw", "wax", "way", "web", "wed", "wee", "wen",
             "wet",
             "wha", "who", "why", "wig", "win", "wis", "wit", "wiz", "woe", "wok", "won", "woo", "wos", "wot", "wow",
             "wry",
             "wud", "wye", "wyn", "xis", "yag", "yah", "yak", "yam", "yap", "yar", "yaw", "yay", "yea", "yeh", "yen",
             "yep",
             "yes", "yet", "yew", "yin", "yip", "yob", "yod", "yok", "yom", "yon", "you", "yow", "yuk", "yum", "yup",
             "zag",
             "zap", "zas", "zax", "zed", "zee", "zek", "zen", "zep", "zig", "zin", "zip", "zit", "zoa", "zoo", "zuz",
             "zzz"]  # to give a 3 lettered word

word_list = words.words()


def rand():  # function which generates a random digit from 0 to 1007
    num1 = random.randint(0, 1007)

    return num1


rand_words = 0  # initialization


def display():
    global rand_words  # used as a global variable

    rand_num = rand()
    print("Enter a word with the letters",
          gen_words[rand_num])  # to print a random 3 lettered word from the list gen_words
    rand_words = gen_words[rand_num]  # assigning to a variable for further use
    return rand_words  # global variable


player1_score = 0
player2_score = 0


def storage(no_of_players, rounds):  # body od the entire game
    global players  # global variable
    global player1_score  # global variable
    global player2_score  # global variable
    print(no_of_players)  # global variable
    dict2 = {}
    dict3 = {}
    player_count = ["player1", "player2", "player3", "player4",
                    "player5"]  # list which holds the key values to be entered into the dictionary
    for i in range(rounds):
        display()  # calling the display function to print 3 lettered word to the console
        for h in range(no_of_players):  # iterates through the total number of players
            key = player_count[h]  # stores key of the player which is playing
            print(player_count[h], "Enter your word:")
            value = input()
            if rand_words in value:  # inputs in the dictionary only if the 3 lettered word is
                # present in the accepted string
                dict2.update({key: value})
                print("Accepted")
            else:  # else it inserts 0 as the value of corresponding key
                value = "0"
                print("Not a word,try harder!")
            dict2.update({key: value})
            for j in dict2:
                key1 = j
                q = dict2[j]
                length = len(q)  # finds length of each values in dict
                value1 = length
                dict3.update({key1: value1})  # updates dictionary
        winner(dict3)  # passes dict 3 to function winner


tot_winner = []


def winner(dictionary):
    global tot_winner
    N = 1
    res = dict(sorted(dictionary.items(), key=itemgetter(1), reverse=True)[:N])  # finding largest value in dict
    for k in res:
        print(k, "Won the round!!!!!\n\n")  # printing the round winner
        tot_winner.append(k)  # appending it to a string for identifying final winner


# program execution starts
players = int(input("Enter the  number of players"))
rounds = 3  # type rounds=int(input("enter the number of rounds")) for variable round length
storage(players, rounds)  # calling the function


def max_occurrences(nums):  # to find the largest among the list
    max_val = 0
    result = nums[0]
    for i in nums:
        occu = nums.count(i)
        if occu > max_val:
            max_val = occu
            result = i
    return result


print("\nCongratulations!  " + max_occurrences(
    tot_winner) + " you won the game")  # largest among the string is the winner

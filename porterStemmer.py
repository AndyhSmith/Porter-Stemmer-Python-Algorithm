import string

class PorterStemmer:
    def __init__ (self):
        self.vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def stem(self, str):
        # Check for zero length
        if len(str) > 0:
            # All charachters must be letters.
            if not str.isalpha():
                return None
        else:
            return None

   
        str = self.step1a(str)
        str = self.step1b(str)
        str = self.step1c(str)
        str = self.step2(str)   
        str = self.step3(str)
        str = self.step4(str)
        str = self.step5a(str)
        return str

    def step1a(self, str):
        # SSES -> SS
        if str[-len("sses"):] == "sses":
            return str[:-len("sses")] + "ss"

        # IES -> I
        if str[-len("ies"):] == "ies":
            return str[:-len("ies")] + "i"

        # SS -> S
        if str[-len("ss"):] == "ss":
            return str[:-len("ss")] + "s"

        # S -> 
        if str[-len("s"):] == "s":
            return str[:-len("s")] + ""
        return str

    def step1b(self, str):
        # (m > 0) EED -> EE
        if str[-len("eed"):] == "eed":
            if len(str[:-len("eed")]) > 0:
                return str[:-len("d")] + ""
            else:
                return str

        # (*v) ED -> 
        elif str[-len("ed"):] == "ed":
            if any (char in self.vowels for char in str[:-len("eed")]):
                return self.step1b2(str[:-len("ed")] + "")

        # (*v) ING ->
        elif str[-len("ing"):] == "ing":
            if any (char in self.vowels for char in str[:-len("ing")]):
                return self.step1b2(str[:-len("ing")] + "")
        return str

    def step1b2(self, str):
        # AT -> ATE
        if str[-len("at"):] == "at":
            return str[:-len("")] + "e"
        # BL -> BLE
        elif str[-len("bl"):] == "bl":
            return str[:-len("")] + "e"
        # IZ -> IZE
        elif str[-len("iz"):] == "iz":
            return str[:-len("")] + "e"
        elif len(str) == 1:
            return str + "e"
        return str

    def step1c(self, str):
        # (*V) Y - I
        if str[-len("y"):] == "y":
            if any (char in self.vowels for char in str[:-len("y")]):
                return str[:-len("y")] + "i"
        return str

    def step2(self, str):
        # ATIONAL -> ATE
        if str[-len("ational"):] == "ational" and len(str[:-len("ional")]) > 0:
            return str[:-len("ional")] + "e"

        # TIONAL -> TION
        elif str[-len("tional"):] == "tional":
            return str[:-len("al")] + ""

        # ENCI -> ENCE
        elif str[-len("enci"):] == "enci":
            return str[:-len("i")] + "e"

        # ANCI -> ANCE
        elif str[-len("anci"):] == "ance":
            return str[:-len("i")] + "e"

        # IZER -> IZE
        elif str[-len("izer"):] == "izer":
            return str[:-len("r")] + ""

        # ABLI -> ABLE
        elif str[-len("abli"):] == "abli":
            return str[:-len("i")] + "e"

        # ENTLI -> ENT
        elif str[-len("entli"):] == "entli":
            return str[:-len("li")] + ""

        # ELI -> E
        elif str[-len("eli"):] == "eli":
            return str[:-len("li")] + ""

        # OUSLI -> OUS
        elif str[-len("ousli"):] == "ousli":
            return str[:-len("li")] + ""

        # IZATION -> IZE
        elif str[-len("ization"):] == "ization":
            return str[:-len("ation")] + "e"

        # ATION -> ATE
        elif str[-len("ation"):] == "ation":
            return str[:-len("ion")] + "e"

        # ATOR -> ATE
        elif str[-len("ator"):] == "ator":
            return str[:-len("or")] + "e"

        # ALISM -> AL
        elif str[-len("alism"):] == "alism":
            return str[:-len("ism")] + ""

        # IVENESS -> IVE
        elif str[-len("iveness"):] == "iveness":
            return str[:-len("ness")] + ""

        # FULNESS -> FUL
        elif str[-len("fulness"):] == "fulness":
            return str[:-len("ness")] + ""

        # OUSNESS -> OUS
        elif str[-len("ousness"):] == "ousness":
            return str[:-len("ness")] + ""

        # ALITII -> AL
        elif str[-len("alitii"):] == "alitii":
            return str[:-len("itii")] + ""

        # IVITI -> IVE
        elif str[-len("iviti"):] == "iviti":
            return str[:-len("iti")] + "e"

        # BILITI -> BLE
        elif str[-len("biliti"):] == "biliti":
            return str[:-len("iliti")] + "le"
        return str

    def step3(self, str):
        # ICATE -> IC
        if str[-len("icate"):] == "icate":
            return str[:-len("ate")] + ""

        # ATIVE -> 
        elif str[-len("ative"):] == "ative":
            return str[:-len("ative")] + ""

        # ALIZE -> AL
        elif str[-len("alize"):] == "alize":
            return str[:-len("ize")] + ""

        # ICITI -> IC
        elif str[-len("iciti"):] == "iciti":
            return str[:-len("iti")] + ""
        
        # ICAL -> IC
        elif str[-len("ical"):] == "ical":
            return str[:-len("al")] + ""

        # FUL -> 
        elif str[-len("ful"):] == "ful":
            return str[:-len("ful")] + ""

        # NESS -> 
        elif str[-len("ness"):] == "ness":
            return str[:-len("ness")] + ""
        return str

    def step4(self, str):
        # AL -> 
        if str[-len("al"):] == "al" and len(str[:-len("al")]) > 1:
            return str[:-len("al")] + ""

        # ANCE -> 
        elif str[-len("ance"):] == "ance" and len(str[:-len("ance")]) > 1:
            return str[:-len("ance")] + ""

        # ENCE ->
        elif str[-len("ence"):] == "ence" and len(str[:-len("ence")]) > 1:
            return str[:-len("ence")] + ""

        # ER -> 
        elif str[-len("er"):] == "er" and len(str[:-len("er")]) > 1:
            return str[:-len("er")] + ""

        # IC -> 
        elif str[-len("ic"):] == "ic" and len(str[:-len("ic")]) > 1:
            return str[:-len("ic")] + ""

        # ABLE -> 
        elif str[-len("able"):] == "able" and len(str[:-len("able")]) > 1:
            return str[:-len("able")] + ""

        # IBLE -> 
        elif str[-len("ible"):] == "ible" and len(str[:-len("ible")]) > 1:
            return str[:-len("ible")] + ""

        # ANT -> 
        elif str[-len("ant"):] == "ant" and len(str[:-len("ant")]) > 1:
            return str[:-len("ant")] + ""

        # EMENT -> 
        elif str[-len("ement"):] == "ement" and len(str[:-len("ement")]) > 1:
            return str[:-len("ement")] + ""

        # MENT -> 
        elif str[-len("ment"):] == "ment" and len(str[:-len("ment")]) > 1:
            return str[:-len("ment")] + ""

        # ENT -> 
        elif str[-len("ent"):] == "ent" and len(str[:-len("ent")]) > 1:
            return str[:-len("ent")] + ""

        # OU -> 
        elif str[-len("ou"):] == "ou" and len(str[:-len("ou")]) > 1:
            return str[:-len("ou")] + ""

        # ISM -> 
        elif str[-len("ism"):] == "ism" and len(str[:-len("ism")]) > 1:
            return str[:-len("ism")] + ""

        # ATE -> 
        elif str[-len("ate"):] == "ate" and len(str[:-len("ate")]) > 1:
            return str[:-len("ate")] + ""

        # ITI -> 
        elif str[-len("iti"):] == "iti" and len(str[:-len("iti")]) > 1:
            return str[:-len("iti")] + ""

        # OUS -> 
        elif str[-len("ous"):] == "ous" and len(str[:-len("ous")]) > 1:
            return str[:-len("ous")] + ""

        # IVE -> 
        elif str[-len("ive"):] == "ive" and len(str[:-len("ive")]) > 1:
            return str[:-len("ive")] + ""

        # IZE -> 
        elif str[-len("ize"):] == "ize" and len(str[:-len("ize")]) > 1:
            return str[:-len("ize")] + ""
        return str

    def step5a(self, str):
        # GU -> GUE
        if str[-len("gu"):] == "gu" and len(str[:-len("gu")]) > 1:
            return str[:] + "e"
        return str


        
 
ps = PorterStemmer()
words = ["argue", "argued", "argues", "arguing", "argus", "argument", "arguments", "argument"]
for word in words:
    newWord = ps.stem(word)
    print(newWord)

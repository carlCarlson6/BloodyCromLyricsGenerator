from common.TextCleanner import TextCleanner

class DataLoader:
    def __init__(self):
        self.Text = str
        self.UniqueCharacters = tuple
        self.CharactersDictionary = dict

    def LoadData(self, TextFileName: str):
        text = self.GetText(TextFileName)
        uniqueCharacters = self.GetUniqueCharacters(text)
        charactersDictionary = self.GetCharactersDictionary(text)
        return text, uniqueCharacters, charactersDictionary

    def GetText(self, TextFileName):
        textCleanner = TextCleanner()
        self.Text = textCleanner.CleanText(self.__LoadTxtFile(TextFileName))
        return self.Text

    def __LoadTxtFile(self, TextFileName: str) -> str:
        with open(TextFileName, 'r') as textFile:
            text = textFile.read()
            textFile.close()
        return text

    def GetUniqueCharacters(self, Text: str) -> tuple:
        self.UniqueCharacters = tuple(set(Text))
        return self.UniqueCharacters

    def GetCharactersDictionary(self, Text: str) -> dict:
        uniqueCharacters = self.GetUniqueCharacters(Text)
        self.CharactersDictionary = {}
        self.CharactersDictionary['Int2Char'] = dict(enumerate(uniqueCharacters))
        self.CharactersDictionary['Char2Int'] = {character: integer for integer, character in self.CharactersDictionary['Int2Char'].items()}
        return self.CharactersDictionary
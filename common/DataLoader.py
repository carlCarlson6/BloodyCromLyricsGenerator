from common.TextCleanner import TextCleanner

class DataLoader:
    def __init__(self, TextFileName = None):
        self.Text = str
        self.UniqueCharacters = tuple
        self.CharactersDictionary = dict

        if TextFileName is not None:
            self.Text, self.UniqueCharacters, self.CharactersDictionary = self.__LoadData(TextFileName)


    def GetText(self, TextFileName):
        text = TextCleanner.CleanText(self.__LoadTxtFile(TextFileName))
        return text

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

        int2Char = dict(enumerate(uniqueCharacters))
        char2Int = {
            character: integer 
            for integer, character in int2Char.items()
        }

        charactersDictionary = {}
        charactersDictionary['Int2Char'] = int2Char
        charactersDictionary['Char2Int'] = char2Int
        
        return charactersDictionary

    def __LoadData(self, TextFileName: str):
        text = self.GetText(TextFileName)
        uniqueCharacters = self.GetUniqueCharacters(text)
        charactersDictionary = self.GetCharactersDictionary(text)

        return text, uniqueCharacters, charactersDictionary
class Tokenizer:
    
    def EncodeText(self, Text: str, Char2IntDictionary: dict) -> list:
        encodedText = [Char2IntDictionary[character] for character in Text]
        return encodedText

    def EncodeAsOneHot(self, EncodedText: str) -> list:
        numberUniqueCharacters = len(set(EncodedText))
        
        oneHotEncodedText = []
        for encodedCharacter in EncodedText:
            oneHotVector = [0]*numberUniqueCharacters
            oneHotVector[encodedCharacter] = 1
            oneHotEncodedText.append(oneHotVector)

        return oneHotEncodedText

    def Tokenize(self, Text):
        pass
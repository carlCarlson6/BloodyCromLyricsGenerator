import numpy

class Tokenizer:
    
    def EncodeText(self, Text: str, Char2IntDictionary: dict) -> numpy.array:
        encodedText = numpy.array([Char2IntDictionary[character] for character in Text])
        return encodedText

    def EncodeAsOneHot(self, EncodedText: numpy.array, NumberLabels: int) -> list:
        oneHotEncodedText = numpy.zeros((EncodedText.size, NumberLabels), dtype=numpy.float32)
        oneHotEncodedText[numpy.arange(oneHotEncodedText.shape[0]), EncodedText.flatten()] = 1
        oneHotEncodedText = oneHotEncodedText.reshape((*EncodedText.shape, NumberLabels))
        return oneHotEncodedText
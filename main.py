from common import DataLoader
from Core import Tokenizer

dataLoader = DataLoader()
dataLoader.LoadData(TextFileName='Data\\BloodyCromLyrics.txt')

tokenizer = Tokenizer()
encodedText = tokenizer.EncodeText(Text=dataLoader.Text, Char2IntDictionary=dataLoader.CharactersDictionary['Char2Int'])
oneHotEncodedText = tokenizer.EncodeAsOneHot(EncodedText=encodedText)

k = 0
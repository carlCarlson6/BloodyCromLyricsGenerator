from common import DataLoader
from Core import Tokenizer, BatchManager

dataLoader = DataLoader()
dataLoader.LoadData(TextFileName='Data\\BloodyCromLyrics.txt')

tokenizer = Tokenizer()
encodedText = tokenizer.EncodeText(Text=dataLoader.Text, Char2IntDictionary=dataLoader.CharactersDictionary['Char2Int'])
oneHotEncodedText = tokenizer.EncodeAsOneHot(EncodedText=encodedText, NumberLabels=len(dataLoader.UniqueCharacters))

batchManager = BatchManager()
batches = batchManager.GetBatches(encodedText, 8, 50)
x, y = next(batches)

k = 0
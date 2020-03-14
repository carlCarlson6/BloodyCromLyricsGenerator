import common
import NN
import torch

dataLoader = common.DataLoader(TextFileName='Data\\BloodyCromLyrics.txt')

tokenizer = NN.Tokenizer()
encodedText = tokenizer.EncodeText(Text=dataLoader.Text, Char2IntDictionary=dataLoader.CharactersDictionary['Char2Int'])
oneHotEncodedText = tokenizer.EncodeAsOneHot(EncodedText=encodedText)

k = 0
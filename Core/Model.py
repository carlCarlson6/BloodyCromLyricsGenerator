from torch import nn
import torch


class CharModel(nn.Module):
    def __init__(self, Tokens, CharactersDictionary, NumberHidden=256, NumberLayers=2, DropProb=0.5, LearnRate=0.001):
        super().__init__()

        self.TrainOnGpu = torch.cuda.is_available()

        self.DropProb = DropProb
        self.NumberLayers = NumberLayers
        self.NumberHidden = NumberHidden
        self.LearnRate = LearnRate

        self.Characters = Tokens
        self.CharactersDictionary = CharactersDictionary

        self.LSTM = nn.LSTM(len(self.Characters), NumberHidden, NumberLayers, dropout=DropProb, batch_first=True)
        self.Dropout = nn.Dropout(DropProb)
        self.FullyConnect = nn.Linear(NumberHidden, len(self.Characters))

    def forward(self, features, hidden):
        recurrentOutput, hidden = self.LSTM(features, hidden)
        
        output = self.Dropout(recurrentOutput)
        output = output.contiguous().view(-1, self.NumberHidden)
        output = self.FullyConnect(output)

        return output, hidden

    def InitHidden(self, BatchSize):
        weight = next(self.parameters()).data

        if(self.TrainOnGpu):
            hidden = (
                weight.new(self.n_layers, BatchSize, self.n_hidden).zero_().cuda(), 
                weight.new(self.n_layers, BatchSize, self.n_hidden).zero_().cuda()
            )
        else:
            hidden = (
                weight.new(self.n_layers, BatchSize, self.n_hidden).zero_(),
                weight.new(self.n_layers, BatchSize, self.n_hidden).zero_()
            )

        return hidden
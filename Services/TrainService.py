import torch
from torch import nn

class TrainService:
    @staticmethod
    def Train(net, data, batchManager, epochs=10, BatchSize=10, SequenceLength=50, LearnRate=0.001, clip=5, valFrac=0.1, printEvery=10):
        net.train()

        optimizer = torch.optim.Adam(net.parameters(), lr=LearnRate)
        criterion = nn.CrossEntropyLoss()

        valIdx = int(len(data)*(1-valFrac))
        data, valData = data[: valIdx], data[valIdx:]

        if(net.TrainOnGpu):
            net.cuda()
        
        counter = 0
        numberCharacters = len(net.Characters)

        for epoch in range(epochs):
            hidden = net.InitHidden(BatchSize)

            for features, targets in batchManager.GetBatches(data, BatchSize, SequenceLength):
                counter += 1
                

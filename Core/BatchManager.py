import numpy

class BatchManager:
    def GetBatches(self, Data, BatchSize, SequenceLength):
        totalBatchSize = BatchSize*SequenceLength
        numberBatches = len(Data)//totalBatchSize

        Data = Data[:numberBatches * totalBatchSize]
        Data = Data.reshape((BatchSize, -1))

        for n in range(0, Data.shape[1], SequenceLength):
            features = Data[:, n:+SequenceLength]
            targets = numpy.zeros_like(features)

            try:
                targets[:, :-1], targets[:, -1] = features[:, 1:], Data[:, n+SequenceLength]
            except IndexError:
                targets[:, :-1], targets[:, -1] = features[:, 1:], Data[:, 0]
            
            yield features, targets
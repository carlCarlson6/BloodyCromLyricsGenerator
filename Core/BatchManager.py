import numpy

class BatchManager:
    def GetBatches(self, Data, BatchSize, SequenceLength):
        totalBatchSize = BatchSize*SequenceLength
        numberBatches = len(Data)//totalBatchSize

        Data = Data[:numberBatches * totalBatchSize]
        Data = Data.reshape((BatchSize, -1))

        for n in range(0, Data.shape[1], SequenceLength):
            x = Data[:, n:+SequenceLength]
            y = numpy.zeros_like(x)
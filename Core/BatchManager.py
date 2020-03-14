class BatchManager:
    def GetBatches(self, Data, BatchSize, SequenceLength):
        totalBatchSize = BatchSize*SequenceLength
        numberBatches = len(Data)//totalBatchSize

        
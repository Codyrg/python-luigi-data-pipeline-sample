import luigi
import numpy as np

class GenerateZerosTask(luigi.Task):
    """A task that generates a NumPy array of zeros"""
    shape = luigi.TupleParameter()

    def output(self):
        return luigi.LocalTarget('data/zeros.csv')

    def run(self):
        zeros_array = np.zeros(self.shape)
        np.savetxt(self.output().path, zeros_array, delimiter=',')

class AddOneTask(luigi.Task):
    """A task that adds 1 to every element in a NumPy array"""
    shape = luigi.TupleParameter()

    def requires(self):
        return GenerateZerosTask(shape=self.shape)

    def output(self):
        return luigi.LocalTarget('data/ones.csv')

    def run(self):
        zeros_array = np.loadtxt(self.input().path, delimiter=',')
        ones_array = zeros_array + 1
        np.savetxt(self.output().path, ones_array, delimiter=',')

class AddRandomTask(luigi.Task):
    """A task that adds a random number to every element in a NumPy array"""
    shape = luigi.TupleParameter()

    def requires(self):
        return AddOneTask(shape=self.shape)

    def output(self):
        return luigi.LocalTarget('data/random.csv')

    def run(self):
        ones_array = np.loadtxt(self.input().path, delimiter=',')
        random_array = ones_array + np.random.rand(*self.shape)
        np.savetxt(self.output().path, random_array, delimiter=',')

if __name__ == '__main__':
    luigi.build([AddRandomTask(shape=(10, 10))])

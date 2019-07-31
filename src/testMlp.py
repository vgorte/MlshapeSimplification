import unittest
import mlp
import numpy as np

class test_mlp(unittest.TestCase):
    def test_loading(self):
        m = mlp.mlp(np.random.randn(100, 5), np.random.randn(100, 1), 10, 5,outtype='softmax')
        m.saveModel("../assets/blobs/testModel.pkl")

        m2 = mlp.mlp.loadModel("../assets/blobs/testModel.pkl")
        self.assertEqual(m.nhidden, m2.nhidden)
        self.assertEqual(np.equal(m.weights1, m2.weights1).mean(), 1)


if __name__=="__main__":
    unittest.main()
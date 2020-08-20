from tqdm import tqdm
import numpy as np

class KNNClassifier:
  def __init__(self, k=3):
    if isinstance(k, int) and k > 0:
      self.__k = k
    else:
      raise ValueError(F"Please provide a valid k={k}")

  def fit(self, x, y):
    if x.shape[0] == y.shape[0]:
      self.__x = x
      self.__y = y
    else:
      raise ValueError(
          F"The dimensions for the x and y is not macthcing, {x.shape[0]} == {y.shape[0]}")

  def predict(self, x):
    preds = []

    for sample in tqdm(x):
      # Calculating the distance between the input point and training points
      dist = [np.linalg(sample, x_train) for x_train in self.__x]

      # Sorting based on the dist
      k_samples = np.argsort(dist)[:self.k]

      # predicting the labels
      k_labels = [self.y[i][0] for i in k_samples]

      preds.append(k_labels)

  def accuracy(self, x, y):
    assert X.shape[0] == y.shape[0], "Equal number of samples and labels expected"

    labels = self.predict(X)

    total = 0
    correct = 0

    for i in range(len(labels)):
      total += 1

      if labels[i] == y[i]:
        correct += 1

    print('\n\nAccuracy {}%'.format(correct / total * 100))

    return correct / total * 100

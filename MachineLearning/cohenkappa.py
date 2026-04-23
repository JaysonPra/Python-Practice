import numpy as np
from sklearn.metrics import cohen_kappa_score, confusion_matrix

y_pred = np.random.randint(0, 2, size=100)
y_true = np.random.randint(0, 2, size=100)

kappa = cohen_kappa_score(y_true, y_pred)
confusion = confusion_matrix(y_true, y_pred)
print(kappa, "\n", confusion)


from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import numpy as np


def confusion_matrix_scorer(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred, labels = [0, 1])
    
    return {'tn': cm[0, 0], 'fp': cm[0, 1],
            'fn': cm[1, 0], 'tp': cm[1, 1]}

# function to compute the predicted acceptance rate for a sub-population
# def Statistical_parity(y_pred):
#     PAR_F =[]
#     for row in y_pred:
#         x = np.count_nonzero(row == 1)
#         result = x/len(row)
#         PAR_F.append(result)
#     PAR_F_mean = np.mean(PAR_F, axis=0)
#     return PAR_F_mean

def Statistical_parity(y_pred):
    
    x= np.count_nonzero(y_pred == 1)
    result = x / len(y_pred)
    return result



def Metric_disparity(x, y):
    return x - y

# def Equal_opportunity(cm):
#     TPR_mean = []
#     for row in cm:
#         TP = row['tp']
#         FN = row['fn']
#         TPR = TP/float(TP+FN)
#     TPR_mean.append(TPR)
#     return np.mean(TPR_mean, axis=0)

def Equal_opportunity(cm):
    TP = cm['tp']
    FN = cm['fn']
    return TP/float(TP+FN)


# def Predictive_equality(cm):
#     FPR_mean = []
#     for row in cm:
#         FP = row['fp']
#         TN = row['tn']
#         FPR = FP/float(FP+TN) 
#     FPR_mean.append(FPR)
#     return np.mean(FPR_mean, axis=0)
def Predictive_equality(cm):
    FP = cm['fp']
    TN = cm['tn']
    return FP/float(FP+TN)

def Treatment_equality(cm):
    TE_mean = []
    for row in cm:
        FP = row['fp']
        FN = row['fn']
        TE = FN/float(FP)
        TE_mean.append(TE)
    return np.mean(TE_mean, axis=0)

# def Overall_accuracy(y_test, y_pred):
#     OA_mean = []
#     for (row_test,row_pred) in zip(y_test, y_pred):
#         accuracy = accuracy_score(row_test, row_pred)
#         OA_mean.append(accuracy)
#     return np.mean(OA_mean, axis=0)

def Overall_accuracy(y_test, y_pred):
    return accuracy_score(y_test, y_pred)

def Predictive_rate_parity(y_test,y_pred):
    precision_mean = []
    for (row_test,row_pred) in zip(y_test,y_pred):
        precision = precision_score(row_test, row_pred)
        precision_mean.append(precision)
    return np.mean(precision_mean, axis=0)

def CSD(x,y,z,w):
    return ((x-y) + (z-w))/2

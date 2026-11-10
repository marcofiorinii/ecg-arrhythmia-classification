from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

# This file is used to collect functions that are gonna be used for the model training. 
# The first function standardizes the three sets based on the training set.
# Remember that StandardScaler scales data column by column.
# 
# The second function does the same but it also applies pca to the datasets. 
#
# The third function collapses the labels into aami classes. 

def standardize_data(X_train, X_val, X_test):
    """
    This function takes as input training, validation and test sets and standardize them using 
    StandardScaler fitted on the training set.
    """

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_val_scaled = scaler.transform(X_val)

    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_val_scaled, X_test_scaled

def standardize_and_pca(X_train, k, X_val, X_test):
    """
    Standardize the features and apply PCA, keeping the first k
    principal components.

    Both StandardScaler and PCA are fitted using only the training set.
    """

    X_train_scaled, X_val_scaled, X_test_scaled = standardize_data(X_train, X_val, X_test)

    pca = PCA(n_components=k)

    X_train_pca = pca.fit_transform(X_train_scaled)

    X_val_pca = pca.transform(X_val_scaled)

    X_test_pca = pca.transform(X_test_scaled)

    return X_train_pca, X_val_pca, X_test_pca

def group_aami_classes(y):
    """
    This function takes as input a vector of labels (from 0 to 14) and maps it into the aami standard. 
    """

    # Original classes 0-14 -> AAMI classes 0-4
    # AAMI: 0=N, 1=S, 2=V, 3=F, 4=Q
    mapping = np.array([
        0,  # 0: N  -> N
        4,  # 1: /  -> Q
        0,  # 2: L  -> N
        0,  # 3: R  -> N
        0,  # 4: e  -> N
        0,  # 5: j  -> N
        1,  # 6: A  -> S
        1,  # 7: a  -> S
        1,  # 8: J  -> S
        1,  # 9: S  -> S
        2,  # 10: E -> V
        3,  # 11: F -> F
        2,  # 12: V -> V
        4,  # 13: f -> Q
        4   # 14: Q -> Q
    ])

    return mapping[y.astype(int)]

def raw_pca(X_train, k, X_val, X_test):
    """
    Apply PCA without standardization, fitting only on the training set.

    k: number of components (integer) or fraction of variance to retain
       (float between 0 and 1).
    """
    pca = PCA(n_components=k, svd_solver="full")

    X_train_pca = pca.fit_transform(X_train)
    X_val_pca = pca.transform(X_val)
    X_test_pca = pca.transform(X_test)

    return X_train_pca, X_val_pca, X_test_pca

def fft_data(X_train, X_val, X_test):
    """
    Compute the FFT of each sample and concatenate its real and
    imaginary parts as features. No standardization is applied.
    """
    train_fft = np.fft.rfft(X_train, axis=1)
    val_fft = np.fft.rfft(X_val, axis=1)
    test_fft = np.fft.rfft(X_test, axis=1)

    X_train_fft = np.concatenate(
        (train_fft.real, train_fft.imag), axis=1
    )
    X_val_fft = np.concatenate(
        (val_fft.real, val_fft.imag), axis=1
    )
    X_test_fft = np.concatenate(
        (test_fft.real, test_fft.imag), axis=1
    )

    return X_train_fft, X_val_fft, X_test_fft

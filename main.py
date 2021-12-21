from datasets import load_searches_v2
from classifier_searches import fit_and_predict, calculate_base_score
import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier


X, Y = load_searches_v2()

X_train, X_validate, X_test = np.split(X, [int(.8*len(X)), int(.9*len(X))])
y_train, y_validate, y_test = np.split(Y, [int(.8*len(Y)), int(.9*len(Y))])

model_MultinomialNB = MultinomialNB()
resultado_MultinomialNB = fit_and_predict('MultinomialNB', model_MultinomialNB, X_train, X_test, y_train, y_test)

model_AdaBoostClassifier = AdaBoostClassifier()
resultado_AdaBoostClassifier = fit_and_predict('AdaBoostClassifier', model_AdaBoostClassifier, X_train, X_test, y_train, y_test)

if resultado_MultinomialNB > resultado_AdaBoostClassifier:
    vencedor = model_MultinomialNB
else:
    vencedor = model_AdaBoostClassifier
    
resultado = vencedor.predict(X_validate)
acertos = (resultado == y_validate)

total_de_acertos = sum(acertos)
total_de_elementos = len(X_validate)
taxa_de_acerto = 100.0 * total_de_acertos/total_de_elementos

print(f'score in real world of winner algorithm (validation data): {round(taxa_de_acerto,2)}%')           
print(f'base score: {calculate_base_score(y_validate)}%')
print(f'number of validations: {len(X_validate)}')
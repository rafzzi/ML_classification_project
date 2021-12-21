from collections import Counter

def fit_and_predict(name, model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)

    result = model.predict(X_test)

    successes = (result == y_test)
    total_successes = sum(successes)
    total_elements = len(X_test)
    score = 100.0 * total_successes/total_elements

    print(f'score of {name}: {round(score,2)}%')
    
    return score

def calculate_base_score(y_validate):
    
    # Calculate score considering all guesses equal
    # to most frequent classification
    
    base_successes = max(Counter(y_validate).values())
    base_score = base_successes / len(y_validate) * 100
    
    return round(base_score,2)

def serialization(model):
    import pickle
    
    pickle_file = open('pickle_search.txt', 'wb')
    pickle.dump(model, pickle_file)
    pickle_file.close



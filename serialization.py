# Project serialization

def load_and_test_project(X_test, y_test):
    import pickle

    pickle_file = open('pickle_search.txt', 'rb')
    model = pickle.load(pickle_file)
    pickle_file.close()

    result = model.predict(X_test)
    diff = result - y_test

    successes = [d for d in diff if d == 0]

    total_successes = len(successes)
    total_elements = len(X_test)
    score = 100.0 * total_successes/total_elements

    print(f'score: {round(score,2)}%')
    print(f'number of elements: {len(X_test)}')
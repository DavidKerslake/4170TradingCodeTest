import numpy as np


def matrix_max(M):
    max_value_index = np.argmax(M, axis=1)
    max_values = M[np.arange(len(M)), max_value_index].reshape((-1, 1))
    # Subtract largest value in each row
    original = M.copy()
    M -= max_values
    assignment_matrix = get_assignment_matrix(M)
    if assignment_matrix[np.arange(len(M)), max_value_index].all():
        return int(sum(max_values))

    row_marks = ~assignment_matrix.any(axis=1)
    column_marks = np.zeros(len(M), dtype=bool)
    column_marks[max_value_index[row_marks]] = True
    for row in range(len(M)):
        row_marks[row] = np.array_equal(column_marks, assignment_matrix[row, :]) or row_marks[row]

    new_max_value = np.amax(M[row_marks.reshape((-1, 1)) & ~column_marks])
    M[row_marks.reshape((-1, 1)) & ~column_marks] -= new_max_value
    M[~row_marks.reshape((-1, 1)) & column_marks] += new_max_value
    max_value_index = np.argmax(M, axis=1)
    max_values = original[np.arange(len(M)), max_value_index].reshape((-1, 1))

    while ~assignment_matrix[np.arange(len(M)), max_value_index].all():

        assignment_matrix = get_assignment_matrix(M)
        print(assignment_matrix)
        max_value_index = np.argmax(M, axis=1)
        row_marks = ~assignment_matrix.any(axis=1)
        column_marks = np.zeros(len(M), dtype=bool)
        column_marks[max_value_index[row_marks]] = True
        for row in range(len(M)):
            row_marks[row] = np.array_equal(column_marks, assignment_matrix[row, :]) or row_marks[row]

        new_max_value = np.amax(M[row_marks.reshape((-1, 1)) & ~column_marks])
        print(new_max_value, row_marks, column_marks)
        M[row_marks.reshape((-1, 1)) & ~column_marks] -= new_max_value
        M[~row_marks.reshape((-1, 1)) & column_marks] += new_max_value

        max_values = original[np.arange(len(M)), max_value_index].reshape((-1, 1))
        print(M, max_value_index, max_values)
    return int(sum(max_values))


def get_assignment_matrix(M):
    max_value_index = np.argmax(M, axis=1)
    assignment_matrix = np.zeros(shape=M.shape, dtype=bool)
    for row in range(len(M)):
        if row > 0:
            if assignment_matrix[:, max_value_index[row]].any():
                pass
            else:
                assignment_matrix[row, max_value_index[row]] = True
        else:
            assignment_matrix[row, max_value_index[row]] = True
    return assignment_matrix


if __name__ == '__main__':
    M = np.array([[7, 53, 183, 439, 863], [497, 383, 563, 79, 973], [287, 63, 343, 169, 583],
                  [627, 343, 773, 959, 943], [767, 473, 103, 699, 303]])
    print(matrix_max(M))

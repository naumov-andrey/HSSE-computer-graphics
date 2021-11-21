import pandas as pd

current_iteration = 0
max_iteration = 1000

points_shape = (7, 3, 3)

end_points = pd.read_csv('./data/lab3/end_control_points.csv').to_numpy().reshape(points_shape)
begin_points = pd.read_csv('./data/lab3/begin_control_points.csv').to_numpy().reshape(points_shape)


def calculate_points(progress):
    return [[[begin_points[i][j][k] + progress * (end_points[i][j][k] - begin_points[i][j][k])
              for k in range(points_shape[2])]
             for j in range(points_shape[1])]
            for i in range(points_shape[0])]

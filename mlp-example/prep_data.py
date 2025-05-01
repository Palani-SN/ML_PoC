import pandas as pd
import random
import math

# Function to check if a point is inside the sphere


def is_inside_sphere(point, center, radius):
    return (sum((p - c) ** 2 for p, c in zip(point, center)) < radius ** 2)


def random_point_on_custom_sphere(center, radius):
    u = random.random()
    v = random.random()

    theta = 2 * math.pi * u
    phi = math.acos(2 * v - 1)

    x = math.sin(phi) * math.cos(theta)
    y = math.sin(phi) * math.sin(theta)
    z = math.cos(phi)

    # Scale by radius and shift by center
    point = (
        center[0] + radius * x,
        center[1] + radius * y,
        center[2] + radius * z
    )

    return list(point)


class DataGenerator:

    cols = {
        'P': (-10, 10),
        'O': (-10, 10),
        'R': (0, 100),
    }

    def __init__(self, file_name, num_rows):
        rows_inside = []
        rows_surface = []
        rows_outside = []
        while True:  # Generate 100 random points
            point = [random.uniform(*self.cols['P']) for _ in range(3)]
            center = [random.uniform(*self.cols['O']) for _ in range(3)]
            radius = random.uniform(*self.cols['R'])
            in_vs_out = bool(is_inside_sphere(point, center, radius))
            # Ensure we have enough points inside the sphere
            if in_vs_out and len(rows_inside) < int(num_rows / 3):
                # print('in')
                rows_inside.append({
                    'px': point[0],
                    'py': point[1],
                    'pz': point[2],
                    'ox': center[0],
                    'oy': center[1],
                    'oz': center[2],
                    'rd': radius,
                    'class': 0,
                })
            # Ensure we have enough points outside the sphere
            elif not in_vs_out and len(rows_outside) < int(num_rows / 3):
                # print('out')
                rows_outside.append({
                    'px': point[0],
                    'py': point[1],
                    'pz': point[2],
                    'ox': center[0],
                    'oy': center[1],
                    'oz': center[2],
                    'rd': radius,
                    'class': 2,
                })
            elif len(rows_surface) < int(num_rows / 3):
                # print('surface')
                point = random_point_on_custom_sphere(center, radius)
                rows_surface.append({
                    'px': point[0],
                    'py': point[1],
                    'pz': point[2],
                    'ox': center[0],
                    'oy': center[1],
                    'oz': center[2],
                    'rd': radius,
                    'class': 1,
                })
            else:
                if len(rows_inside) >= int(num_rows / 3) and len(rows_outside) >= int(num_rows / 3) and len(rows_surface) >= int(num_rows / 3):
                    break
                else:
                    continue

        self.create_dataframe(
            file=file_name,
            rows=rows_inside[0:int(num_rows/3)] +
            rows_outside[0:int(num_rows/3)] +
            rows_surface[0:int(num_rows/3)]
        )
        print("Dataframe created successfully!")

    def create_dataframe(self, file, rows):
        dataframe = pd.DataFrame(rows)
        print(dataframe.head())
        dataframe.to_csv(file, index=False)
        return dataframe


if __name__ == "__main__":
    dat_gen = DataGenerator(file_name='train-data.csv', num_rows=10000)
    dat_gen = DataGenerator(file_name='eval-data.csv', num_rows=3000)

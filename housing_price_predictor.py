# Nathan Sanchez
# Housing Price Prediction Model
#
# Learns from housing data and uses the trained weights
# to estimate the price of a house.

import csv
from random import uniform


# Read housing data from CSV into a 2D list.
with open("Housing.csv", newline="") as file:
    reader = csv.reader(file)
    data = [row for row in reader]


# Convert categorical values into numbers.
for i, row in enumerate(data):
    if i == 0:
        continue

    # Convert yes/no columns to 1/0.
    for col in [5, 6, 7, 8, 9, 11]:
        value = row[col].strip().lower()

        if value == "yes":
            row[col] = 1
        elif value == "no":
            row[col] = 0

    # Convert furnishing status to a numeric value.
    furniture = row[12].strip().lower()

    if furniture == "furnished":
        row[12] = 0
    elif furniture == "semi-furnished":
        row[12] = 1
    elif furniture == "unfurnished":
        row[12] = 2


# Convert numeric strings into ints or floats.
for i, row in enumerate(data):
    for j, value in enumerate(row):
        try:
            number = float(value)

            if number.is_integer():
                data[i][j] = int(number)
            else:
                data[i][j] = number

        except (ValueError, TypeError):
            pass


# Move house price from the first column to the last column.
for row in data:
    price = row.pop(0)
    row.append(price)


# Remove the CSV header.
data = data[1:]


# Scale area values to make training more manageable.
for row in data:
    row[0] = row[0] / 10000


# Predict a value using the current weights.
def predict(row, weights):
    prediction = weights[-1]  # Bias

    for i in range(len(row) - 1):
        prediction += row[i] * weights[i]

    return prediction


# Train the prediction model.
def train(train_data, num_epochs, learning_rate):
    weights = [
        uniform(-1, 1)
        for _ in range(len(train_data[0]))
    ]

    for epoch in range(num_epochs):
        total_error = 0
        within_margin = 0

        for row in train_data:
            actual = row[-1]
            prediction = predict(row, weights)

            # Calculate percentage error.
            if actual != 0:
                relative_error = abs(prediction - actual) / abs(actual)
            else:
                relative_error = abs(prediction - actual)

            # Update weights if prediction is outside the ±5% margin.
            if relative_error > 0.05:
                error = actual - prediction

                for i in range(len(weights) - 1):
                    weights[i] += learning_rate * error * row[i]

                weights[-1] += learning_rate * error
                total_error += abs(error)

            else:
                within_margin += 1

        accuracy = within_margin / len(train_data) * 100
        average_error = total_error / len(train_data)

        print(
            f"Epoch {epoch + 1}: "
            f"within ±5% margin = {accuracy:.2f}%, "
            f"Avg Error = {average_error:.4f}"
        )

    return weights


# Train the model.
weights = train(
    data,
    num_epochs=1000,
    learning_rate=0.02
)


# Get information about a house from the user.
area = float(input("Area: "))
bedrooms = float(input("Bedrooms: "))
bathrooms = float(input("Bathrooms: "))
stories = float(input("Stories: "))
mainroad = float(input("Main road? (1=yes, 0=no): "))
guestroom = float(input("Guest room? (1=yes, 0=no): "))
basement = float(input("Basement? (1=yes, 0=no): "))
hotwaterheating = float(input("Hot water heating? (1=yes, 0=no): "))
airconditioning = float(input("Air conditioning? (1=yes, 0=no): "))
parking = float(input("Parking spaces: "))
prefarea = float(input("Preferred area? (1=yes, 0=no): "))
furnishingstatus = float(
    input("Furnishing status (0=furnished, 1=semi, 2=unfurnished): ")
)


# Format user data in the same way as the training data.
user_data = [
    area,
    bedrooms,
    bathrooms,
    stories,
    mainroad,
    guestroom,
    basement,
    hotwaterheating,
    airconditioning,
    parking,
    prefarea,
    furnishingstatus,
    0
]

user_data[0] = user_data[0] / 10000


predicted_price = predict(user_data, weights)

print("Your house will likely cost $", int(predicted_price))

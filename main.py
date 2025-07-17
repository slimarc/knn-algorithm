import matplotlib.pyplot as plt
import numpy as np

measures_flowers_data_x = [
    [1.4, 0.2], [1.3, 0.2], [1.5, 0.2], [4.5, 1.5], [4.1, 1.0],
    [4.7, 1.4], [1.7, 0.3], [4.2, 1.3], [1.5, 0.4], [4.3, 1.4]
]
type_flowers_data_y = [0, 0, 0, 1, 1, 1, 0, 1, 0, 1]


def calculate_euclidean_distance(new_point, measures_data_x, type_data_y):
    """
    Essa função calcula a distância euclidiana entre o novo ponto e os dados de treinamento.
    """
    distances_data = []
    for flower, measures_flower in enumerate(measures_data_x):
        class_type_flower = type_data_y[flower]
        distance = (((new_point[0] - measures_flower[0]) ** 2) + ((new_point[1] - measures_flower[1]) ** 2)) ** 0.5
        distances_data.append((distance, class_type_flower))
    return distances_data

def calculate_manhattan_distance(new_point, measures_data_x, type_data_y):
    """
    Essa função calcula a distância manhattan entre o novo ponto e os dados de treinamento.
    """
    distances_data = []
    for flower, measures_flower in enumerate(measures_data_x):
        class_type_flower = type_data_y[flower]
        distance = abs(new_point[0] - measures_flower[0]) + abs(new_point[1] - measures_flower[1])
        distances_data.append((distance, class_type_flower))
    return distances_data

def knn_predict_for_loocv(point, k, distance_type, train_data_x, train_data_y):
    """
    Essa função retorna o tipo previsto da flor, sendo que optei por utilizar KNN ponderado para critério de desempate caso
    o K vizinhos possuem o mesmo número de tipos de flor, então não preciso usar collections.Counter para contar os tipos.
    """
    if distance_type == "euclidean":
        distances = calculate_euclidean_distance(point, train_data_x, train_data_y)
    elif distance_type == "manhattan":
        distances = calculate_manhattan_distance(point, train_data_x, train_data_y)
    else:
        return None

    ordered_distances = sorted(distances, key=lambda x: x[0])
    k_nearest_neighbors = ordered_distances[:k]

    if not k_nearest_neighbors:
        return None

    weighted_votes = {}
    for distance, type_label in k_nearest_neighbors:
        if distance == 0:
            return type_label
        else:
            weight = 1 / distance

        if type_label in weighted_votes:
            weighted_votes[type_label] += weight
        else:
            weighted_votes[type_label] = weight

    if not weighted_votes:
        return None

    most_common_type = max(weighted_votes, key=weighted_votes.get)
    return most_common_type

def knn_predict(point, k, distance_type):
    """
    Utilizo essa função apenas para respeitar o escopo da atividade, mas ela pode ser utilizada para prever o tipo de flor.
    """
    return knn_predict_for_loocv(point, k, distance_type, measures_flowers_data_x, type_flowers_data_y)


def leave_one_out_cross_validation(measures_data_x, type_data_y, k, distance_type):
    """
    Essa função faz a validação por leave_one_out, retornando o desempenho do algoritmo, por se tratar de um dataset específico
    o resultado da acurácia será 1. Ela também gera um pequeno relatório de cada teste. Ela armazena os pontos a serem testados
    em variáveis temporárias e compara com os dados reais para determinar se o resultado foi correto ou incorreto.
    """
    correct_predictions = 0
    total_predictions = len(measures_data_x)

    print("\n|-----------Details of Leave-One-Out Cross-Validation-----------|")
    for i in range(total_predictions):
        test_point_measures = measures_data_x[i]
        true_type_for_test_point = type_data_y[i]
        temp_measures_data_x = measures_data_x[:i] + measures_data_x[i + 1:]
        temp_type_data_y = type_data_y[:i] + type_data_y[i + 1:]
        predicted_type = knn_predict_for_loocv(test_point_measures, k, distance_type, temp_measures_data_x, temp_type_data_y)

        print(f"Interation {i + 1}/{total_predictions}:")
        print(f"  Test point (X): {test_point_measures}")
        print(f"  Real type (Y): {true_type_for_test_point} (Type {'A' if true_type_for_test_point == 0 else 'B'})")
        if predicted_type is not None:
            print(f"  Predict class: {predicted_type} (Tipo {'A' if predicted_type == 0 else 'B'})")
            if predicted_type == true_type_for_test_point:
                correct_predictions += 1
                print("  Result: Correct prediction!")
            else:
                print("  Result: Incorrect prediction!")
        else:
            print("  Could not predict the class. Please check input or data.")
            print("  Result: Could not predict the class.")
        print("-"*40)

    accuracy = (correct_predictions / total_predictions) * 100
    return print(f"Accuracy with Leave-One-Out Cross-Validation: {accuracy:.2f}%")

def menu():
    print("\n|--------------KNN ALGORITHM-----------------|")
    petal_length = float(input("Enter the length of the petal: "))
    petal_width = float(input("Enter the width of the petal: "))
    k_neighbors  = int(input("Enter the value of K: "))
    distance_type = input("Enter the type of distance (euclidean/manhattan): ").lower()
    point = [petal_length, petal_width]
    return point, k_neighbors, distance_type

def plot(measures_data_x, type_data_y, new_point):
    measures_data_x_np = np.array(measures_data_x)
    type_data_y_np = np.array(type_data_y)

    class_0_x = measures_data_x_np[type_data_y_np == 0]
    class_1_x = measures_data_x_np[type_data_y_np == 1]

    plt.figure(figsize=(8, 6))

    plt.scatter(class_0_x[:, 0], class_0_x[:, 1], color='red', label='Type 0 (Flower A)')
    plt.scatter(class_1_x[:, 0], class_1_x[:, 1], color='black', label='Type 1 (Flower B)')

    plt.scatter(new_point[0], new_point[1], color='blue', marker='*', s=200, label='New Point')

    plt.title('Flower Petal Characteristics Dispersion')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    plt.legend()
    plt.grid(True)

    plt.show()

point, k, distance_type = menu()
predict_class = knn_predict(point, k, distance_type)

if predict_class is not None:
    plot(measures_flowers_data_x, type_flowers_data_y, point)
    if predict_class == 0:
        print(f"Predicted class: {predict_class} (Type flower A)")
    else:
        print(f"Predicted class: {predict_class} (Type flower B)")
else:
    print("Could not predict the class. Please check input or data.")

leave_one_out_cross_validation(measures_flowers_data_x, type_flowers_data_y, k, distance_type)
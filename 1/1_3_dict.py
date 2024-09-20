
def farm(animal):
    farm1 = {
        'корова': [11, 250],
        'курица': [5, 2],
        'свинья': [12, 100],
        'гусь': [8, 5],
        'лошадь': [18, 400],
    }
    farm2 = {
        'корова': [13, 230],
        'курица': [5, 3],
        'свинья': [11, 90],
        'гусь': [9, 5],
        'индюк': [10, 8],
    }

    animal_data1 = farm1.get(animal)
    animal_data2 = farm2.get(animal)
    is_first_animal_younger = False

    if animal_data1[0] == animal_data2[0]:
         return (animal_data1[1] + animal_data2[1]) / 2
    elif animal_data1[0] < animal_data2[0]:
        is_first_animal_younger = True

    result = animal_data1[1] if is_first_animal_younger else animal_data2[1]

    return result


def main():
    print(farm('курица'))
    print(farm('корова'))


if __name__ == '__main__':
    main()

from python_intermidiate_training.exceptions_1.exercises_1 import case_1, case_2, case_3, case_4, case_4_v_2


def main():
    print('Start up')

    # try:
    #
    #     case_2('')
    # except Exception as e:
    #     print(f'Exception {e.args}')

    # result = case_3(10, 0)
    # print(result)
    # print(f'Finish')
    dictionary = {
        "rzeczy": ['butter', 'bread']
    }
    case_4_v_2(dictionary)

if __name__ == '__main__':
    main()
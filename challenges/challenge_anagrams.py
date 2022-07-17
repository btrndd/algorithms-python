def is_anagram(first_string, second_string):
    if (len(first_string) < 1 or len(second_string) < 1):
        return False

    end_first = len(first_string) - 1
    end_second = len(second_string) - 1
    start = 0
    arr1 = []
    arr2 = []

    return quick_sort(list(first_string.lower()), start, end_first, arr1, arr2) == quick_sort(list(second_string.lower()), start, end_second, arr1, arr2)


## quick sort e partition elaboradas com auxilio do conteudo do course
## https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/a8624298-434b-42bf-b713-5f1d3e69859c/algoritmos-que-usam-dividir-e-conquistar/1a3b70b4-7836-4677-b2a2-c26f772672d7?use_case=side_bar
def quick_sort(string, start, end, arr1, arr2):
    if start < end:
        p = partition(string, start, end)

        arr1 = quick_sort(p[1], start, p[0] - 1, arr1, arr2)

        arr2 = quick_sort(p[1], p[0] + 1, end, arr1, arr2)
    elif (len(arr1) > 0 and len(arr2) > 0):
        string = arr1 + arr2

    return string


def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):
        if string[index] <= pivot:
          delimiter = delimiter + 1
          string[index], string[delimiter] = string[delimiter], string[index]

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return (delimiter + 1, string)

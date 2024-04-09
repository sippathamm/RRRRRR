def generate_permutation(n: int, s: str) -> list:
    if n < 0:
        return []
    if n == 0:
        return [s.strip()]
    result = []
    result.extend(generate_permutation(n - 1, 'ร ' + s))
    result.extend(generate_permutation(n - 2, 'รร ' + s))
    result.extend(generate_permutation(n - 3, 'รรร ' + s))
    return result


def main() -> None:
    n = int(input('Enter a number of occurrences of \'ร\': '))
    permutation = generate_permutation(n, '')
    print('Number of permutations:', len(permutation))
    print('Permutation: ', permutation)


if __name__ == '__main__':
    main()

def generate_permutation(n: int) -> list:
    if n <= 0:
        return [[]]

    permutations = [[] for _ in range(n + 1)]
    permutations[0] = ['']

    for i in range(1, n + 1):
        for j in range(1, min(4, i + 1)):
            for permutation in permutations[i - j]:
                permutations[i].append('ร' * j + ' ' + permutation.strip())

    return permutations[n]


def main() -> None:
    n = int(input('Enter a number of occurrences of \'ร\': '))
    print('Word:', 'ร' * n)
    permutation = generate_permutation(n)
    print('Number of permutations:', len(permutation))
    print('Possible permutations: ', sorted(permutation))


if __name__ == '__main__':
    main()

def kmp_table(pattern) -> [int]:
    m = len(pattern)
    table = [-1] * m
    pos = 1  # the current position we are computing in the pattern ( pos equivalent to i )
    cnd = 0  # the zero-based index in the pattern of the next character of the current candidate substring ( cnd equivalent to j )

    while pos < m:
        if pattern[pos] == pattern[cnd]:
            table[pos] = table[cnd]
        else:
            table[pos] = cnd
            cnd = table[cnd]
            while cnd >= 0 and pattern[pos] != pattern[cnd]:
                cnd = table[cnd]
        pos += 1
        cnd += 1

    table.append(cnd)

    return table


def kmp_search(text, pattern) -> [int]:
    j, k = 0, 0  # the position of the current character in text, the position of the current character in pattern
    table = kmp_table(pattern)
    pos = []

    while j < len(text):
        if pattern[k] == text[j]:
            j += 1
            k += 1
            if k == len(pattern):
                # match
                pos.append(j - k)
                k = table[k]
        else:
            k = table[k]
            if k < 0:
                j += 1
                k += 1
    return pos


def axamac(text, pattern) -> [int]:
    pos = []

    # preprocessing
    table = kmp_table(pattern)
    m, n = len(pattern), len(text)
    ell = 1
    while pattern[ell - 1] == pattern[ell]:
        ell += 1
        if ell == m:
            ell = 0

    # searching
    i = ell
    j, k = 0, 0
    while j <= n - m:
        while i < m and pattern[i] == text[i + j]:
            i += 1
        if i >= m:
            while k < ell and pattern[k] == text[i + j]:
                k += 1
            if k >= ell:
                pos.append(j)
        j += i - table[i]
        if i == ell:
            k = max(0, k - 1)
        else:
            if table[i] <= ell:
                k = max(0, table[i])
                i = ell
            else:
                k = ell
                i = table[i]


# t, p = "bbbabbbba", "bbba"
t, p = "GCATCGCAGAGAGTATACAGTACG", "GCAGAGAG"
# pre processing
print("Table of pattern", p, ":", kmp_table(p))
# output should be: [-1, 0, 0, -1, 1, -1, 1, -1, 1]
# KMP
print("The pattern occurs at positions :", kmp_search(t, p))
# Apostolico-Chrochemore
print("The pattern occurs at positions :", axamac(t, p))
# output should be: [0, 5]


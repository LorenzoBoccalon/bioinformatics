"""
algorithm kmp_table:
    input:
        an array of characters, W (the word to be analyzed)
    output:
        an array of integers, T (the table to be filled)

    define variables:
        an integer, pos ← 1 (the current position we are computing in T)
        an integer, cnd ← 0 (the zero-based index in W of the next character of the current candidate substring)

    let T[0] ← -1

    while pos < length(W) do
        if W[pos] = W[cnd] then
            let T[pos] ← T[cnd]
        else
            let T[pos] ← cnd
            let cnd ← T[cnd] (to increase performance)
            while cnd ≥ 0 and W[pos] ≠ W[cnd] do
                let cnd ← T[cnd]
        let pos ← pos + 1, cnd ← cnd + 1

    let T[pos] ← cnd (only needed when all word occurrences are searched)
"""


def kmp_table(pattern) -> [int]:
    m = len(pattern)
    table = [-1] * m
    pos = 1  # the current position we are computing in T
    cnd = 0  # the zero-based index in W of the next character of the current candidate substring

    while pos < len(pattern):
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


"""
algorithm kmp_search:
    input:
        an array of characters, S (the text to be searched)
        an array of characters, W (the word sought)
    output:
        an array of integers, P (positions in S at which W is found)
        an integer, nP (number of positions)

    define variables:
        an integer, j ← 0 (the position of the current character in S)
        an integer, k ← 0 (the position of the current character in W)
        an array of integers, T (the table, computed elsewhere)

    let nP ← 0

    while j < length(S) do
        if W[k] = S[j] then
            let j ← j + 1
            let k ← k + 1
            if k = length(W) then
                (occurrence found, if only first occurrence is needed, m ← j - k  may be returned here)
                let P[nP] ← j - k, nP ← nP + 1
                let k ← T[k] (T[length(W)] can't be -1)
        else
            let k ← T[k]
            if k < 0 then
                let j ← j + 1
                let k ← k + 1
"""


def kmp_search(text, pattern) -> [int]:
    j, k = 0, 0  # the position of the current character in text, the position of the current character in pattern
    table = kmp_table(pattern)
    p = []

    while j < len(text):
        if pattern[k] == text[j]:
            j += 1
            k += 1
            if k == len(pattern):
                # match
                p.append(j - k)
                k = table[k]
        else:
            k = table[k]
            if k < 0:
                j += 1
                k += 1
    return p


text, pattern = "bbbabbbba", "bbba"
print("Table of pattern", pattern, ":", kmp_table(pattern))
print("The pattern occurs at positions :", kmp_search(text, pattern))

def dl_distance(word1, word2):
    # Luo talukko, joka tallentaa editointietäisyyden osaväleille
    dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]

    # Alusta taulukko
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j

    # Täytä taulukko dynaamisella ohjelmoinnilla
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i]
                                   [j - 1], dp[i - 1][j - 1])
            if (
                i > 1 and j > 1
                and word1[i - 1] == word2[j - 2]
                and word1[i - 2] == word2[j - 1]
            ):
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

    # Palauta muokkausetäisyys
    return dp[len(word1)][len(word2)]

"""Edit distance."""

# These words don't add any value to the search matching
STOP_WORDS = {"the", "is", "and"}


def distance(word1: str, word2: str) -> int:
    """Calculate the Levenshtein distance between two words."""

    # use an inner function so we dont have to pass around variables
    def backtrack(i: int, j: int, memo: dict) -> int:
        # check memo
        if (i, j) in memo:
            return memo[(i, j)]
        # base case
        if i == len(word1) and j == len(word2):
            return 0

        # out of bounds, we dont need to do more work as the cost
        # is everything left over in the non-empty word
        if i >= len(word1):
            # the remainder of word2 is the cost
            return len(word2) - j

        if j >= len(word2):
            # the remainder of word1 is the code
            return len(word1) - i

        # same letter
        if word1[i] == word2[j]:
            res: int = backtrack(i + 1, j + 1, memo)

        else:
            # different letter
            res: int = 1 + min(
                # insert
                backtrack(i, j + 1, memo),
                # delete
                backtrack(i + 1, j, memo),
                # replace
                backtrack(i + 1, j + 1, memo),
            )

        memo[(i, j)] = res
        return res

    return backtrack(0, 0, {})


def search_match(
    search_term: str,
    max_distance: int,
    word_list: list[str]
) -> list[str]:
    """Find matching results for a given search term.

    A match is any words that is less than or equal to max_distance.
    """
    result: list[str] = []

    for sentence in word_list:
        # tokenize sentence
        words: list[str] = sentence.split()

        for word in words:
            if word.lower() in STOP_WORDS: continue

            # if at least on of the words is similar, we count that as a match
            if distance(search_term, word.lower()) <= 3:
                print(word)
                result.append(sentence)
                # we dont need to do more work
                break

    return result


word_dict: list[str] = [
    "The King David Jerusalem Hotel, Jerusalem",
    "Burj Al Arab Jumeirah, Dubai",
    "The Plaza, New York City",
    "Fairmont Le Chateau Frontenac, Quebec City",
    "Old Faithful Inn. Yellowstone National Park",
    "Grand Hotel Furore, St Petersburg",
]


print(distance("horse", "ros"))
print(distance("intention", "execution"))
print(search_match("taj", 3, word_dict))

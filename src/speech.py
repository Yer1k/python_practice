"""Module for analyzing the word counts of the length of words in a speech."""


def analyse_word_counts(speech: str) -> None:
    """
    Function to analyze the word counts of the length of words in a speech.
    """
    # split into the different words
    words = speech.split(" ")

    word_index = 0
    for word in words:
        # get rid of punctuation and new lines
        # (using translation table for better performance)
        translation_table = str.maketrans("", "", ",.!?;\n")
        word = word.translate(translation_table)

        # turn to lower case
        word = word.lower()

        # write changes back to list
        words[word_index] = word

        # increment index
        word_index += 1

    # show number of words
    print(f"\nNumber of words = {len(words)}\n")

    # loop over number of letters from 1 to 20
    checksum = 0
    for num in range(0, 20):

        # show number of words with this many letters
        number_words = len([x for x in words if len(x) == num])
        if number_words > 0:
            checksum += number_words
            print(f"{num}-letter words = {number_words}")

    # show the total
    print(f"\nCheck total: {checksum}")


if __name__ == "__main__":

    # Julius Caesar Act 4, Scene 3, 218–224
    BRUTUS_SPEECH = (
        "There is a tide in the affairs of men \n"
        "Which, taken at the flood, leads on to fortune; \n"
        "Omitted, all the voyage of their life \n"
        "Is bound in shallows and in miseries. \n"
        "On such a full sea are we now afloat, \n"
        "And we must take the current when it serves, \n"
        "Or lose our ventures."
    )

    analyse_word_counts(BRUTUS_SPEECH)

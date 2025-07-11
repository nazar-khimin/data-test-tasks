from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

# Download required resources
nltk.download('punkt')
nltk.download('wordnet')


def stem_and_lemmatize(tokens):
    """
    Applies stemming and lemmatization to the input tokens.

    Args:
    tokens (list): A list of tokens (words).

    Returns:
    dict: A dictionary with original, stemmed, and lemmatized tokens.
    """
    
    return {
        "original": tokens,
        "stemmed": stemmed,
        "lemmatized": lemmatized
    }


if __name__ == "__main__":
    print(stem_and_lemmatize(['goes', 'worlds', 'done', 'being', 'undefined']))

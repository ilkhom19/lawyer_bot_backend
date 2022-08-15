from nltk.tokenize import sent_tokenize


def make_paired_sentences(article_text):
    sentences = sent_tokenize(article_text)
    if len(sentences) < 2:
        return article_text
    couple_sentences = [f'{sentences[i]}' for i in range(len(sentences) - 1)] #{sentences[i + 1]}

    return couple_sentences

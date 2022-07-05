from re import sub
import matplotlib.pyplot as plt
from colour import Color
import io, base64


def count_words(txt, case_sensitive):
    if not case_sensitive:
        txt = txt.lower()
    txt = sub(r'[^A-z ]', '', txt)
    words = {}
    for word in txt.split():
        if word not in words.keys():
            words[word] = 0
        words[word] += 1
    words = dict(sorted(words.items(), key=lambda x: (x[1], x[0]), reverse=True))
    return words


def extract_palindromes(words):
    palindromes = []
    for word in words.keys():
        if len(word) <= 2:
            continue
        word = word.lower()
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes


# TODO: empty plot

def plot_words(words):
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    values = list(words.values())[:10]
    if len(values) == 0:
        return None
    purple = Color("purple")
    blue = Color("blue")
    colors = [color.hex for color in list(purple.range_to(blue, 10))]
    bars = ax.bar(list(words.keys())[:10], values, color=colors, edgecolor="#FFFFFF")
    ax.bar_label(bars)
    ax.set_title("Top 10 most common words")
    ax.set_xlabel("word")
    ax.set_ylabel("count")
    ax.set_ylim(ymin=round(min(values) - values[-1] * 0.1) - 1)
    # fig.savefig("E://MDDaw/Pobrane/words.pdf")

    # https://spapas.github.io/2021/02/08/django-matplotlib/
    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()
    return b64

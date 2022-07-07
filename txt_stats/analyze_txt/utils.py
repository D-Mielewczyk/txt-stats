import base64
import io
from re import sub

import matplotlib.pyplot as plt
from colour import Color


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
    purple = Color("purple")
    blue = Color("blue")
    colors = [color.hex for color in list(purple.range_to(blue, 10))]
    values = list(words.values())[:10]
    bars = ax.bar(list(words.keys())[:10], values, color=colors, edgecolor="#FFFFFF")
    ax.bar_label(bars)
    ax.set_title("Top 10 most common words", fontsize="20")
    ax.set_xlabel("word", fontweight='bold')
    ax.set_ylabel("count", fontweight='bold')
    ax.set_ylim(ymin=round(min(values) - values[-1] * 0.1) - 1)
    plt.xticks(rotation=-25)
    fig.tight_layout()
    return fig_to_b64(fig)


# https://spapas.github.io/2021/02/08/django-matplotlib/
def fig_to_b64(fig):
    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()
    return b64


def can_access(user, owner):
    if user.is_superuser:
        return True
    if owner is None:
        return True
    if owner == user.pk:
        return True
    return False

"""
The :mod:`preprocessing` module includes normalization, 
abbr recognition, stopword filter, lemmatization.
""" 

from .punctuation import Replacer

from .methods import url_string_recognition_support
from .methods import punctuation_filter
from .methods import del_contiguous_point_support
from .methods import contiguos_string_recognition_support
from .methods import abbrev_recognition_support
from .methods import del_char_len_one
from .methods import add_text_end_dot


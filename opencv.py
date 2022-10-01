import math
import os
import sys


def read_file_binary(file_path: str) -> str:
    """
    Reads given file as bytes and returns them as a long string
    """
    result = ""
    try:
        with open(file_path, "rb") as binary_file:
            data = binary_file.read()
        for dat in data:
            curr_byte = f"{dat:08b}"
            result += curr_byte
        return result
    except OSError:
        print("File not accessible")
        sys.exit()


def add_key_to_lexicon(
    lexicon: dict, curr_string: str, index: int, last_match_id: str
) -> None:
    """
    Adds new strings (curr_string + "0",  curr_string + "1") to the lexicon
    """
    lexicon.pop(curr_string)
    lexicon[curr_string + "0"] = last_match_id

    if math.log2(index).is_integer():
        for curr_key in lexicon:
            lexicon[curr_key] = "0" + lexicon[curr_key]

    lexicon[curr_string + "1"] = bin(index)[2:]


def compress_data(data_bits: str) -> str:
    """
    Compresses given data_bits using Lempel–Ziv–Welch compression algorithm
    and returns the result as a string
    """
    lexicon = {"0": "0", "1": "1"}
    result, curr_string = "", ""
    index = len(lexicon)

    for i in range(len(data_bits)):
        curr_string += data_bits[i]
        if curr_string not in lexicon:
            continue

        last_match_id = lexicon[curr_string]
        result += last_match_id
        add_key_to_lexicon(lexicon, curr_string, index, last_match_id)
        index += 1
        curr_string = ""

    while curr_string != "" and curr_string not in lexicon:
        curr_string += "0"

    if curr_string != "":
        last_match_id = lexicon[curr_string]
        result += last_match_id

    return result

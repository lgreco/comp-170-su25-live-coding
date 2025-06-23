def our_upper_case(word:str) -> str:
    result = None
    if len(word) > 0:
        result = ""
        for i in range(len(word)):
            current_character = word[i]
            # find the ascii value of the current character
            current_ascii = ord(current_character)
            # Subtract to bring to upper case
            new_ascii = current_ascii - 32
            # create a new symbol with this ascii code
            new_character = chr(new_ascii)
            # concatenate new char to the output string
            result = result + new_character
    # done
    return result

# quick demo
print(our_upper_case("Leo9"))
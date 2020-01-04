def commafy(list):
    # Turn the list into a comma separated string
    # Grab last item
    last_item = list[len(list) - 1]
    #print("last item: ", last_item)
    list.pop(len(list) - 1)
    result_string = ""
    for item in list:
        result_string += str(item) + ", "

    # Trim extra chars off and add 'and'
    result_string = result_string[:-2]

    return result_string + ", and " + str(last_item)


def test_commafy():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    spam2 = [1, 2, 3, 4]

    result = commafy(spam2)
    print("result: %s" % result)

    if result == '1, 2, 3, and 4':
        return True
    else:
        return False


if __name__ == "__main__":
    result = test_commafy()
    print(result)
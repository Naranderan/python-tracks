def proverb(*words, qualifier):
    proverb_text = []
    proverb_each_line_template = "For want of a {0} the {1} was lost."
    proverb_last_line_template = "And all for the want of a {0}."

    for index in range(len(words)):
        if index != len(words) - 1:
            proverb_text.append(proverb_each_line_template.format(words[index], words[index+1]))
        else:
            proverb_text.append(proverb_last_line_template.format(words[0] if qualifier == None else qualifier+" "+words[0]))

    return proverb_text

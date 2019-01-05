# fix the error prob

# semi error
def semi_error_fixer(error_line_list, filename):
    f = open(filename, 'r')
    contents = f.readlines()
    f.close()

    for semi_error_line_num in error_line_list:
        tmp_line = contents[semi_error_line_num - 2]
        tmp_line = tmp_line.replace('\n', ';\n')
        contents[semi_error_line_num - 2] = tmp_line

    f = open(filename, 'w')
    contents = "".join(contents)
    f.write(contents)
    f.close()


def error_fixer(error_dict, filename):
    if 'semi' in error_dict:
        semi_error_fixer(error_dict['semi'], filename)


        



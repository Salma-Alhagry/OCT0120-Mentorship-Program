def sed(pattern, replace, source, dest):
    try:
        f_input = open(source, 'r')
        try:
            f_output = open(dest,'w')
            for line in f_input:
                line = line.replace(pattern, replace)
                f_output.write(line)
            f_output.close()

        except IOError:
            print('\n cant open file for writing')
            f_input.close()

    except IOError:
        print('\n cant open file for reading')

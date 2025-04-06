def remove_articles(input_file,output_file):
    articles = ['a','an','the']
    with open(input_file,'r') as infile:
        lines = infile.readlines()
    cleaned_lines = []
    for line in lines:
        words = line.split()
        cleaned = ['' if word.lower() in articles else word for word in words]
        cleaned_line = ' '.join(cleaned)
        cleaned_lines.append(cleaned_line)

    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(cleaned_lines))

remove_articles('input.txt','output.txt')

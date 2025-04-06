source_file = "input.txt"
output_file = "output.txt"

with open (source_file, "r") as infile, \
    open (output_file,"w") as outfile:
    for line in infile:
        modified_line = line.upper()
        outfile.write(modified_line)
        

with open("file1.txt", "r") as f1, \
     open("file2.txt", "r") as f2, \
     open("merged_file.txt", "w") as out:
    
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    max_len = max(len(lines1), len(lines2))

    for i in range(max_len):
        if i < len(lines1):
            out.write(lines1[i].rstrip() + '\n')
        if i < len(lines2):
            out.write(lines2[i].rstrip() + '\n')

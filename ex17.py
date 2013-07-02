from sys import argv

script, from_file, to_file = argv

in_file = open(from_file,'r')
out_file = open(to_file,'w')
out_file.write(open(from_file).read())

out_file.close()
in_file.close()



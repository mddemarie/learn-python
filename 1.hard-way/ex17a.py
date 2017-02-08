from sys import argv; from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file).read()

print ("File existing? %r" % exists(to_file))

out_file = open(to_file, 'w').write(in_file)
import os
from ppm_maker import PPMMaker

input_directory = "sources/ppm/"
output_directory = "generated/images/"
ppm_maker = PPMMaker()
for input_file in os.listdir(input_directory):
    if input_file.endswith(".txt"):
        output_filename = os.path.splitext(os.path.basename(input_file))[0] + ".gif"
        ppm_maker.image_from_ppm_file(input_directory + input_file, output_directory + output_filename)
        print "Generated " + output_directory + output_filename


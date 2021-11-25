import filter
import old_filter

def use_filter():
    input_file = input("Input file: ")
    output_file = input("Output file: ")
    mosaic_size = int(input("Mosaic size: "))
    grayscale = int(input("Grayscale: "))
    input_file = "img/" + input_file + ".jpg"
    output_file = "img/" + output_file + ".jpg"

    pixel_art_optimized = filter.generate_pixel_art_optimized(input_file, mosaic_size, grayscale)
    pixel_art_optimized.save(output_file)

def use_old_filter():
    old_filter.generate_pixel_art()

use_filter()
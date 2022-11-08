__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil


current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r"cache")
cache_dir = r"C:\Users\dkuyl\winc\Assignments\files"
zip_file = r"C:\Users\dkuyl\winc\Assignments\files\data.zip"


def clean_cache():
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    else:
        shutil.rmtree(final_directory)
        os.makedirs(final_directory)


def cache_zip(zip_file_path, cache_dir_path):
    shutil.unpack_archive(zip_file_path, extract_dir=cache_dir_path)


def cached_files():
    file_paths = []

    for folder, subs, files in os.walk(os.path.join(os.getcwd(), 'cache')):
        for filename in files:
            file_paths.append(os.path.abspath(os.path.join(folder, filename)))
    return file_paths


def find_password(list):
    for path in list:
        for line in open(path):
            phrase = "password"
            if phrase in line:
                passw = line.split(" ")[1]
                return passw.strip()


'''
ik zal heel eerlijk zijn dit is veelal het werk van google,
maar heb wel door hoe je zelf dus uitvind wat werk en wat niet.
Maar heb wel het gevoel dat ik vooral copy/paste/adjust heb gedaan,
en van bijvoorbeeld de os.walk functie weet ik niet 100% zeker of die er wel in moet
bij cached_files.
ik hoop dat dit zo generiek genoeg is. bij mij geeft hij groen aan iig.
'''
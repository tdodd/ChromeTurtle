#!/usr/bin/env python

import os
import pathlib
from scripts.template_builder import TemplateBuilder

if __name__ == '__main__':
   # Get files in working directory
   working_directory = os.getcwd()
   files = os.listdir(working_directory)

   movie_dirs = []

   # Get video directories
   for f in files:
      if os.path.isdir(f):
         path = working_directory + '/' + f
         movie_dirs.append(path)

   # Valid video file extensions
   file_extensions = {
      '.avi': True,
      '.flv': True,
      '.wmv': True,
      '.mov': True,
      '.mp4': True,
      '.mkv': True
   }

   movie_files = {}

   # Get video files for each directory
   for md in movie_dirs:
      movie_files[md] = []
      md_files = os.listdir(md)
      for f in md_files:
         path = md + '/' + f
         if pathlib.Path(path).suffix in file_extensions:
            movie_files[md].append(f)

   # Build the html template
   builder = TemplateBuilder()
   builder.build_template(movie_files, movie_dirs, working_directory)

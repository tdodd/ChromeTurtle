import os

class TemplateBuilder:
   """
   The template builder constructs the html template for displaying the video files
   """

   def build_template(self, movie_files, movie_dirs, working_directory):
      """
      Build the html template
      :param movie_files: a map containing the movie directories and their movie files
      :param movie_dirs: this list of directories
      :param working_directory: the directory where the script was called
      """
      header_path = os.path.dirname(os.path.realpath(__file__)) + '/header.html'
      footer_path = os.path.dirname(os.path.realpath(__file__)) + '/footer.html'

      header_contents = ''
      footer_contents = ''

      # Read template file contents
      with open(header_path, 'r') as html_header:
         header_contents = html_header.read().replace('\n', '')

      with open(footer_path, 'r') as html_footer:
         footer_contents = html_footer.read().replace('\n', '')

      folder_snippet = '<h1>{0}</h1>'
      video_snippet = '<li data-movie-src="{0}">{1}</li>'
      body_contents = ''

      # Add html snippets
      for directory, movies in movie_files.items():
         if len(movies) > 0: # Folder has videos
            # Get directory name
            dir_name = os.path.basename(os.path.normpath(directory))
            dir_header = folder_snippet.format(dir_name)
            body_contents = body_contents + dir_header

            body_contents = body_contents + '<ul>'

            # Get video location
            for movie in movies:
               movie_path = directory + '/' + movie
               body_contents = body_contents + video_snippet.format(movie_path, movie)

            body_contents = body_contents + '</ul>'

      # Create html file
      output_contents = header_contents + body_contents + footer_contents
      output_filename = working_directory + '/videos.html'
      output_file = open(output_filename, 'w+')
      output_file.write(output_contents)
      output_file.close()

import figmapy
import pprint
import os

token = os.environ["FIGMA_TOKEN"]  # can be found in your figma user profile page
file_key = os.environ["FIGMA_FILE"]  # can be found in the URL of the file
figmaPy = figmapy.FigmaPy(token=token)
file = figmaPy.get_file(key=file_key)
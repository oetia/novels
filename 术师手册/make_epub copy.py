import os
import zipfile

# Zip the files into an EPUB
with zipfile.ZipFile('my_ebook.epub', 'w') as epub:
    epub.write('my_ebook/mimetype', 'mimetype', compress_type=zipfile.ZIP_STORED)
    for folder, subfolders, files in os.walk('my_ebook'):
        for file in files:
            if file != 'mimetype':
                epub.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), 'my_ebook'), compress_type=zipfile.ZIP_DEFLATED)
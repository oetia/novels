import os
import zipfile

# Create directory structure
os.makedirs('my_ebook/META-INF', exist_ok=True)
os.makedirs('my_ebook/OEBPS', exist_ok=True)

# Create mimetype file
with open('my_ebook/mimetype', 'w') as f:
    f.write('application/epub+zip')

# Create META-INF/container.xml
container_xml = '''<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
with open('my_ebook/META-INF/container.xml', 'w') as f:
    f.write(container_xml)

html_files = os.listdir("./html")


toc_string = ""



# Create OEBPS/content.opf
content_opf = '''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="2.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:title>My eBook</dc:title>
        <dc:identifier id="bookid">urn:uuid:12345</dc:identifier>
        <dc:language>en</dc:language>
    </metadata>
    <manifest>
        <item id="toc" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
        <item id="chapter1" href="chapter1.xhtml" media-type="application/xhtml+xml"/>
        <item id="chapter2" href="chapter2.xhtml" media-type="application/xhtml+xml"/>
        <item id="chapter3" href="chapter3.xhtml" media-type="application/xhtml+xml"/>
    </manifest>
    <spine toc="toc">
        <itemref idref="chapter1"/>
        <itemref idref="chapter2"/>
        <itemref idref="chapter3"/>
    </spine>
</package>'''
with open('my_ebook/OEBPS/content.opf', 'w') as f:
    f.write(content_opf)

# Create OEBPS/toc.ncx
toc_ncx = '''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="urn:uuid:12345"/>
        <meta name="dtb:depth" content="1"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle>
        <text>My eBook</text>
    </docTitle>
    <navMap>
        <navPoint id="navPoint-1" playOrder="1">
            <navLabel>
                <text>Chapter 1</text>
            </navLabel>
            <content src="chapter1.xhtml"/>
        </navPoint>
        <navPoint id="navPoint-2" playOrder="2">
            <navLabel>
                <text>Chapter 2</text>
            </navLabel>
            <content src="chapter2.xhtml"/>
        </navPoint>

        <navPoint id="navPoint-3" playOrder="3">
            <navLabel>
                <text>Chapter 3</text>
            </navLabel>
            <content src="chapter3.xhtml"/>
        </navPoint>
    </navMap>
</ncx>'''
with open('my_ebook/OEBPS/toc.ncx', 'w') as f:
    f.write(toc_ncx)

# Create OEBPS/chapter1.xhtml
chapter1_xhtml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Chapter 1</title>
</head>
<body>
    <h1>Chapter 1</h1>
    <p>This is the first chapter of my eBook.</p>
</body>
</html>'''
with open('my_ebook/OEBPS/chapter1.xhtml', 'w') as f:
    f.write(chapter1_xhtml)

# Create OEBPS/chapter2.xhtml
chapter2_xhtml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Chapter 2</title>
</head>
<body>
    <h1>Chapter 2</h1>
    <p>This is the second chapter of my eBook.</p>
</body>
</html>'''
with open('my_ebook/OEBPS/chapter2.xhtml', 'w') as f:
    f.write(chapter2_xhtml)

# Create OEBPS/chapter2.xhtml
chapter3_xhtml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Chapter 3</title>
</head>
<body>
    <h1>Chapter 3</h1>
    <p>This is the third chapter of my eBook.</p>
</body>
</html>'''
with open('my_ebook/OEBPS/chapter3.xhtml', 'w') as f:
    f.write(chapter3_xhtml)

# Zip the files into an EPUB
with zipfile.ZipFile('my_ebook.epub', 'w') as epub:
    epub.write('my_ebook/mimetype', 'mimetype', compress_type=zipfile.ZIP_STORED)
    for folder, subfolders, files in os.walk('my_ebook'):
        for file in files:
            if file != 'mimetype':
                epub.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), 'my_ebook'), compress_type=zipfile.ZIP_DEFLATED)
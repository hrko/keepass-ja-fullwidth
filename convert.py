import requests
import zipfile
import gzip
import io
import xml.etree.ElementTree as ET
import unicodedata
import uuid
import datetime
import sys

keepass_version = sys.argv[1]
url = f"https://downloads.sourceforge.net/project/keepass/Translations%202.x/{keepass_version}/KeePass-{keepass_version}-Japanese.zip"

zip_bytes = requests.get(url).content
with zipfile.ZipFile(io.BytesIO(zip_bytes)) as tmp:
    lngx_bytes = tmp.read("Japanese.lngx")
with gzip.open(io.BytesIO(lngx_bytes), mode='rt', encoding="utf-8") as tmp:
    xml_text = tmp.read()

mod_author = "hrko"
contact = "https://github.com/hrko/keepass-ja-fullwidth"
generator = "keepass-ja-fullwidth"

root = ET.fromstring(xml_text)

for element in root.findall(".//Value"):
    element.text = unicodedata.normalize('NFKC', element.text)

for element in root.findall(".//Text"):
    element.text = unicodedata.normalize('NFKC', element.text)

element = root.find("./Properties/NameEnglish")
element.text = "Japanese (Full Width)"

element = root.find("./Properties/NameNative")
element.text = "日本語 (全角)"

element = root.find("./Properties/AuthorName")
element.text = f"{element.text} (改変: {mod_author})"

element = root.find("./Properties/AuthorContact")
element.text = contact

element = root.find("./Properties/Generator")
element.text = generator

element = root.find("./Properties/FileUuid")
element.text = uuid.uuid4().hex.upper()

element = root.find("./Properties/LastModified")
now = datetime.datetime.utcnow()
element.text = now.strftime("%Y-%m-%d %H:%M:%SZ")

dest_lngx_path = f"Japanese-{keepass_version}-FullWidth.lngx"
with gzip.open(dest_lngx_path, mode="wb") as tmp:
    tree = ET.ElementTree(root)
    tree.write(tmp, encoding="utf-8", xml_declaration=True)

print(f"converted file has been saved to {dest_lngx_path}")
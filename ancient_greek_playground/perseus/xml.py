from lxml import etree

from .models import Author, Work

METADATA_FILENAME = "__cts__.xml"
NAMESPACES = {
    "ti": "http://chs.harvard.edu/xmlns/cts",
    "xml": "http://www.w3.org/XML/1998/namespace",
    "tei": "http://www.tei-c.org/ns/1.0",
}


def extract_author_metadata(xml_file_path: str) -> Author:
    tree = etree.parse(xml_file_path)
    author_name = tree.xpath(
        "/ti:textgroup/ti:groupname/text()", namespaces=NAMESPACES
    )[0]
    author_urn = tree.xpath("/ti:textgroup/@urn", namespaces=NAMESPACES)[0]
    return Author(author_name, author_urn, works={})


def extract_work_metadata(xml_file_path: str) -> Work:
    tree = etree.parse(xml_file_path)
    work_name = tree.xpath("/ti:work/ti:title/text()", namespaces=NAMESPACES)[0]
    work_urn = tree.xpath("/ti:work/@urn", namespaces=NAMESPACES)[0]
    return Work(work_name, work_urn)


def get_greek_text(xml_file: str):
    tree = etree.parse(xml_file)

    greek_text = tree.xpath(
        "//tei:div[@xml:lang='grc']//text()",
        namespaces=NAMESPACES,
    )

    return " ".join([stripped for text in greek_text if (stripped := text.strip())])

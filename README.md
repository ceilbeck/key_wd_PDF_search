
# key_wd_PDF_search

This program searches a directory of PDF files looking for key words.  For each PDF file it finds, it searches the text of the file for a number of pre-defined key words.  For each PDF file it prints out a list of which line each key word was found, plus the actual key word itself in square brackets plus 50 characters on either side of the key word.  In addition there is a summary of the key words found and how many times each key word was found in the given file.  Finally, a summary of all the results across multiple files is printed out in a file called **Notes.txt**.

## Usage
**\> python3  key_wd_PDF_search.py  \<dir1\>  \[\<dir2\>\]**

where **\<dir1\>** is the directory to be searched, and the optional **\<dir2\>** is the destination for the output files.  If **\<dir2\>** is omitted, the destination for the output files defaults to **\<dir1\>**.

You also need a plain text file called **key_wds.txt** in **\<dir1\>**  containing all the key words you are interested in, one per line.

### Prerequisite

**key_wds.txt** uses pdfplumber, so this needs to be installed before your first run.

**\> pip install pdfplumber**

### Note
This program is intended to be used for examining scientific journal articles.  Such articles come in a variety of layout formats, 1-column, 2-column, etc.  The program makes no attempt to identify which format any specific paper uses, but assumes that the first page is single column (to cover the abstracts) and the remaining pages are all in 2-column format. Thus it may misidentify some line breaks, shown as "|" in the output text.

The default program prints 50 characters on either side of the key word found, to give the context.  Change the constant **pad** at line 135 if you want to use another value.

The use of this code in a literature survey is decribed in the paper *Data mining versus manual screening to select papers for inclusion in systematic reviews: a novel method to increase efficiency*, Elena Ierardi, J Chris Eilbeck, Frederike van Wijck, Myzoon Ali and Fiona Coupar, submitted for publication.

Chris Eilbeck J.C.Eilbeck@hw.ac.uk

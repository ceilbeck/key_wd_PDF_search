#!/user/bin/env python3
#
# Looks for key word list in a directory of pdf files
# cd tex/software/python/FvWsearch
import pdfplumber, re, sys, glob, os, collections, time, datetime, key_wd_PDF_search as ml

def main():
    starttime = time.time()
    na = len(sys.argv)
    if na==3:
        indirname = os.path.normcase(sys.argv[1]); 
        outdirname = os.path.normcase(sys.argv[2]);
    elif na==2:
        indirname = os.path.normcase(sys.argv[1]); 
        outdirname = os.path.normcase(sys.argv[1]);
    else:
        print("Usage:", os.path.normcase(sys.argv[1]),
              os.path.normcase(sys.argv[1]), "indir outdir");
        sys.exit(1)
        
    print("dir in:", indirname, ", dir out:", outdirname);

    dir1 = os.path.normcase(sys.argv[1])
    
    pattern = ml.pattern()
    files = sorted(glob.glob(dir1+"/*.pdf"))
    numfiles = len(files)
    print("num files to process: {0:6}".format(numfiles))
    startnum = 0
    file_count = startnum
    
    key_wds_overall = collections.defaultdict(int)
    if not os.path.isdir(outdirname):
        os.mkdir(outdirname)
    notes = outdirname+"/Notes.txt"
    notes = os.path.normcase(notes)
    print("output summary:",notes,"\n")
    f_notes = open(notes,"w")

    for fileName in files[startnum:numfiles]:
        #print("\n")
        key_wds = collections.defaultdict(int)

 
        fnew = fileName.replace(".pdf",".txt")
        op_f = open(fnew,"w")
        print("File number {0:5}".format(file_count+1))
        op_f.write("\n")
        file_count += 1
        print("reading from ",fileName)
        print("writing to",fnew,"\n")
           
        try:
            with pdfplumber.open(fileName) as pdf:
    
                numPages = len(pdf.pages)
                op_f.write(f"No of Pages {numPages+1}\n")
                key_wds = collections.defaultdict(int)
               # first page
                op_f.write(f"Page 1\n")
                p0 = pdf.pages[0]
                text = p0.extract_text(x_tolerance=1.5)
                ml.kw_list(text, pattern, key_wds, key_wds_overall, op_f)  
              
                for i in range(1, numPages): #numPages min(2,numPages)

                    p0 = pdf.pages[i]           
                    left_col = p0.crop((0, 0, 0.5 * float(p0.width), p0.height),
                      relative=True)
                    right_col = p0.crop((0.5 * float(p0.width), 0,\
                      float(p0.width), p0.height),  relative=True)
                    text1 = left_col.extract_text(x_tolerance=1.5)
                    if text1 is None:
                       print("txt1 =", text1)
                    else:
                       op_f.write(f"Page {i+1}, col 1\n")
                       ml.kw_list(text1, pattern, key_wds, key_wds_overall, op_f)
                    text2 = right_col.extract_text(x_tolerance=1.5)
                    if text2 is None:
                       print("txt2 =", text2)
                    else:
                       op_f.write(f"Page {i+1}, col 2\n")    
                       ml.kw_list(text2, pattern, key_wds, key_wds_overall, op_f)
                    if text1 is None and text2 is None:
                       op_f.write(f"Page {i+1}, no matches this page\n") 
        except :
            print("Exception!")
            print(fileName)
            f_notes.write("{0:15} Error \n".format(fileName))
     
            
        for word in sorted(key_wds):
                op_f.write("{0:12} : {1:4}\n".format(word, key_wds[word]))
         
    print("key_wd_PDF_search.py calculation time = {0:8.4f} secs\n".
          format(time.time()-starttime))
         
    op_f.close()

    
    dt = datetime.datetime.now()

    f_notes.write("Run of key_wd_PDF_search.py on ")
    f_notes.write(dt.strftime("%c"))

    f_notes.write("\n\nKeywords = \n")
    f_notes.write(str(pattern.split('|')))

    f_notes.write("\n\n{0:5} files processed in {1:g} seconds\n\n".
       format(len(files), time.time()-starttime))
    for word in sorted(key_wds_overall):
        f_notes.write("{0:12} : {1:7}\n".format(word, key_wds_overall[word]))
    f_notes.close()
 

main()

import re

def pattern():
     return 'Abil|Adult|Arm|Degree|Difficult|Function|Good|Group|' + \
     'Hierarch|High|Impair|Keyword|Level|Little|Low|Mild|Moder|Poor|Problem|' + \
     'Recover|Sever|Stratif|Stroke|Upper|Diagnos|Participant|Subject|Patient|' + \
     'Survivor|Elbow|Finger|Hand|Shoulder|Wrist'
    

      
def kw_list(text, pattern, key_wds, key_wds_overall, op_f): 
    for match in re.finditer(pattern, text, re.I):
        pad = 50
        i1 = match.start()
        i2 = match.end()
        str1 = text[i1-pad:i1]+"["+ text[i1:i2]+"]" +text[i2:i2+pad]
        str1 = str1.replace('-\n','')
        str1 = str1.replace('\n',' | ')
        op_f.write(f"Match: {i1} {str1}\n")
        key_wds[text[i1:i2].lower()] += 1
        key_wds_overall[text[i1:i2].lower()] += 1



import re

def questions_mark(text:str):
    
    lst = []
    count = 0
    regex = re.compile(r'[\d.*\?{3}\d]')
    find_text = regex.findall(text)
    if find_text:       
        for i in find_text:
            lst.append(i)
            text = text.replace(i,'')
            new_list = [int(item) for lst in lst for item in lst if item.isdigit()]
        
        for i in new_list:
            if sum(new_list[0:2:1]) == 10:
                count += 1
                del new_list[0:2:1]
        if  1 <= count :
            return True 
        
        return False
    else:
        return False        

    



def test_Qustions_Marks():
    assert questions_mark('arrb6???4xxbl5???5eee5') == True 
    assert questions_mark('arrb6???4xxbl5???5') == True
    assert questions_mark('"aa6???7"') == False
    assert questions_mark("acc?7??sss?3rr1??????5") == True
    assert questions_mark('9???1???9???1???9') == True

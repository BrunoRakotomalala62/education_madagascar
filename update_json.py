import json
import os

# Nouvelles données pour Philosophie série A
NEW_PDFS_A = [
    {"titre": "Enoncé Philosophie série A 2011", "session": "2011", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/liAlsqumUjJEGJPy.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2010", "session": "2010", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/zeMBAfYITNLRLeac.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2009", "session": "2009", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/emYVXODHbKSaZhSB.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2008", "session": "2008", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/ghnJDDnBZrhykUKt.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2007", "session": "2007", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/ZDZwCYnMIoFptqBk.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2005", "session": "2005", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/ASFZiqqCMneyXisG.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2004", "session": "2004", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/wqlEUSBEFIfIcDhq.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2003", "session": "2003", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/jAaQzwhCmZlcMhBw.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2002", "session": "2002", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/RZTTlXpjAHPKjUww.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2001", "session": "2001", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/aTjOrGJsEFBUTckZ.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 2000", "session": "2000", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/KrwLfVEkFwxJiQtA.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"},
    {"titre": "Enoncé Philosophie série A 1999", "session": "1999", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/RzNsUooXytuUJHYk.pdf", "matiere": "Philosophie", "serie": "A", "type": "sujet"}
]

# Nouvelles données pour Philosophie série CD
NEW_PDFS_CD = [
    {"titre": "Enoncé Philosophie série CD 2011", "session": "2011", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/XyECWpyTgPFHKPcl.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 2010", "session": "2010", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/ZDvBoeMgeIqiFctz.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 2009", "session": "2009", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/BuThffVziGAIFDpk.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 2008", "session": "2008", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/OzHJwUeBQvnJDlUw.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 2007", "session": "2007", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/ggqNWCOeefaJcMkV.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 2005", "session": "2005", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/FBGpcnBulYxVXGlj.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 2004", "session": "2004", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/wkvjvtEBNeWhPTga.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 2003", "session": "2003", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/dhvdlXluzUsHnKpd.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 2002", "session": "2002", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/KVrLlCjlvKipCWdn.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 2000", "session": "2000", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/HaqTZHHXudosuhUb.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"},
    {"titre": "Enoncé Philosophie série CD 1999", "session": "1999", "url_pdf": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663511326494/zBTfmtQGSlhbGBCY.pdf", "matiere": "Philosophie", "serie": "C", "type": "sujet"}
]

DATA_FILE = '/home/ubuntu/education_madagascar/bac_madagascar_data.json'

def update():
    if not os.path.exists(DATA_FILE):
        return
        
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    existing_keys = set((item['titre'], item['session']) for item in data)
    
    added_count = 0
    for new_item in NEW_PDFS_A + NEW_PDFS_CD:
        if (new_item['titre'], new_item['session']) not in existing_keys:
            data.append(new_item)
            added_count += 1
            
    data.sort(key=lambda x: (x['matiere'], x['serie'], x['session']), reverse=True)
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Mise à jour terminée. {added_count} nouveaux éléments ajoutés.")

if __name__ == "__main__":
    update()

import os
import shutil

def folder_task():
    
    os.mkdir("Example")
    
    
    os.chdir("Example")
    os.mkdir("subdirect")
    
    
    
    image_path = input("Səkil faylının yolunu daxil edin: ")
    text_path = input("Text faylının yolunu daxil edin: ")
    
    
    shutil.move(image_path, "subdirect")
    shutil.move(text_path, "subdirect")
    
    
    for file_name in os.listdir("subdirect"):
        if file_name.endswith(".txt"):
            shutil.move(os.path.join("subdirect", file_name), ".")
            
    print("Folder taskı problemsiz icra edildi!")


folder_task()

# ------------------------------------------------------------------------------------------------------------------------------
def yeri_tap(xallar):
    
    siralama = sorted(enumerate(xallar, 1), key=lambda x: x[1])
    
    yerler = [None] * len(xallar)
    
    for indeks, (yer, _) in enumerate(siralama):
        yerler[indeks] = f"{yer}-ci"
    
    return yerler


xallar = [5, 3, 4, 2, 1]

print(yeri_tap(xallar))


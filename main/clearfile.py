def clearFile():
    file = open('mouse_log2.txt','w') 
    file.write("") 
    file.close()

if __name__ == "__main__":
    clearFile()
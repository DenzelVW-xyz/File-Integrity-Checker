import os
import hashlib
import json
from select_options import Select
options = ["Scan", "Check"]

selected = Select(options, prompt="Choose an option")

single = selected.run()
print(f"You selected: {single}")

if single == "Scan":
    directory = os.path.expanduser(input("Directory to scan: "))
    
    hashes = {}
    
    for root, directories, files in os.walk(directory):
        for filename in files:
            full_path = os.path.join(root, filename)
            
            with open(full_path, "rb") as opened_file:
                content = opened_file.read()
                hashed_content = hashlib.sha256(content).hexdigest()
                hashes[full_path] = hashed_content
                
        
    with open("baseline.json", "w") as file:
        json.dump(hashes, file, indent=4)
        
elif single == "Check":
    directory = os.path.expanduser(input("Directory to check: "))
    
    with open("baseline.json", "r") as file:
        baseline = json.load(file)

    for file_path in baseline:
        file_exists = os.path.exists(file_path)
        
        if file_exists:
            
            with open(file_path, "rb") as opened_file:
                content = opened_file.read()
                current_file_hash = hashlib.sha256(content).hexdigest()
                
                if baseline[file_path] == current_file_hash:
                    print(f"{file_path}", ":", "OK")
                else:
                    print(f"{file_path}", ":", "Changed")
                    
        elif not file_exists:
            print(f"{file_path}", ":", "Deleted!")
            
    for root, directories, files in os.walk(directory):
        for filename in files:
            full_path = os.path.join(root, filename)
                
            if full_path not in baseline:
                print(f"{full_path} : NEW!")
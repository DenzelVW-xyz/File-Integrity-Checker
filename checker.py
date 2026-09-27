import os
import hashlib
import json
from select_options import Select
options = ["Scan", "Check"]

selected = Select(options, prompt="Choose an option")

single = selected.run()
print(f"You selected: {single}")

if single == "Scan":
    directory = input("Directory to scan: ")
    
    hashes = {}
    
    for root, directories, files in os.walk(directory):
        for filename in files:
            full_path = os.path.join(root, filename)
            
            with open(full_path, "rb") as opened_file:
                content = opened_file.read()
                hashed_content = hashlib.sha256(content).hexdigest()
                hashes[full_path] = hashed_content
                
        
    with open("baseline.json", "w") as file:
        json_file = json.dump(hashes, file, indent=4)
                
    
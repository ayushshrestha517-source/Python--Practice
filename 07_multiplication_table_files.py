# write table from 2 to 20 and store in different files under a common folder
import os

os.makedirs("Table", exist_ok=True)  # ensures folder exists

for i in range (2,21):
    
    with open(f"Table/Table for {i}.txt","w") as f: 
        for j in range (1,11):
        
            f.write(f"{i} X {j} = {i*j}\n")

print("Program executed.")

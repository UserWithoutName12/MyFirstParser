import requests
import time
import os
'''
This function writes the site status code to the file, as well as the exact time when the page was dumped
'''
def kodstatusa_and_time():
    print("Enter the path to the file")
    print("For OC Windows drive:\directory")
    print("For Linux /home/username/") # Note for correct entry of the save path
    filepath = input("Enter the path to save the file:") # Entering the required variables
    path_url = input("Enter the path of the site:") 
    current_time = time.localtime()
    current_time = time.strftime("%H:%M:%S", current_time) # Finding the current time
    kodstatusa = requests.get(path_url) # Make a .get request to the page, for the status code
    kod = kodstatusa.text # Write the page code to the variable
    file_path = os.path.join(filepath, "output.txt") # function for working with the file system, where the path of saving and the name of the file are specified
    with open(file_path, 'w', encoding='utf-8') as f: # Write the variables above to the file
        f.write(f'Current time:{current_time}\n')
        f.write(f'Status Code:{kodstatusa}\n')
        f.write(f'Page code\n{kod}')
        print("The file has been successfully saved!")
kat = kodstatusa_and_time()
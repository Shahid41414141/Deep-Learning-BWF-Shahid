try:
   
    with open('Task 9/input.txt', 'r') as input_file:
       
        contents = input_file.read()

       
        contents_upper = contents.upper()

 
    with open('Task 9/output.txt', 'w') as output_file:
        
        output_file.write(contents_upper)

except FileNotFoundError:
    
    print("File not found!")

except Exception as e:
    
    print("An error occurred: ", e)

finally:
    
    try:
        input_file.close()
    except:
        pass

    try:
        output_file.close()
    except:
        pass

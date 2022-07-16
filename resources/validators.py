from django.core.exceptions import ValidationError

def valid_file_type_for_documents(value):
    file = str(value)
    if file.endswith('.pdf') != True and file.endswith('.doc') != True and\
        file.endswith('.docx') != True and file.endswith('.rtf') != True and\
        file.endswith('.xlsx') != True and file.endswith('.zip') != True\
        and file.endswith('.rar') != True and file.endswith('.ppt') != True \
            and file.endswith('.pptx') != True:
        raise ValidationError(f"file types isn't supportable")
    else:
        return file
    
def valid_file_size_for_documents(value):
 
    size_limit = 2621440 #2.5 mb
    if value.size > size_limit:
        raise ValidationError("Max file size mustn't be more than 2.5 mb")
    else:
        return value
import re

for i in range(10):
    file_path = r'<test.py에서 저장된 파일경로>' % i
    try:
        with open(file_path, 'rt', encoding='utf-8') as f:
            RG_line = f.read()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다. 다음 파일로 넘어갑니다.")
        continue

    cleaned_line = re.sub(r'o/|n/|d/|\(\)|\)|\(|/', '', RG_line)
    cleaned_line = re.sub(r'\s+', ' ', cleaned_line).strip()  

    output_file_path = r'<마무리된 파일 저장할 위치 및 파일 이름>' % i
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_line)
        
    print(f"성공적으로 저장되었습니다.")

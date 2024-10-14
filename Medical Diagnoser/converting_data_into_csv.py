import urllib.request
import ssl


context = ssl._create_unverified_context()
data = urllib.request.urlopen(
    "https://raw.githubusercontent.com/adil200/Medical-Diagnoser/main/medical_data.csv", 
    context=context
)
csv_content = data.read().decode('utf-8')


file_path = '/Users/bahodirnematjonov/Desktop/AI-Machine-Learning-Deep-Learning-Computer-Vision/Medical Diagnoser/medical_data.csv'
with open(file_path, 'w') as file:
    file.write(csv_content)

file_path

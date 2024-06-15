import requests
import json

# Define the API endpoint
url = "http://127.0.0.1:5000/similarity"

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Define the payload

# text 1 is the job description
# text 2 is the resume of the candidate
payload = {
    "text1": '''Bachelor's degree in Engineering, Information Systems, Computer Science, or a related field.
		10+ years of experience in Software Engineering or a related field.
		10+ years of experience with programming languages such as C, C++, Python, etc.
		Desired Skills and Aptitudes
		Solid theoretical understanding of model architectures for various applications, including object classification, object detection, recommender systems, NLP, text and voice processing models, and 3D models.
		Experience in designing new Neural Network architectures tailored to specific use cases and utilizing appropriate datasets to achieve target accuracies.
		Proactive attitude, with the ability to analyze and anticipate trends in neural network technologies and techniques.
		In-depth knowledge of various model quantization techniques.
		Comprehensive understanding of model pruning and compression techniques.
		Strong foundation in mathematical statistics, probability theory, and linear algebra as they relate to Machine Learning and Deep Neural Networks.
		Familiarity with traditional Machine Learning methods such as Linear & Logistic regression, SVM, Kernel methods, Decision trees, and ensemble techniques like Bagging and Boosting.
		Ability to evaluate performance and accuracy metrics for different classes of neural networks.
		Background in hardware architectures, including GPUs and AI accelerators like TPUs, is a plus.
		Proficiency in C++ and Python development.
		Extensive hands-on experience with Deep Learning frameworks such as PyTorch and TensorFlow.
		Excellent communication skills (both written and verbal) and a collaborative 	team player.
		Minimum Qualifications
		Bachelor's degree in Engineering, Information Systems, Computer Science, or a related field.
		2+ years of experience in Software Engineering or a related field.
		2+ years of experience with programming languages such as C, C++, Python, etc.
		Additional Job Description
		Bachelor's degree in Engineering, Information Systems, Computer Science, or a related field.
		10+ years of experience in Software Engineering or a related field.
		10+ years of experience with programming languages such as C, C++, Python, etc.''',
		
		
    "text2": '''
    		EXPERIENCE 
Full stack Developer | MIT School of Research and Consultancy 
APRIL 2019 - PRESENT   
MITRC is a web portal for researchers and PhD students of MIT ADT University. Portal 
consists of different forums, publication/library, submissions,progress, profile etc. feature 
which also includes data analysis and data visualisation of students and their progress. It's 
development work i.e frontend and backend is being done by us. 
 EDUCATION 
B.Tech Information Technology  | MIT School of Engineering 
JUNE 2017 –  JUNE 2021 
CGPA: 8.12 
HSC | Nowrosjee Wadia College of Arts and Science. 
2015 - 2017 
Percentage: 68.64% 
SSC | Stella Maris High School. 
2015 
Percentage: 90.20% 
 PROJECTS 
Sahayak- AI Enabled citizen grievance monitoring system  |Github repo. 
Smart maintenance is a web app which is implemented using different deep learning algorithms 
to report garbage and potholes in the campuses, which uses trained AI model to identify the 
problem and classify them into garbage and potholes and report it to the respective officers.  
https://www.linkedin.com/in/vinayak-sutar-813039197/
https://github.com/vsutar1451
https://github.com/ramsuthar305/Smart-Maintenance
Knowledge Sharing platform for Ministry of labor India |Github repo.   
Knowledge sharing platform is based on a problem statement given by the Ministry of 
Labour India in Smart India Hackathon 2019 to help labour know the latest technology and 
laws by the constitution on real time basis with a law dictionary feature. 
 SKILLS 
 Familiar with:  
 C 
 Cpp 
 JS 
 Django 
 Sqlite 
 Mongodb 
 Proficient in: 
 Python3 
 Flask 
 ACHIEVEMENT 
1. Winner in Smart India Hackathon (SIH) 2019.  
2. Winner in Intra department Technical presentation competition. 
 MANAGEMENT 
Codebreak1.0 - National level onsite hackathon |Organizer. 
Organised codebreak1.0 onsite hackathon which received more than 1000 applicants from all 
over India. 
Humanoid walking robot workshop cum competition | Student Organizer. 
Organised and managed National level Humanoid walking robot workshop in association with 
Eduxlab and IIT Roorkee. 
GameZone, MIT ADT Persona Fest 2018 |Organizer. 
Organised National level gaming competition, managed more than 2000 participants. 
Tech talk by Gaurav Sen |Organizer. 
Organised technical talk on Competitive programming and interview cracking by Gaurav Sen for 
students of MIT ADT University. 
    '''
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)


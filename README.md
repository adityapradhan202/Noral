# Noral
Noral is an AI driven oral healthcare appointment system. It's a web application that utilizes image classification CNN models and NLP models in the backend to automate tasks typically performed by intermediary staff in large dental clinics.

### 🎥 Video Recording:
To see the working of this project you can checkout this video ➡️ [Noral Walkthrough](https://drive.google.com/file/d/1MZ5s4q2UaHbkCdMW069P23HlBUsFhwl6/view?usp=sharing)

### Project PPT:
Go through this presentation to understand the real world problem statement and it's solution ➡️ [Presentation](https://www.canva.com/design/DAGrok7CTHk/0eUHwfpAI9X-KzyUkecNCQ/view?utm_content=DAGrok7CTHk&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=haa1e633909)  
**Also don't forget to watch the video recording mentioned above.**

### Overal workflow:
![workflow](https://github.com/adityapradhan202/Noral/blob/main/readme_images/Copy%20of%20pe-1%20PPT%20updated%20R2.png)

### Dependencies:
This is the list of inbuilt and external modules that will be required to run this project on your local machine:-
1. Flask
2. Streamlit
3. Pathlib
4. Numpy
5. Pandas
6. Scikit-learn
7. Joblib
8. Pytorch version 2+ (cuda support recommended, otherwise cpu version will also work)
7. Tqdm
8. PIL
9. Requests
10. IO

### Steps for running this on local machine:
1. Clone the repository using the command command in the git bash terminal `git clone https://github.com/adityapradhan202/Noral.git`.
2. `./Noral/Models` folder contains all the saved models and paramters of the custom trained pre-trained models.
3. The project uses the pretrained model [efficient_net_b0](https://docs.pytorch.org/vision/main/models/generated/torchvision.models.efficientnet_b0.html#torchvision.models.efficientnet_b0). So make sure you download the before hand using pytorch.  
**A quick guide on how to download this model:**
```py
import torch
import torchvision

# This line if check if model is already present in torchvision cache directory or not.
effnet_model = torchvision.models.efficient_b0(
    pretrained=True
)
```
4. Run [dbcreate.py](https://github.com/adityapradhan202/Noral/blob/main/dbcreate.py) to create a database.
5. Now we need to run two Flask APIs before running the main app.
6. First run the [nb_nlp_flask.py](https://github.com/adityapradhan202/Noral/blob/main/nb_nlp_flask.py) in a terminal.
7. Secondly run the [cnn_pipeline_flask.py](https://github.com/adityapradhan202/Noral/blob/main/cnn_pipeline_flask.py) in another terminal.
8. Now run the [app.py](https://github.com/adityapradhan202/Noral/blob/main/app.py) using the command `streamlit run app.py` file.
9. Now you can use Noral just like shown in the video tutorial ➡️ [Noral Walkthrough](https://drive.google.com/file/d/1MZ5s4q2UaHbkCdMW069P23HlBUsFhwl6/view?usp=sharing)

### Further improvements:
For further improvement, this AI driven system can be hosted on cloud and integrated with a fully functioning full stack website.

### Publication:
This project has been published as a research paper on **[IJIRCCE](https://ijircce.com/admin/main/storage/app/pdf/7rUnXm1zcnu4s05s07tYOWFS5XqLAnj3H2MgEP1P.pdf)**, **[Research Gate](https://www.researchgate.net/publication/387089433_Noral_AI-Driven_Oral_Healthcare_Appointment_System)** and is also listed and accessible through **[Google-Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Noral%3A+AI+Driven+Oral+Healthcare+Appointment+System&btnG=)**.



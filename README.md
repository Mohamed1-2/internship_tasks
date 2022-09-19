# $${\color{green}Welcome 👐 🤠 \space \color{lightblue}}$$ $${\color{green}To \space \color{lightblue}}$$ $${\color{green}My \space \color{lightgreen} internship }$$ $${\color{green}repo 📔 }$$  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![stuart-in-course-unscreen](https://user-images.githubusercontent.com/34875234/189671078-734118a7-a773-4f07-80d5-e54e2e1b334d.gif) 


I completed a 6-month  internship from March 2022 to September 2022 with AI Team in **Sophic Automation** . This repository contains the work that I completed throughout the period of this intership  

# Tasks 👨‍💻
- ## [Task 1](https://github.com/Mohamed1-2/internship_tasks/tree/main/gauge_reader)
  - **Task Overall** 📋
  
     | Project name | Description |
     | --- | --- |
     | Gauge reader | reading value of a analogue gauge using open CV script from real time video and images|
  - **Features** ✨
      - **gauge needle Detector** 🕶
           * contrast level 
           * ROI extraction
           * Gamma Correction
           * Circle Detection
           * Gaussian Smoothing
           * Grayscaling 
           * Canny Edge Detection
           
  -  **Demo** 🖼️
      -  Image 
         #### <img src="https://user-images.githubusercontent.com/34875234/189685455-23ce2854-ee39-47f3-82c3-98ca9279be0f.jpeg" alt="Image" width="250"/>
        
      -  Video
         #### <img src="https://user-images.githubusercontent.com/34875234/189687456-7465803a-b216-4715-9032-0eac025d38ea.gif" alt="gif" width="550"/>


* ## [Task 2](#team-members)

| Project name | Description |
| --- | --- |
| Water surface detection 💧 | trained transfer learning model to detect Water surface in pumphouse and draw a mask around water surface class using MASK-RCNN model |
  - **Model Result** 🥳
     | **number of steps** | **val loss value** |  
     | --- | --- |
     | 1 |0.975083411
     | 2|0.646316946
     |3 |0.603483021
     | 4|0.601662695

     
  -  **Demo 🖼️** 
        -  Video
           #### <img src="https://user-images.githubusercontent.com/34875234/190196592-06d1b704-0148-49ab-a201-cd15e82277ee.gif" alt="gif" width="550"/>
  -  **Procedure** 🧾
       1. 150 images were taken from the recorded videos of a pumphouse point after they were converted to footage.
       2. Annotated the footages using [makesense.ai](https://www.makesense.ai/) which is an online annotation tool.
       3. Built a model to detect masks on water surface images.
   -  **How To ❓**
         - **steps**
           |**1-Dataset**          | **2-Annotation**         | 3- **model configuration**          |**4-Train**          |**5-Test**          |**6-repate**         | 
           | --- | --- | --- | --- | --- | --- |
           |a small dataset used contains around 150 images taken from 2 different videos |Annotate the entire dataset in coco format  using a polygon shape |Before training the dataset modify the confieg function   | In order to train the model you need to download the Mask Rcnn trained weights from [here](https://drive.google.com/file/d/1HFLlPs-8yXu-30hkU920liAvMgOLc5kW/view?usp=sharing) and modify the epochs numbers ,start with 2 epochs and see if the model improved then add more epochs.| Test the model on real-world visual data that is not annotated | repeat steps 4 and 5 until you get high accurate model           **_NOTE:_** Better to use Tensorboard|
           |    [Dataset Link](https://drive.google.com/drive/folders/16J4JmzTWBp2-YCivTmWgllaJLDeYl5oS?usp=sharing)       | <img src="https://user-images.githubusercontent.com/34875234/190351355-ed81da70-e8a0-402d-9e6a-a642ed147b19.gif" alt="gif" width="500"/> |  ```  class myMaskRCNNConfig(Config): NUM_CLASSES = 1 + 1 STEPS_PER_EPOCH = 100 DETECTION_MIN_CONFIDENCE = 0.85 ``` | | [Test dataset Link](https://drive.google.com/drive/folders/1qYXXTgcR77F_4sdiMveo97CqwBtl_idx?usp=sharing) |
   -  **requirements ⚠️**
       - **Need Python 3.5 or later with all the following dependencies installed :**
     
     
     tensorflow==1.13.1
     h5py==2.10.0
     keras==2.0.8
     scikit-image==0.16.2
     opencv-python
     Pillow==8.0.1
     pandas
     numpy
   
   - **Run on Colab** 🟡
       
       The easiest way is to open [notebook](https://colab.research.google.com/drive/1jc5ooTPvBkSFfGayduBd0Xg1YQseZnIk?usp=sharing)

   - **Run Locally** 💻
   
       Clone or download this repo :
       
           git clone https://github.com/Mohamed1-2/internship_tasks    
       To start the notebook in jupyter run the command line in the project start:
       
           jupyter notebook
       
       Then open **Train_Mask_RCNN_MODEL_FOR_WATER_SURFACE_DETECTION.ipynb** in the browser 
       
       
   



* ## [Task 3](#team-members)

| Project name | Description |
| --- | --- |
| Identity card detection 👁️| The aim of the project is to detect employees id cards of westren digital company using MASK-RCNN and extract employees id numbers using opencv techniques .  |

  - **Model Result** 🥳
     | **number of steps** | **val loss value** |  
     | --- | --- |
     | 1 |0.871458054
     | 2|0.616355062
     |3 |0.391975462
  -  **Demo 🖼️** 
       -  Images 
           #### <img src="https://user-images.githubusercontent.com/34875234/190845243-6718f760-f1b5-4add-87b4-54a238fa620a.jpg" alt="imag1" width="150"/><img src="https://user-images.githubusercontent.com/34875234/190845245-151c249e-5d92-48d6-990f-33a1874bd392.jpg" alt="imag2" width="150"/><img src="https://user-images.githubusercontent.com/34875234/190845477-023c27f2-329e-49ec-bd30-af1cd99f482d.jpg" alt="imag2" width="150"/><img src="https://user-images.githubusercontent.com/34875234/190845485-dd833028-29d9-4646-aa66-38464886c47e.jpg" alt="imag2" width="150"/><img src="https://user-images.githubusercontent.com/34875234/190868935-7b84effa-75df-4e39-ab36-0d75112367a0.png" alt="imag2" width="150"/><img src="https://user-images.githubusercontent.com/34875234/190868938-7cd84682-3d12-4fe6-abd2-3f4c57743db5.png" alt="imag2" width="150"/>




        -  Video
           #### <img src="https://user-images.githubusercontent.com/34875234/190903758-fc80df46-a920-498d-a963-229352dd480f.gif" alt="gif" width="550"/>


  -  **Procedure 🧾** 

       1. a very small dataset used with 20 images for employees IDs .
       2. Annotated the company logo from the images using the same tool that used in the prevoius project .
       3. Built a model to detect bounding box on id cards images.
       4. yolo object detection used to detect the employee image.
       5. extract the text from the card using opencv ocr tesseract.
       
   -  **Method 🛠**
         - **For logo detection** 
              Mask-rcnn model built using the same steps in task 2, the model will draw a boundary box on the logo if detected, then we used the logo's boundary box and multiplying it by 3 in lengths,the new boundary box will be the region of interest . So we'll crop that region for the next step.

              - **detected card: (example)** :      
                  #### <img src="https://user-images.githubusercontent.com/34875234/190917384-b6d5565d-093b-4d30-9a6c-7b82a2d382cf.jpg" alt="img" width="350"/>
                  #### <img src="https://user-images.githubusercontent.com/34875234/190917256-9b92dcfa-7c90-4e09-a7e7-33a3ffdca75b.jpg" alt="img" width="350"/>

         - **For ID number detection**
               I used yolo to detect the employee's photo, then if the id contains an image, take the image's boundary box and multiply it by 2 in length then crop the image.
              - **Cropped card ROI: (example)** :
                  #### <img src="https://user-images.githubusercontent.com/34875234/190915295-e0d926a0-b1d8-457a-bbe7-9660e08d4d9b.jpg" alt="img" width="350"/>

         - **For Text extraction** 
             Using **opencv ocr tesseract** on the cropped image after grayscale it to extract whole the text under the image including the employee name. Text is filtered to only keep numbers in the length of 5 numbers or more.  
              
              - **grayscale Cropped card: (example)** :
                  #### <img src="https://user-images.githubusercontent.com/34875234/190922123-5cceb660-7e5c-4420-b380-42c79b7cca17.jpg" alt="img" width="350"/>
   - **Run on Colab** 🟡
   
        Run
        
        ```python 
        wget https://pjreddie.com/media/files/yolov3.weights
        ```
      
        in root project directory to get yolo weights

        
        Then open [notebook](https://colab.research.google.com/drive/17OBnGGGkGkUGFT_LfaC0fRqLvaHjuOgj?usp=sharing)

   - **Run Locally** 💻
  
      
        To run the project locally follow the same steps in Task 2.


* ## [Task 4](#team-members)

| Project name | Description |
| --- | --- | 
| vehicle and pedestrians detection | Using openvino pre-trained model to detect vehicle and pedestrians in videos  |

  -  **Demo 🖼️** 

        #### <img src="https://user-images.githubusercontent.com/34875234/190944917-c7143852-1715-400a-9b5c-3f547cf92e9e.gif" alt="gif" width="550"/>


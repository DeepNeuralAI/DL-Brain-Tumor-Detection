# Brain Tumor Detection

The following web application was built using Flask.

The machine learning model relies on transfer learning from resnet 50. 

The basic principle is to keep all the convolutional layers with their weights pretrained. 

We then only train the head of the model initially. Later, we unfreeze the layers and start the process of fine-tuning using differential learning rates.

![cnn](https://miro.medium.com/max/3480/1*uUYc126RU4mnTWwckEbctw@2x.png)

Dependencies:
- fast.ai 
- flask
- tailwind

![image](https://user-images.githubusercontent.com/34294344/68198182-aae70e00-000f-11ea-8658-85483b66bee4.png)

![image](https://user-images.githubusercontent.com/34294344/68198587-71fb6900-0010-11ea-94f4-e0301e53ba95.png)

![image](https://user-images.githubusercontent.com/34294344/68198627-82134880-0010-11ea-8d38-6646c3c518a1.png)


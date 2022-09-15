import cv2
import os
file_names = []

for each in os.scandir():
	
	if each.name.endswith('.mp4'):
		file_names.append(each.name.split('.')[0])

for file_name in file_names:

	print(file_name)

	vidcap = cv2.VideoCapture(f'{file_name}.mp4')
	success,image = vidcap.read()
	count = 0
	step = 100

	for num in range(1,22500,step):

			if success:
				cv2.imwrite(f"images/{file_name}_frame%d.jpg" % count, image)     # save frame as JPEG file      
				
				vidcap.set(cv2.CAP_PROP_POS_FRAMES, num)
				success,image = vidcap.read()
				count += 1
			else:

				pass

# while success:
# 	if step == skip :
# 		print(f'in frame {step}' )

# 		cv2.imwrite("images/frame%d.jpg" % count, image)     # save frame as JPEG file      
# 		success,image = vidcap.read()
# 		# print('Read a new frame: ', success)

# 		count += 1

# 		step = 1

# 	else:
# 		success,image = vidcap.read()

# 		print(f'in else {step}')

# 		step +=1
# 		continue





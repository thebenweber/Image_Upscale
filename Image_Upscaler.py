#imports
import cv2
import glob
#initial folder path
folder_name="folder_name"
#gets paths for all images in folder
paths = glob.glob(folder_name+"/*")
#count to number the photos
count =0
#loop through all photos in folder
for i in paths:
    #read image
    img = cv2.imread(i,1)
    #resize fx is the multiplier/ scale value
    img_scale_up = cv2.resize(img, (0, 0), fx=10, fy=10)
    #increase count
    count +=1
    #print(count)
    #change folder_name as a string, "example" to make custom name/ defaulted to folder name + number
    filename = (str(folder_name+str(count))+".jpg")
    #save image to output_folder path
    cv2.imwrite(r"output_folder/"+filename, img_scale_up)
#print done when for loop ends
print("Done")
#close cv2
cv2.waitKey(0)
cv2.destroyAllWindows()
import pydicom
import matplotlib.pyplot as plt


directory = "1-03.dcm"
dicom_data = pydicom.dcmread(directory)
img = dicom_data.pixel_array


plt.subplot(), plt.title(f"{directory}"), plt.imshow(img, cmap='gray')
plt.show()
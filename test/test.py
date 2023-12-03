import cv2
from scipy import io
import imageio
import matplotlib.pyplot as plt

# Đường dẫn của ảnh
image_path = 'static/images/Albert-Einstein.jpg'

# Đọc ảnh bằng cv2
img_cv2 = cv2.imread(image_path)

# Chuyển định dạng màu từ BGR sang RGB
# img_cv2_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)

# Đọc ảnh bằng scipy.io
img_scipy = imageio.imread(image_path)

# Hiển thị ảnh
plt.subplot(121)
plt.imshow(img_cv2)
plt.title('OpenCV')

plt.subplot(122)
plt.imshow(img_scipy)
plt.title('scipy.io')

plt.show()

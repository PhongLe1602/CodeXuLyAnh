import os
from flask import Flask, render_template, request
import cv2
import matplotlib.pyplot as plt 
import imageio
import math
import numpy as np
from PIL import Image


from ToanTuDiemAnh import image_negative
from ToanTuDiemAnh import log_transformation
from ToanTuDiemAnh import threshold_transformation
from BoLoc import median_filter
from ToanTuDiemAnh import histogram_equalization
from PhatHienBien import laplacian
from ToanTuDiemAnh import exponential_transformation
from BoLoc import weighted_average_filter
from BoLoc import filter_average_k_cloest_values
from PhatHienBien import operator_roberts
from PhatHienBien import operator_sobel
from PhatHienBien import operator_prewitt
from PhatHienBien import method_canny
from PhatHienBien import algorithm_ostu
from NenAnh import compress_image_rlc
from XuLyHinhThai import photo_shrink
from XuLyHinhThai import image_dilation
from XuLyHinhThai import open_image
from XuLyHinhThai import close_image
from NenAnh import huffman
from NenAnh  import lzw





# https://github.com/Akhilesh64/Image-Processing/blob/master/Laplacian%20Edge%20Detection/Image.jpg
# https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian/laplacian.jpg
app = Flask(__name__)
@app.route('/')
def view():
    return render_template('view.html')

@app.route('/submit', methods=['POST'])
def submit():
    selected_option = request.form.get('options')
    print(selected_option + ' hihii')
    
    

    if 'image' in request.files:
        image = request.files['image']
        image_path = save_uploaded_image(image)
        print(image_path)
        img_bgr = cv2.imread(image_path, 1) 
        #Lấy ảnh từ tên gốc
        file_name, file_extension = os.path.splitext(os.path.basename(image_path))
        
        
        # Biến đổi âm bản
        if selected_option == 'image_negative':
            img_bgr = image_negative.tranfer_negative(img_bgr)
        # Biếm đổi Log
        elif selected_option == 'log_transformation':
            img_bgr = log_transformation.transfer_log(img_bgr)
        # Bộ lọc phân ngưỡng
        elif selected_option == 'thresholding':
            img_bgr = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            threshold_value = request.form.get('threshold')  # Lấy giá trị threshold từ form
            img_bgr = threshold_transformation.transfer_thresholding(img_bgr,int(threshold_value))
        # Bộ lọc trung vị
        elif selected_option == 'median_filter':
            print('phongleeee')
            img_bgr = cv2.imread(image_path, 0)
            img_bgr = median_filter.MedianFilter(img_bgr,7)
        # Nâng cao chất lượng ảnh
        elif selected_option == 'histogram_equalization':
            img_bgr = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
            img_bgr = histogram_equalization.histeq(img_bgr)
        # Cạnh góc
        elif selected_option == 'laplacian':
            img_bgr = cv2.imread(image_path,0)
            img_bgr = laplacian.conv2d(img_bgr,laplacian.conv_kernel)
        
        elif selected_option == 'exponential_transformation':
            # img_bgr = cv2.imread(image_path)
            
            # img_bgr = cv2.cvtColor(img_bgr, cv2.IMREAD_GRAYSCALE)
            img_bgr = imageio.imread(image_path)
            img_bgr = exponential_transformation.ExpTran(img_bgr)
        
        elif selected_option == 'weighted_average':
            img_bgr = cv2.imread(image_path)
            img_bgr = weighted_average_filter.transfer_weighted_average(img_bgr)
        # Lọc trung vị với k giá trị nhỏ nhất
        elif selected_option == 'knn_average':
            img_bgr = cv2.imread(image_path)
            img_bgr = filter_average_k_cloest_values.transfer_knn(img_bgr)
        # Toán tử Roberts
        elif selected_option == 'roberts':
            img_bgr = cv2.imread(image_path)
            img_bgr = operator_roberts.transfer_robert(img_bgr)
        # Toán tử Sobel
        elif selected_option == 'sobel':
            img_bgr = cv2.imread(image_path)
            img_bgr = operator_sobel.transfer_sobel(img_bgr)
        # Toán tử Prewitt
        elif selected_option == 'prewitt':
            img_bgr = cv2.imread(image_path)
            img_bgr = operator_prewitt.transfer_prewitt(img_bgr)
        # Phương pháp Canny
        elif selected_option == 'canny':
            img_bgr = cv2.imread(image_path)
            img_bgr = method_canny.transfer_canny(img_bgr)
        # Thuật toán Ostu
        elif selected_option == 'ostu':
            img_bgr = cv2.imread(image_path)
            img_bgr = algorithm_ostu.transfer_ostu(img_bgr)
        # Nén ảnh bằng RLC
        elif selected_option == 'rlc':
            img_bgr = Image.open(image_path).convert('L')
            
            # img_bgr = cv2.imread(image_path)
            
            # img_bgr = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
            encode_data = compress_image_rlc.rlc_encode(img_bgr)
            
        # Co ảnh
        elif selected_option == 'erosion':
            img_bgr = cv2.imread(image_path)
            img_bgr = photo_shrink.transfer_shrink(img_bgr)
        # Giãn ảnh
        elif selected_option == 'dilation':
            img_bgr = cv2.imread(image_path)
            img_bgr = image_dilation.Transfer_dilation(img_bgr)
        # Mở ảnh
        elif selected_option == 'opening':
            img_bgr = cv2.imread(image_path)
            img_bgr = open_image.Open_image(img_bgr)
        # Đóng ảnh
        elif selected_option == 'close':
            img_bgr = cv2.imread(image_path)
            img_bgr = close_image.Close_image(img_bgr)
        # Nén ảnh bằng thuật toán Huffman
        elif selected_option == 'huffman':
            img_bgr = Image.open(image_path).convert('L')
            bitset, huffman_tree = huffman.huffman_compress(img_bgr)
             # Nén ảnh bằng thuật toán LZW
        elif selected_option == 'lzw':
            img_bgr = Image.open(image_path).convert('L')
            bitset, dictionary = lzw.compress_lzw(img_bgr)
            
            

            
        
        if selected_option =='rlc':
            values = 1
            return render_template('result.html',
                               origional_image_path=image_path,encode=encode_data, selected_option=selected_option,value = values)
        elif selected_option in ['huffman', 'lzw']:
            values = 2
            # bitset = 200
            bitset = len(bitset)
            return render_template('result.html',
                               origional_image_path=image_path,bit = bitset, selected_option=selected_option,value = values)
        else:
            # Tạo tên mới cho ảnh đã xử lý
            print(file_name,file_extension)
            new_image_path = os.path.join(app.config['UPLOAD_FOLDER'], f'{file_name+'_'+selected_option}{file_extension}')
            cv2.imwrite(new_image_path, img_bgr)
            # print(new_image_path)
            values = 0
            return render_template('result.html',
                                origional_image_path=image_path,new_image_path=new_image_path, selected_option=selected_option,value = values)
            
        








app.config['UPLOAD_FOLDER'] = 'static/images'

def save_uploaded_image(file):
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_path)
    return image_path

if __name__ == '__main__':
    app.run(debug=True)

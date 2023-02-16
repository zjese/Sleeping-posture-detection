from libkinect2 import Kinect2
from libkinect2.utils import ir_to_image, depth_map_to_image, draw_skeleton
import numpy as np
import cv2
import os

# 骨骼数据集
dataset_skeleton_path = "./sleep_skeleton_dataset/"
if not (os.path.exists(dataset_skeleton_path)):
    os.mkdir(dataset_skeleton_path)

for i in range(5):
    class_skeleton_path = dataset_skeleton_path + str(i)
    if not (os.path.exists(class_skeleton_path)):
        os.mkdir(class_skeleton_path)
# 深度数据集
dataset_depth_path = "./sleep_depth_dataset/"
if not (os.path.exists(dataset_depth_path)):
    os.mkdir(dataset_depth_path)

for i in range(5):
    class_depth_path = dataset_depth_path + str(i)
    if not (os.path.exists(class_depth_path)):
        os.mkdir(class_depth_path)
# 红外数据集
dataset_ir_path = "./sleep_ir_dataset/"
if not (os.path.exists(dataset_ir_path)):
    os.mkdir(dataset_ir_path)

for i in range(5):
    class_ir_path = dataset_ir_path + str(i)
    if not (os.path.exists(class_ir_path)):
        os.mkdir(class_ir_path)
# 普通图像数据集
dataset_normal_path = "./sleep_normal_dataset/"
if not (os.path.exists(dataset_normal_path)):
    os.mkdir(dataset_normal_path)

for i in range(5):
    class_normal_path = dataset_normal_path + str(i)
    if not (os.path.exists(class_normal_path)):
        os.mkdir(class_normal_path)

# Init kinect w/all visual sensors
kinect = Kinect2(use_sensors=['color', 'depth', 'ir', 'body'])
kinect.connect()
kinect.wait_for_worker()

data_counter = 0
class_number = 0

for _, color_img, depth_map, ir_data, bodies in kinect.iter_frames():
    # 骨骼图像
    body_img = np.zeros(color_img.shape)
    for body in bodies:
        draw_skeleton(body_img, body)
    body_img = cv2.resize(body_img, (512,512))
    cv2.imshow('skeleton',body_img)
    # 深度图像
    depth_img = depth_map_to_image(depth_map)
    depth_img = cv2.resize(depth_img, (512,512))
    # cv2.imshow('depth',depth_img)
    # 红外图像
    ir_img = ir_to_image(ir_data)
    ir_img = cv2.resize(ir_img, (512,512))
    # cv2.imshow('ir', ir_img)
    # 普通图像
    normal_img = color_img
    normal_img = cv2.resize(normal_img, (512,512))
    # cv2.imshow('normal', normal_img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        # 保存骨骼图像
        file_skeleton_name = dataset_skeleton_path + str(class_number) + "/" + "%03d.jpg" %data_counter
        cv2.imwrite(file_skeleton_name,body_img)
        # 保存深度图像
        file_depth_name = dataset_depth_path + str(class_number) + "/" + "%03d.jpg" %data_counter
        cv2.imwrite(file_depth_name,depth_img)
        # 保存红外图像
        file_ir_name = dataset_ir_path + str(class_number) + "/" + "%03d.jpg" %data_counter
        cv2.imwrite(file_ir_name,ir_img)
        # 保存普通图像
        file_normal_name = dataset_normal_path + str(class_number) + "/" + "%03d.jpg" %data_counter
        cv2.imwrite(file_normal_name,normal_img)
        print("saving picture %d" %data_counter)
        data_counter = data_counter + 1
    elif key == ord('n'):
        class_number = class_number + 1
        data_counter = 0
        print("saving class %d" %class_number)

kinect.disconnect()
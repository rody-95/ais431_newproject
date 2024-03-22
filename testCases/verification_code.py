from PIL import Image
import os
import numpy as np


# 生成黑白二值图片
def generate_binary_image(image_path):
    image = Image.open(image_path).convert("L")
    binary_image = image.point(lambda x: 0 if x < 128 else 255, "1")
    return binary_image


# 生成白底图片
def generate_white_background(image_path):
    image = Image.open(image_path)
    white_image = Image.new("RGB", image.size, (255, 255, 255))
    return white_image


# 切割图片
def crop_image(image):
    width, height = image.size
    pixels = image.load()
    start_x = None
    end_x = None
    cropped_images = []
    for x in range(width):
        for y in range(height):
            if pixels[x, y] == (0, 0, 0):
                if start_x is None:
                    start_x = x
                end_x = x
                break
        if start_x is not None and end_x is not None:
            cropped_image = image.crop((start_x, 0, end_x + 1, height))
            cropped_images.append(cropped_image)
            start_x = None
            end_x = None
    return cropped_images


# 存储切割出的图片
def save_cropped_images(cropped_images, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for i, cropped_image in enumerate(cropped_images):
        output_path = os.path.join(output_folder, f"{i}.png")
        cropped_image.save(output_path)


# 加载训练集
def load_training_set(training_set_folder):
    training_set = []
    for filename in os.listdir(training_set_folder):
        image_path = os.path.join(training_set_folder, filename)
        image = Image.open(image_path).convert("L")
        training_set.append(image)
    return training_set


# 计算向量空间模型
def calculate_similarity(image1, image2):
    histogram1 = image1.histogram()
    histogram2 = image2.histogram()
    similarity = np.sqrt(np.sum((np.array(histogram1) - np.array(histogram2)) ** 2))
    return similarity


# 验证码识别
def recognize_captcha(captcha_image_path, training_set_folder):
    binary_image = generate_binary_image(captcha_image_path)
    white_image = generate_white_background(captcha_image_path)
    cropped_images = crop_image(binary_image)
    save_cropped_images(cropped_images, training_set_folder)
    training_set = load_training_set(training_set_folder)

    result = ""
    for cropped_image in cropped_images:
        min_similarity = float('inf')
        min_index = -1
        for i, training_image in enumerate(training_set):
            similarity = calculate_similarity(cropped_image, training_image)
            if similarity < min_similarity:
                min_similarity = similarity
                min_index = i
        if min_index != -1:
            result += chr(ord('A') + min_index)

    return result


# 测试
captcha_image_path = r'C:\Users\Administrator\Desktop\镭晨科技\我的分享\PPT素材\验证码.jpg'
training_set_folder = r'C:\Users\Administrator\Desktop\镭晨科技\我的分享\PPT素材\结果.jpg'
result = recognize_captcha(captcha_image_path, training_set_folder)
print("识别结果:", result)

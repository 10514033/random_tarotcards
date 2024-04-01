from django.shortcuts import render
from django.conf import settings
import os
import random
from . import image_info


def index(request):
    images_dir = os.path.join(settings.BASE_DIR, 'static', 'images')
    # 获取文件夹中所有图片的路径
    images = [os.path.join(images_dir, image)
              for image in os.listdir(images_dir)]

    # print("Images in images_dir:", images)

    if request.method == 'POST':
        rws_selected = 'rws_images' in request.POST
        cardname_selected = 'cardname' in request.POST
        if request.POST.get('rws_images'):
            images = [image for image in images if os.path.basename(
                image).startswith('rws')]
        # 如果是 POST 请求，随机选择一张图片
        random_image = random.choice(images)
        image_name = image_info.image_info_dict.get(os.path.basename(
            random_image), {}).get('name', '')
        # print(image_name)
        image_upright = image_info.image_info_dict.get(os.path.basename(
            random_image), {}).get('upright', '')
        image_reversed = image_info.image_info_dict.get(os.path.basename(
            random_image), {}).get('reversed', '')

        random_image = random_image.split('\\')[-2:]
        # print(random_image[0]+'/'+random_image[1])
        random_image = random_image[0]+'/'+random_image[1]
        return render(request, 'index.html', {'image': random_image, 'rws_selected': rws_selected, 'name': image_name, 'upright': image_upright, 'reversed': image_reversed, 'cardname_selected': cardname_selected})

    # 如果是 GET 请求，直接渲染模板

    return render(request, 'index.html')

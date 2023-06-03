# -*- coding:utf-8 -*-
# @Project:      mmpose
# @Create Time : 2023/3/22 15:13
# @Author :      ai-weights_cfg
# @File name:    mzq_demo.py
# @Software:     PyCharm

import time

from mmpose.apis import inference_topdown, init_model
from mmpose.utils import register_all_modules

register_all_modules()

config_file = '../weights_cfg/td-hm_hrnet-w48_8xb32-210e_coco-256x192.py'
checkpoint_file = '../weights_cfg/hrnet_w48_coco_256x192-b9e0b3ab_20200708.pth'
model = init_model(config_file, checkpoint_file, device='cuda:0')

t = time.time()
result = inference_topdown(model, 'demo.jpg')
print('推理时间：', time.time() - t)
print('res: ', type(result[0]))

## MagicPose

v1.0.1

简介
- 基于openmmlab_mmpose库，构建人体关键点检测模型！！！
- 实战项目：基于RTMPose的耳朵穴位关键点检测！！！

安装：
~~~
mim install -e .
~~~

RTMDet检测模型快速命令：
~~~
# 训练
cd MagicMMdetection && python tools/train.py weights_cfg/ear_cfg/rtmdet_tiny_ear.py
# 评估
python tools/test.py weights_cfg/ear_cfg/rtmdet_tiny_ear.py \
                      work_dirs/rtmdet_tiny_triangle/epoch_200.pth
# 推理
python demo/image_demo.py \
        data/test_img1.jpeg \
        weights_cfg/ear_cfg/rtmdet_tiny_ear.py \
        --weights checkpoint/epoch_170.pth \
        --out-dir outputs/E2_rtmdet \
        --device cuda:0 \
        --pred-score-thr 0.3
        
# 视频预测
python demo/video_demo.py \
        data/test_video1.mp4 \
        weights_cfg/ear_cfg/rtmdet_tiny_ear.py \
        checkpoint/epoch_170.pth \
        --device cuda:0 \
        --score-thr 0.6 \
        --out outputs/E2_out_video_rtmdet.mp4
~~~

姿态估计模型快速命令：
~~~
# 训练
python tools/train.py weights_cfg/ear_cfg/rtmpose-s-ear.py
# 评估
python tools/test.py weights_cfg/ear_cfg/rtmpose-s-ear.py \
                      work_dirs/epoch_200.pth
# 推理
python demo/topdown_demo_with_mmdet.py \
        weights_cfg/ear_cfg/rtmdet_tiny_ear.py \
        checkpoint/epoch_170.pth \
        weights_cfg/ear_cfg/rtmpose-s-ear.py \
        checkpoint/epoch_99.pth \
        --input data/test_img1.jpeg \
        --output-root outputs/G2_RTMDet-RTMPose \
        --device cuda:0 \
        --bbox-thr 0.5 \
        --kpt-thr 0.5 \
        --nms-thr 0.3 \
        --radius 36 \
        --thickness 30 \
        --draw-bbox \
        --draw-heatmap \
        --show-kpt-idx
~~~
'''
生成GT图片应用于分类
同一类在一个文件夹中

'''
import os
import cv2
import numpy as np
from config import CLASSES
from tool_function import combined_roidb

# CLASSES_dict=dict(list(zip(CLASSES, list(range(len(CLASSES))))))
def main():
    dataset_path = 'E:/fjj/SeaShips_SMD/'
    split_name = 'all'
    save_root_path='Classification'
    if not os.path.exists(save_root_path):
        os.mkdir(save_root_path)
    for i in range(len(CLASSES)):
        new_path=os.path.join(save_root_path,CLASSES[i])
        if not os.path.exists(new_path):
            os.mkdir(new_path)
    imdb, roidb = combined_roidb("shipdataset", split_name,dataset_path)
    count=0
    # for data in roidb:
    while count<len(roidb):
        data=roidb[count]
        boxes=data['boxes']
        img_path=data['image']
        basename=os.path.splitext(os.path.basename(img_path))[0]

        classes=data['gt_classes']
        img=cv2.imread(img_path)
        H,W,C=img.shape
        for i in range(len(classes)):
            xmin = max(boxes[i, 0],0)
            ymin = max(boxes[i, 1],0)
            xmax = min(boxes[i, 2]+1,W)
            ymax = min(boxes[i, 3]+1,H)
            roi=img[ymin:ymax,xmin:xmax]
            save_name=os.path.join(save_root_path,CLASSES[classes[i]],'%s_%d.jpg'%(basename,i))
            try:
                cv2.imwrite(save_name,roi)
            #except:
                print(count,'/',len(roidb))
            except:
                print(count,basename,'#################################################################')
                continue
        count += 1
        #cv2.imwrite(os.path.join(save_root_path,basename),img)


if __name__ == '__main__':
    main()
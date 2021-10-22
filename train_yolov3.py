import yaml
import torch

from YOLOv3.dataloader import build_train_loader
from YOLOv3.loss import make_label


if __name__ == '__main__':
    with open(file="experiments/yolov3.yaml") as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)

    train_loader = build_train_loader(cfg)
    for i, (img, tar) in enumerate(train_loader):
        print("i = ", i)
        print("img size: {}, tar size: {}".format(img.size(), tar.size()))
        labels = make_label(cfg, tar)
        for _ in labels:
            print(_.size())
            print(_.type())
        break
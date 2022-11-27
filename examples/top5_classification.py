from PIL import Image
import torch
from torchvision.models import resnet50
from torchvision.transforms import transforms as T
import pandas as pd
from piedemo.checkpoint import PretrainedCheckpoint
from piedemo.fields.outputs.piegraph import PieGraph


ckpt = PretrainedCheckpoint(
    url="https://raw.githubusercontent.com/xmartlabs/caffeflow/master/examples/imagenet/imagenet-classes.txt",
    filename="imagenet_classes.txt")
with open(str(ckpt.download()), "r") as f:
    categories = [s.strip() for s in f.readlines()]
model = resnet50(pretrained=True)
model.eval()
preprocess = T.Compose([
    T.Resize([256, 256]),
    T.CenterCrop(224),
    T.PILToTensor(),
    T.ConvertImageDtype(torch.float),
    T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


def classify(img: Image.Image):
    print(img)
    if img.size == (0, 0):
        return {
            "output": pd.DataFrame({}),
            "pie": PieGraph()
        }
    batch = preprocess(img).unsqueeze(0)
    prediction = model(batch).squeeze(0).softmax(0)
    class_ids = prediction.argsort()[-5:].tolist()[::-1]
    scores = [prediction[class_id].item() for class_id in class_ids]
    names = [categories[class_id] for class_id in class_ids]

    return {
        "output": pd.DataFrame({
            'categories': names,
            'scores': scores
        }),
        "pie": PieGraph([{"label": n, "prob": s} for n, s in zip(names, scores)])
    }

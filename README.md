# piedemo


```
git clone https://github.com/NVlabs/stylegan3  
cd stylegan3  
piedemo web gen_images:generate_images  
```

<img width="1139" alt="image" src="https://user-images.githubusercontent.com/26091470/204933937-554f9d11-f1c6-493e-af38-48a3c9d7f5c6.png">
<img width="1144" alt="image" src="https://user-images.githubusercontent.com/26091470/204934093-244ff3d0-c672-41bd-ae10-eebfa42d7657.png">
<img width="914" alt="image" src="https://user-images.githubusercontent.com/26091470/204934587-6607d5fe-965b-41b2-922c-c021d5d23ff2.png">




```
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

```


```
piedemo web infer_resnet_imagenet:classify
```

<img width="1137" alt="image" src="https://user-images.githubusercontent.com/26091470/204930993-7287828a-4a89-4c10-bbeb-f4c9d5928281.png">

<img width="1143" alt="image" src="https://user-images.githubusercontent.com/26091470/204931060-37071465-c7ef-4d51-8756-df04bf6e2cfa.png">

<img width="1122" alt="image" src="https://user-images.githubusercontent.com/26091470/204931763-d8c66084-c057-45fe-bba2-357839667e8b.png">



Set up rclone tool for better experience:  

```commandline
curl https://rclone.org/install.sh | sudo bash
rclone config
```

After that use Google Drive hosting and verify your account.
If you use remote connection, verify your account via port forwarding.   
```ssh -L localhost:53682:localhost:53682 ...```

You can simply host your file in Google Drive and use it everywhere you want:
```commandline
python -m piedemo host 1.txt
Host model option
Transferred:              0 B / 0 B, -, 0 B/s, ETA -
Checks:                 1 / 1, 100%
Elapsed time:         1.7s
Url: 
https://drive.google.com/open?id=1nN64iU6EY490YMjI3GHfNQhbN4tVmhtu
Filename: 
1.txt
Code:
PretrainedCheckpoint(gdrive='1nN64iU6EY490YMjI3GHfNQhbN4tVmhtu',
                     filename='1.txt')
```


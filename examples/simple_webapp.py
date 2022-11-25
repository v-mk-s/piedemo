from PIL import Image
from piedemo.fields.outputs.image import OutputImageField
from piedemo.webdemo import WebDemo
from piedemo.fields.inputs.image import InputImageField
from piedemo.fields.grid import VStack, HStack


def demo_function(my_input: Image.Image,
                  my_input2: Image.Image):
    return {
        "image": my_input
    }


if __name__ == '__main__':
    web = WebDemo("PieDataWebDemo",
                  demo_function=demo_function,
                  inputs=VStack([
                      InputImageField("my_input"),
                      InputImageField("my_input2")
                  ]),
                  outputs=OutputImageField("image"))
    web.run()

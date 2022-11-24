from piedemo.fields.outputs.image import OutputImageField
from piedemo.webdemo import WebDemo
from piedemo.fields.inputs.image import InputImageField
from piedemo.fields.grid import VStack, HStack


def demo_function(my_input, my_input2):
    return {
        "image": my_input
    }


web = WebDemo("PieDataWebDemo",
              demo_function=demo_function,
              inputs=VStack([
                  InputImageField("my_input"),
                  InputImageField("my_input2")
              ]),
              outputs=OutputImageField("image"))
web.run()

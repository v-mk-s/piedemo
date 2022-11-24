import os
from flask import Flask, send_from_directory, render_template, render_template_string, request, redirect, url_for, jsonify
import pickle
from .cache import Cache


class WebDemo(object):
    def __init__(self,
                 name="PieDataWebDemo",
                 demo_function=lambda x: x,
                 inputs=None,
                 outputs=None,
                 aggregation_rule=None,
                 cache_path='./.cache'):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

        self.demo_function = demo_function
        self.aggregation_rule = aggregation_rule

        self.input_fields = {f.name: f for f in self.inputs.children()}

        self.cache = Cache(cache_path)

    def run(self,
            host='0.0.0.0',
            port='8008',
            debug=True,
            **options):
        app = Flask(self.name, static_folder='/Users/georgijkasparanc/piedemo_frontend/build')

        @app.route('/', defaults={'path': ''})
        @app.route('/<path:path>')
        def serve(path):
            if path != "" and os.path.exists(app.static_folder + '/' + path):
                return send_from_directory(app.static_folder, path)
            else:
                return send_from_directory(app.static_folder, 'index.html')

        @app.route('/api/inputs', methods=['POST'])
        def send_inputs():
            return jsonify(self.inputs.generate())

        @app.route('/api/outputs/<int:output_id>', methods=['POST'])
        def send_outputs(output_id: int):
            output_data = self.cache.get(output_id)['outputs']
            print(output_data)
            return jsonify(output_data)

        @app.route('/api/process', methods=['POST'])
        def process():
            data = request.files.to_dict()
            data.update(request.form.to_dict())
            data.update(request.args.to_dict())
            data = self.aggregate(data)

            for key in data.keys():
                data[key] = self.input_fields[key].parse(data[key])

            output_data = self.demo_function(**data)
            output_id = self.cache.store(data, output_data)

            return redirect(url_for("serve", path=f"outputs/{output_id}"),
                            code=200)

        app.run(host=host, port=port, debug=debug, **options)

    def aggregate(self, data):
        if self.aggregation_rule is None:
            return data

        if self.aggregation_rule == 'by_underscore':
            new_data = {}
            for key in data.keys():
                d = new_data
                ks = key.split('_')
                for k in ks[:-1]:
                    d = d.setdefault(k, {})
                d[ks[-1]] = data[key]
            return new_data

        raise NotImplementedError()

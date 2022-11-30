import os
from pathlib import Path
import shutil
from .checkpoint import url_download_file
from flask import Flask, send_from_directory, render_template, render_template_string, request, redirect, url_for, jsonify
import zipfile
import pickle
import copy
from .cache import Cache, make_storage


class WebDemo(object):
    PIEBREAK = '__piedemo__'

    def __init__(self,
                 name="PieDataWebDemo",
                 demo_function=lambda x: x,
                 inputs=None,
                 outputs=None,
                 aggregation_rule='by_underscore',
                 cache_path='./.cache'):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

        self.demo_function = demo_function
        self.aggregation_rule = aggregation_rule

        self.input_fields = {f.name: f for f in self.inputs.children()}

        self.cache = Cache(Path(cache_path))
        self.static_path = os.path.join(os.path.dirname(__file__), 'build')
        self.download_static_files()

    def download_static_files(self):
        if not os.path.exists(self.static_path):
            cached_path = os.path.join(os.path.dirname(__file__))
            zip_path = os.path.join(cached_path, 'static.zip')
            url_download_file(url="https://github.com/PieDataLabs/piedemo_frontend/releases/download/V0.0.5/static.zip",
                              cached_path=zip_path)
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(cached_path)
            os.remove(zip_path)

    def run(self,
            host='0.0.0.0',
            port='8008',
            debug=True,
            **options):
        print(self.static_path)
        app = Flask(self.name, static_folder=self.static_path)

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
            outputs = copy.deepcopy(self.outputs)
            output_fields = {f.name: f for f in outputs.children()}
            output_data = self.cache.get(output_id)['outputs']
            for key in output_data.keys():
                output_fields[key].set_output(output_data[key])
            response = jsonify(outputs.generate())
            outputs.clear()
            return response

        @app.route('/api/process', methods=['POST'])
        def process():
            data = request.files.to_dict()
            data.update(request.form.to_dict())
            data.update(request.args.to_dict())
            print(data)
            data = self.aggregate(data)
            print(data)

            for key in list(data.keys()):
                if key not in self.input_fields:
                    del data[key]
                    continue
                data[key] = self.input_fields[key].parse(data[key])

            print(data)

            output_data = self.demo_function(**data)
            print(output_data)
            output_id = self.cache.store(data, output_data)

            return redirect(url_for("serve", path=f"outputs/{output_id}"))

        app.run(host=host, port=port, debug=debug, **options)

    def aggregate(self, data):
        if self.aggregation_rule is None:
            return data

        if self.aggregation_rule == 'by_underscore':
            new_data = {}
            for key in data.keys():
                if self.PIEBREAK not in key:
                    new_data[key] = make_storage(data[key])

            for key in data.keys():
                if self.PIEBREAK not in key:
                    continue
                ks = key.split(self.PIEBREAK)
                setattr(new_data[ks[0]], self.PIEBREAK.join(ks[1:]), data[key])
            return new_data

        raise NotImplementedError()

    def __del__(self):
        shutil.rmtree(self.static_path)

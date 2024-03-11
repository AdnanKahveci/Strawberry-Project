from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')

os.makedirs(uploads_dir, exist_ok=True)


@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


#
# fig, ax = plt.subplots(2,4, figsize=(20,10))
# imgs = os.listdir('./images/train')
# for idx in itertools.product(range(2),range(4)):
#     imgname = np.random.choice(imgs)
#     img = cv2.imread(f'./images/train/{imgname}')
#     results = model(img)
#     ax[idx[0],idx[1]].imshow(cv2.cvtColor(np.squeeze(results.render()), cv2.COLOR_BGR2RGB))

# print(img)
#
# img = os.path.join('yolov5','cilek.jpg')
# results=model(img)
# print(results)
# plt.imshow(results.render())
# plt.show()

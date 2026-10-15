import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/sort', methods=['POST'])
def bubble_sort():
  data = request.get_json()
  arr = data.get('array', [])

  steps = []
  # 초기 상태 저장
  steps.append(list(arr))

  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True
        steps.append(list(arr))
    if not swapped:
      break

  return jsonify({'steps': steps, 'sorted': arr})


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)

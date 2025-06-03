Penjelasan File

Setelah mengunduh contoh proyek, Anda akan menjumpai beberapa file dan folder sebagai berikut:

    `notebook.ipynb` merupakan berkas notebook yang dapat dijalankan melalui Google Colaboratory. Notebook ini berisi tahapan dalam membuat, mengevaluasi, dan mengonversi model.
    `yelp_labelled.txt` merupakan dataset untuk melatih model.
    `model.h5` merupakan sebuah HDF5 model yang akan dikonversi menjadi `model.json`.
    `tfjs_model` merupakan sebuah folder yang berisi `model.json` dan bobot dalam berbentuk binary file. Kedua file tersebut digunakan untuk menerapkan model NLP ke dalam web browser.
    `word_index.json` merupakan sebuah metadata dalam bentuk file json yang berisi pasangan kata dan indeks. Dengan memanfaatkan berkas ini, kita dapat mengubah inputan reviu menjadi sebuah token.
     `index.html` merupakan berkas html sebagai tampilan utama web.
    `script.js` merupakan berkas JavaScript yang berisi perintah untuk men-deploy model yang telah dibuat ke dalam web.
    `images` berisi beberapa gambar seperti plot evaluasi model yang telah dibuat dan tampilan awal web.
    `styles` berisi `style.css` dan beberapa gambar untuk memperindah tampilan web.


Setelah melatih dan menyimpan TensorFlow model, kemudian ubahlah model tersebut menjadi tflite model. Untuk mengubah model menjadi tflite model kita dapat menggunakan TFLite Converter, berikut cara penggunaan TFLite Converter untuk mengonversi model menjadi tflite model:

    Konversi model yang disimpan dalam format SavedModel

    converter = tf.lite.TFLiteConverter.from_saved_model(“SavedModel_path”)
    tflite_model = converter.convert()
     
    with tf.io.gfile.GFile('model_name.tflite', 'wb') as f:
        f.write(tflite_model)

Konversi model yang disimpan dalam format keras model

        converter = tf.lite.TFLiteConverter.from_keras_model(“keras_model_path”)
        tflite_model = converter.convert()
         
         
        with tf.io.gfile.GFile('model_name.tflite', 'wb') as f:
            f.write(tflite_model)

Kemudian tflite model tersebut akan dieksekusi menggunakan TensorFlow Lite interpreter. TF-Lite juga dilengkapi dengan API untuk berbagai bahasa pemrograman, seperti Swift, C, C++, Java, dan Python.

Selanjutnya, kita akan menjalankan model machine learning pada aplikasi android dengan menggunakan TF-Lite. Apakah Anda sudah tidak sabar untuk masuk ke materi latihan? Yuk, lanjut ke materi berikutnya.
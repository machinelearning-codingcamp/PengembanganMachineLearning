# Image classification submission

Halo! Salam kenal, namaku nadia, pada project ini aku akan membuat image classification dengan 6 kelas dengan objek pemandangan/alam/bangunan. 
Sebelumnya mohon maaf apabila terdapat banyak code yang harus saya interrupt, karena proses pengerjaan submisi ini membutuhkan waktu sekitar 4 hari, yang dimana tidak memungkinkan untuk membiarkan laptop saya terus menyala. Untuk menangani hal tersebut, aku memanfaat check point callback untuk memastikan progress saya tersimpan.

Saya banyak belajar dalam project ini, terutama dalam experiment. Karena itu pada notebook ada plot yang hilang historynya karena saya belum tahu variabel apa yang harus digunakan, atau bagaimana cara mengatasi kernel yang restart ketika laptop mati. Saya juga melakukan kesalahan di awal karena menghapus beberapa kali dataset yang ada dan memulihkan dengan dataset awal karena ketika melanjutkan pekerjaan, saya malah run all cell.

Saya sangat mengharapkan review mendetail perihal saran yang dapat dikembangkan, maupun tips dalam pengerjaan. Sebagai informasi tambahan, saya masih mengalami kesulitan pada:
- melakukan fine tuning pada model CNN
- load model (terutama tfjs dan tflite) karena pada materi yang tersedia belum update dependency dan saya belum bisa menyelesaikannya

Karena saya menyimpan cukup banyak data, saya hanya melampirkan yang disarankan pada ketentuan submisi. Adapun tree asli project saya adalah:

(.venv) nadia@nadia-HP-14-Laptop-PC:~/Documents/non-kuliah/CODINGCAMP/MachineLearningPlayGround/PengembanganMachineLearning/finalProject$ tree -L 3
.
├── data
│   ├── seg_augmented
│   │   ├── buildings
│   │   ├── forest
│   │   ├── glacier
│   │   ├── mountain
│   │   ├── sea
│   │   └── street
│   ├── seg_combined
│   │   ├── buildings
│   │   ├── forest
│   │   ├── glacier
│   │   ├── mountain
│   │   ├── sea
│   │   └── street
│   ├── seg_pred
│   │   └── seg_pred
│   ├── seg_test
│   │   └── seg_test
│   ├── seg_train
│   │   └── seg_train
│   └── seg_train_2
│       └── seg_train
├── final_model_1.h5
├── final_model_2.h5
├── inference.ipynb
├── model_checkpoint_epoch7.h5
├── model_checkpoints
│   ├── model_epoch_08.h5
│   ├── model_epoch_09.h5
│   ├── model_epoch_10.h5
│   ├── model_epoch_11.h5
│   ├── model_epoch_12.h5
│   ├── model_epoch_13.h5
│   ├── model_epoch_14.h5
│   ├── model_epoch_15.h5
│   ├── model_epoch_16.h5
│   ├── model_epoch_17.h5
│   ├── model_epoch_18.h5
│   ├── model_epoch_19.h5
│   ├── model_epoch_20.h5
│   ├── model_epoch_21.h5
│   ├── model_epoch_22.h5
│   ├── model_epoch_23.h5
│   ├── model_epoch_24.h5
│   ├── model_epoch_25.h5
│   ├── model_epoch_26.h5
│   ├── model_epoch_27.h5
│   ├── model_epoch_28.h5
│   ├── model_epoch_29.h5
│   └── model_epoch_30.h5
├── model_checkpoints_2
│   ├── model_epoch_13.h5
│   ├── model_epoch_14.h5
│   ├── model_epoch_15.h5
│   ├── model_epoch_16.h5
│   ├── model_epoch_17.h5
│   ├── model_epoch_18.h5
│   ├── model_epoch_19.h5
│   ├── model_epoch_20.h5
│   ├── model_epoch_21.h5
│   ├── model_improved_epoch_01.h5
│   ├── model_improved_epoch_02.h5
│   ├── model_improved_epoch_03.h5
│   ├── model_improved_epoch_04.h5
│   ├── model_improved_epoch_05.h5
│   ├── model_improved_epoch_06.h5
│   ├── model_improved_epoch_07.h5
│   ├── model_improved_epoch_08.h5
│   ├── model_improved_epoch_09.h5
│   ├── model_improved_epoch_10.h5
│   ├── model_improved_epoch_11.h5
│   ├── model_improved_epoch_22.h5
│   ├── model_improved_epoch_23.h5
│   ├── model_improved_epoch_24.h5
│   ├── model_improved_epoch_25.h5
│   ├── model_improved_epoch_26.h5
│   ├── model_improved_epoch_27.h5
│   ├── model_improved_epoch_28.h5
│   ├── model_improved_epoch_29.h5
│   └── model_improved_epoch_30.h5
├── model_checkpoints_3
│   ├── model_MobileNetV2_epoch_01.h5
│   ├── model_MobileNetV2_epoch_02.h5
│   ├── model_MobileNetV2_epoch_03.h5
│   ├── model_MobileNetV2_epoch_04.h5
│   ├── model_MobileNetV2_epoch_05.h5
│   ├── model_MobileNetV2_epoch_06.h5
│   ├── model_MobileNetV2_epoch_07.h5
│   ├── model_MobileNetV2_epoch_08.h5
│   ├── model_MobileNetV2_epoch_09.h5
│   ├── model_MobileNetV2_epoch_10.h5
│   ├── model_MobileNetV2_epoch_11.h5
│   ├── model_MobileNetV2_epoch_12.h5
│   ├── model_MobileNetV2_epoch_13.h5
│   ├── model_MobileNetV2_epoch_14.h5
│   ├── model_MobileNetV2_epoch_15.h5
│   ├── model_MobileNetV2_epoch_16.h5
│   ├── model_MobileNetV2_epoch_17.h5
│   ├── model_MobileNetV2_epoch_18.h5
│   ├── model_MobileNetV2_epoch_19.h5
│   └── model_MobileNetV2_epoch_20.h5
├── model_checkpoints_fine_tune_2
│   ├── model_MobileNetV2_fine_tune_2_epoch_01.h5
│   ├── model_MobileNetV2_fine_tune_2_epoch_03.h5
│   ├── model_MobileNetV2_fine_tune_2_epoch_04.h5
│   ├── model_MobileNetV2_fine_tune_2_epoch_06.h5
│   ├── model_MobileNetV2_fine_tune_2_epoch_07.h5
│   ├── model_MobileNetV2_fine_tune_2_epoch_08.h5
│   ├── model_MobileNetV2_fine_tune_2_epoch_09.h5
│   ├── model_MobileNetV2_fine_tune_2_epoch_17.h5
│   └── model_MobileNetV2_fine_tune_2_epoch_18.h5
├── notebook.ipynb
├── README.md
├── requirements.txt
├── saved_model
│   ├── assets
│   ├── fingerprint.pb
│   ├── saved_model.pb
│   └── variables
│       ├── variables.data-00000-of-00001
│       └── variables.index
├── tfjs_model
│   ├── group1-shard1of3.bin
│   ├── group1-shard2of3.bin
│   ├── group1-shard3of3.bin
│   └── model.json
└── tflite
    ├── label.txt
    └── model.tflite

33 directories, 98 files


Mungkin itu saja yang dapat saya sampaikan, saya berterima kasih atas kesediaannya.

God bless!
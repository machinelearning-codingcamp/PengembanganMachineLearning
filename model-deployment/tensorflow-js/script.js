// ----Kolom deklarasi variabel-----
let input = document.querySelector('input');
let button = document.querySelector('button');
button.addEventListener('click', onClick);

let isModelLoaded = false;
let model;
let word2index;

// Parameter data preprocessing
const maxlen = 20;
const vocab_size = 2000;
const padding = 'post';
const truncating = 'post';

var myVar;
// -----------------------------------

function myFunction() {
    myVar = setTimeout(showPage, 3000);
}

function showPage() {
    document.getElementById("loaderlabel").style.display = "none";
    document.getElementById("loader").style.display = "none";       
    document.getElementById("mainAPP").style.display = "block";
}

function detectWebGLContext () {
    // Create canvas element. The canvas is not added to the
    // document itself, so it is never displayed in the
    // browser window.
    var canvas = document.createElement("canvas");
    // Get WebGLRenderingContext from canvas element.
    var gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
    // Report the result.
    if (gl && gl instanceof WebGLRenderingContext) {
        console.log("Congratulations! Your browser supports WebGL.");
        init();
    } else {
        alert("Failed to get WebGL context. Your browser or device may not support WebGL.");
    }
}

detectWebGLContext();

// ----Kolom fungsi `getInput()`-----
// Fungsi untuk mengambil input review
function getInput(){
    const reviewText = document.getElementById('input')
    return reviewText.value;
}
// -----------------------------------

// ----Kolom fungsi `padSequence()`-----
// Fungsi untuk melakukan padding
function padSequence(sequences, maxLen, padding='post', truncating = "post", pad_value = 0){
    return sequences.map(seq => {
        if (seq.length > maxLen) { //truncat
            if (truncating === 'pre'){
                seq.splice(0, seq.length - maxLen);
            } else {
                seq.splice(maxLen, seq.length - maxLen);
            }
        }
                
        if (seq.length < maxLen) {
            const pad = [];
            for (let i = 0; i < maxLen - seq.length; i++){
                pad.push(pad_value);
            }
            if (padding === 'pre') {
                seq = pad.concat(seq);
            } else {
                seq = seq.concat(pad);
            }
        }               
        return seq;
        });
}
// -----------------------------------


// ----Kolom fungsi `predict()`-----
// Fungsi untuk melakukan prediksi
function predict(inputText){

    // Mengubah input review ke dalam bentuk token
    const sequence = inputText.map(word => {
        let indexed = word2index[word];

        if (indexed === undefined){
            return 1; //change to oov value
        }
        return indexed;
    });
    
    // Melakukan padding
    const paddedSequence = padSequence([sequence], maxlen);

    const score = tf.tidy(() => {
        const input = tf.tensor2d(paddedSequence, [1, maxlen]);
        const result = model.predict(input);
        return result.dataSync()[0];
    });

    return score;  

}
// -----------------------------------


// ----Kolom fungsi `onClick()`-----
// Fungsi yang dijalankan ketika tombol "Post Review" diclick
function onClick(){
    
    if(!isModelLoaded) {
        alert('Model not loaded yet');
        return;
    }

    if (getInput() === '') {
        alert("Review Can't be Null");
        document.getElementById('input').focus();
        return;
    }
    
    // 
    const inputText = getInput().trim().toLowerCase().split(" ");

    // Score prediksi dengan nilai 0 s/d 1 
    let score = predict(inputText); 

    // Kondisi penentuan hasil prediksi berdasarkan nilai score
    if (score > 0.5) {
        alert ('Positive Review \n'+score);
    } else {
        alert ('Negative Review \n'+score);
    }
}
// -----------------------------------


// // ----Kolom fungsi `init()`-----
// async function init(){

//     // Memanggil model tfjs
//     // model = await tf.loadLayersModel('http://127.0.0.1:5500/tfjs_model/model.json'); // Untuk VS Code Live Server
//     model = await tf.loadLayersModel('http://127.0.0.1:5500/PengembanganMachineLearning/model-deployment/tfjs_model/model.json'); // Untuk VS Code Live Server
//     // model = await tf.loadLayersModel('http://127.0.0.1:8887/tfjs_model/model.json');
//     isModelLoaded = true;

//     //Memanggil word_index
//     const word_indexjson = await fetch('http://127.0.0.1:5500/PengembanganMachineLearning/model-deployment/word_index.json'); // Untuk VS Code Live Server
//     // const word_indexjson = await fetch('http://127.0.0.1:8887/word_index.json'); 
//     word2index = await word_indexjson.json();

//     console.log(model.summary()); 
//     console.log('Model & Metadata Loaded Succesfully');
// }
// // -----------------------------------

// Add this after model loading in init()
async function init() {
    try {
        console.log("Init function started");
        
        // Model path
        const modelPath = 'http://127.0.0.1:5500/PengembanganMachineLearning/model-deployment/tfjs_model/model.json';
        console.log("Attempting to load model from:", modelPath);
        
        // Try accessing the model file to verify it exists
        const modelCheck = await fetch(modelPath);
        if (!modelCheck.ok) {
            throw new Error(`Model file not accessible: ${modelCheck.status} ${modelCheck.statusText}`);
        }
        console.log("Model file exists and is accessible");
        
        // Try loading the model
        model = await tf.loadLayersModel(modelPath);
        console.log("Model loaded successfully");
        
        // Word index path
        const word_indexPath = 'http://127.0.0.1:5500/PengembanganMachineLearning/model-deployment/word_index.json';
        console.log("Attempting to load word index from:", word_indexPath);
        
        // Try accessing the word index file to verify it exists
        const word_indexCheck = await fetch(word_indexPath);
        if (!word_indexCheck.ok) {
            throw new Error(`Word index file not accessible: ${word_indexCheck.status} ${word_indexCheck.statusText}`);
        }
        console.log("Word index file exists and is accessible");
        
        // Load word index
        const word_indexjson = await fetch(word_indexPath);
        word2index = await word_indexjson.json();
        console.log("Word index loaded successfully");
        
        // Set model loaded flag
        isModelLoaded = true;
        console.log("Model and word index loaded successfully");
        
        // Optional: Print model summary
        try {
            console.log(model.summary());
        } catch (summaryError) {
            console.warn("Could not print model summary:", summaryError);
        }
        
        // Show the main app
        document.getElementById("loaderlabel").style.display = "none";
        document.getElementById("loader").style.display = "none";
        document.getElementById("mainAPP").style.display = "block";
        
    } catch (error) {
        console.error("Detailed error in init():", error);
        
        // Try to get more information about the model file
        try {
            const modelPath = 'http://127.0.0.1:5500/PengembanganMachineLearning/model-deployment/tfjs_model/model.json';
            const response = await fetch(modelPath);
            console.log("Model file status:", response.status, response.statusText);
            if (response.ok) {
                const modelJson = await response.json();
                console.log("Model JSON structure:", modelJson);
            }
        } catch (fetchError) {
            console.error("Additional error checking model file:", fetchError);
        }
        
        alert("Failed to load the model. Please check the console for details.");
    }
}
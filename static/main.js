function getDataUrl(img) {
    // Create canvas
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    // Set width and height
    canvas.width = img.width;
    canvas.height = img.height;
    // Draw the image
    ctx.drawImage(img, 0, 0);
    return canvas.toDataURL('https://testbucketirina.s3.eu-west-2.amazonaws.com/ml-image/img_cat_real.jpeg');
 }

var selectedFile = document.getElementById("file-upload");
selectedFile.addEventListener("change", selectedFileHandler, false);
var imagePreview = document.getElementById("image-preview");
var imageDisplay = document.getElementById("image-display");
var uploadCaption = document.getElementById("upload-caption");
var predResult = document.getElementById("pred-result");
var loader = document.getElementById("loader");

function selectedFileHandler(e) {
  var files = e.target.files;
  console.log(files);
  e.preventDefault();
  file = files[0];
  console.log(file.name);
  var fileName = encodeURI(file.name);
  console.log(fileName);
  var FR = new FileReader();
  FR.readAsDataURL(file);

  FR.onloadend = () => {
    imagePreview.src = URL.createObjectURL(file);
    console.log(imagePreview.src);

    show(imagePreview);
    hide(uploadCaption);

    predResult.innerHTML = "";
    imageDisplay.classList.remove("loading");

    let display = document.getElementById("image-display");
    display.src = FR.result;
    show(display);
    console.log(display.src);
  };

  console.log(FR);
  imagePreview.src = URL.createObjectURL(file);
  imagePreview.classList.remove("hidden");
  console.log(imagePreview.src);
  console.log(typeof(imagePreview.src));
  console.log((imagePreview.src).length);
}


function hide(el) {
  el.classList.add("hidden");
}

function show(el) {
  el.classList.remove("hidden");
}
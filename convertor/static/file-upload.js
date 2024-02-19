// document.getElementById('file-input').addEventListener("change", function () {
//     document.getElementById('filecount')
// });

function handleFileSelect(event) {
    //Check File API support
    if (window.File && window.FileList && window.FileReader) {
    console.log("gfgfg")

        var files = event.target.files; //FileList object
        var output = document.getElementById("result");
        var filecount = document.getElementById('filecount');
        var filename = document.getElementById('filename')

        if (typeof (filecount) != 'undefined' && filecount != null) {
            document.getElementById('filecount').innerHTML = files.length + " files selected";
        }

        if (typeof (filename) != 'undefined' && filename != null) {
            document.getElementById('filename').innerHTML = files[0].name;
        }


        // for (var i = 0; i < files.length; i++) {
        //     output.classList.remove('quote-imgs-thumbs--hidden')
        //     var file = files[i];
        //
        //     var picReader = new FileReader();
        //     picReader.addEventListener("load", function (event) {
        //         var picFile = event.target;
        //         var div = document.createElement("div");
        //         div.innerHTML = "<img class='img-preview-thumb' src='" + picFile.result + "'" + "title='" + file.name + "'/>";
        //         output.insertBefore(div, null);
        //     });
        //     //Read the image
        //     picReader.readAsDataURL(file);
        // }

        if (!!files) {
            if (typeof (output) != 'undefined' && output != null) {
                output.classList.remove('quote-imgs-thumbs--hidden');
            }
            document.getElementById('uploadbutton').disabled = false;
            document.getElementById('removequeue').classList.remove('disabled')
        }

        if (typeof (output) != 'undefined' && output != null) {
            for (var i = 0; i < files.length; i++) {
                var img = document.createElement('img');
                img.src = URL.createObjectURL(event.target.files[i]);
                img.classList.add('img-preview-thumb');
                img.classList.add('remove');
                output.appendChild(img)
            }
        }

    } else {
        console.log("Your browser does not support File API");
    }
}
function handlePdfFileSelect(event) {

    if (window.File && window.FileList && window.FileReader) {
    console.log("hghg");
    console.log(event.target.files);
    var output = document.getElementById("result");
var object = document.getElementById('object');
var anchor = document.getElementById('file-tag');
const blob = new Blob([event.target.files[0]], {type: event.target.files[0]?.type});
anchor.href = URL.createObjectURL(blob);
object.data = URL.createObjectURL(blob);
                output.classList.remove('quote-imgs-thumbs--hidden');

}
else {
        console.log("Your browser does not support File API");
    }

}
if(document.getElementById('files') != null){
console.log(document.getElementById('files'));
document.getElementById('files').addEventListener('change', handleFileSelect, false);

}
if(document.getElementById('files_docx') != null){
console.log("in files docx");
document.getElementById('files_docx').addEventListener('change', handlePdfFileSelect, false);

}

// Define some variables for the function.
const height = document.getElementById('inputHeight');
const width = document.getElementById('inputWidth');
const canvas = document.getElementById('pixelCanvas');
// core of the makeGrid function
function makeGrid(height, width) {
    // reset grid at start
    canvas.innerHTML = '';
    // build grid: outer loop for rows, nested for cell appendations
    for (var x = 0; x < height.value; x++) {
        let row = canvas.insertRow(x);
        for (var y = 0; y < width.value; y++) {
            let cell = row.insertCell(y);
            // Select color input
            cell.addEventListener('click', function (event) {
                event.target.style.backgroundColor = document.getElementById("colorPicker").value;
            });
        }
    }
}

//build grid by calling makeGrid
const sizePick = document.getElementById('sizePicker');
sizePick.addEventListener('submit', function (event) {
    event.preventDefault();
    makeGrid(height, width);
    });

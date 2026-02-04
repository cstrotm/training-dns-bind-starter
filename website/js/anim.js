var count = 0;

function NextPage(id,max) {
    img = document.getElementById(id);
    count++;
    if (count == max) {
	count = 0;
    }
    cnt = count.toString().padStart(2, "0")
    img.src = 'img/' + id + '-' + cnt + '.png';
}

function PrevPage(id) {
    img = document.getElementById(id);
    count--;
    if (count < 0) {
	count = 0;
    }
    cnt = count.toString().padStart(2, "0")
    img.src = 'img/' + id + '-' + cnt + '.png';
}

function ResetSlides(id) {
    img = document.getElementById(id);
    count=0;
    cnt = count.toString().padStart(2, "0")
    img.src = 'img/' + id + '-' + cnt + '.png';
}

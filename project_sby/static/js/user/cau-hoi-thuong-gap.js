
    var closeLightboxButton = document.getElementById('close-icon');

    closeLightboxButton.onclick = function () {
        document.getElementById('lightbox').style.display = 'none';
    }

    var questions = document.getElementsByClassName('question');

    for (var j = 0; j < questions.length; j++) {
        var question = questions[j];



        question.onclick = function () {
            // var answer = question.nextElementSibling; // Lỗi khi dùng cách này!!!
            var answer = this.nextElementSibling; // Dùng 'this' => OK (y)(y)(y)
            console.log(answer);

            // ẩn/hiện câu trả lời
            var display = answer.style.display;
            answer.style.display = display == 'block' ? 'none' : 'block';

            // thay đổi nội dung của toogle display icon
            var iconText = this.getElementsByClassName('toggle-display')[0].innerText;
            this.getElementsByClassName('toggle-display')[0].innerText = (iconText == '+') ? '' : '';
        }

    }

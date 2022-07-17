$(document).ready(function(){
    viewportWidth = 420 //クロッピングするサイズ（横幅 ピクセル表記）
    viewportHeight = 560 //クロッピングするサイズ（縦幅 ピクセル表記）
    boundaryWidth = 700 //クロッピング元画像のサイズ（横幅 ピクセル表記）
    boundaryHeight = 700 //クロッピング元画像のサイズ（縦幅 ピクセル表記）

    // croppieの初期設定
    $image_crop = $('#profileImage_croppie').croppie({
        enableExif: true,
        viewport: {
            width: viewportWidth,
            height: viewportHeight,
            type:'circle' //円形にクロッピングしたい際はここをcircleとする
        },
        boundary: {
            width: boundaryWidth,
            height: boundaryHeight
        }
    })
    $('#upload_image').on('change', function(){
        var reader = new FileReader();
        reader.onload = function (event) {
            $image_crop.croppie('bind', {
                url: event.target.result
            }).then(function(){
                // console.log('Bind complete');
            });
        }
        $('#profileImage_croppie').css('display','block');
        reader.readAsDataURL(this.files[0]);
    });
});

$('#profileImage_croppie').ready(function(event){
    $('#profileImage_croppie').css('display','none');
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// 登録ボタン押下
$('#post_image').click(function(event){
    var csrf_token = getCookie("csrftoken");
    var rslt = window.confirm("プロフィール画像を登録してよろしいですか？");
    if (rslt) {
        $image_crop.croppie('result', 'base64').then(function(response){
            $.ajax({
                url:"{% url 'myapp:image_upload' %}",
                type: "POST",
                data:{"image": response},
                dataType: 'json',
                // 送信前にヘッダにcsrf_tokenを付与
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrf_token);
                    }
                },
            });
        })
    }
});
function parseText(data) {
	var ret = "";
	for (var i = 0; i < data.length; i++) {
		if (data[i] == '0' || data[i] == '1')
			ret += data[i];
	}
	return ret;
}
function jsReadFiles(files) {
	if (files.length) {
		var file = files[0];
		var reader = new FileReader();//new一个FileReader实例
		reader.onload = function() {
			data.text = parseText(this.result);
			jsonData = JSON.stringify(data);
			if (1 == data.mode && data.text.length % 64 != 0) {
				spinner.hide();
				error.text("解密密文没有对齐64位，当前有效位数为" + data.text.length);
				error.show();
			} else {
				getJson("POST", "/des", jsonData, renderResult);
			}
		}
		reader.readAsText(file);
	} else {
		spinner.hide();
		error.text("请选择上传的文件");
		error.show();
	}
}

function beautifyJson(jsonString) {
    return JSON.stringify(JSON.parse(jsonString),null,2);
}

function getJson(type, url, data, callback) {
    $.ajax({
        type: type,
        url: url,
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: callback,
        failure: function(errMsg) {
            alert(errMsg);
        }
    });
}

function renderResult(response) {
	var str;
	spinner.hide();
	if (response['status'] == 0) {
		if (data.mode == 1) {
			str = "解密";
		} else {
			str = "加密";
		}
		toastText.text(str + "完成！");
		toast.toast('show');
		result.val(response['result']);
	} else {
		error.text(response['result']);
		error.show();
	}
    // data = beautifyJson(data);
    // var length = data.split(/\r\n|\r|\n/).length;
    // result.attr("rows", length);
}

function getData() {
	spinner.show();
	toast.toast('hide');
	error.hide();
    var mode = parseInt($("input[name=mode]:checked").val());
    var ciphertext = parseText($("#ciphertextInput").val());
    var iv = parseText($("#iv").val());
	data = { 
		mode: mode,
		ciphertext: ciphertext,
		iv: iv
	}
	flag = true;
	if (ciphertext.length != 64) {
		flag = false;
		invalidCipher.text(validStr + ciphertext.length);
		cipherInput.addClass('is-invalid');
	} else {
		cipherInput.removeClass('is-invalid');
	}
	if (iv.length != 64) {
		flag = false;
		invalidIv.text(validStr + iv.length);
		ivInput.addClass('is-invalid');
	} else {
		ivInput.removeClass('is-invalid');
	}
    console.log(flag + "\nData: " + JSON.stringify(data));
	if (flag)
		jsReadFiles(fileObj[0].files);
	else
		spinner.hide();
    // getJson("POST", "/des", data, renderResult);
}

var cipherInput = $("#ciphertextInput");
var ivInput = $("#iv");
var result = $("#result");
var fileObj = $("#file");
var toast = $(".toast");
var toastText = toast.children(".toast-body");
var spinner = $("#spinner");
var error = $("#error");
var invalidCipher = $("#invalid-cipher");
var invalidIv = $("#invalid-iv");
var validStr = "请输入64位二进制内容，目前有效位数为";
var data;
var flag;

$(document).ready(function () {
	  bsCustomFileInput.init()
})

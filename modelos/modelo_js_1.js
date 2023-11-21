function showLoading(a, b) {
    document.querySelector(a).classList.add('loading');
    document.querySelector(b).classList.add('loading-content');
}

function hideLoading(a, b) {
    document.querySelector(a).classList.remove('loading');
    document.querySelector(b).classList.remove('loading-content');
}

function formClear() {
	$('#file').val('');
	$('#id-{singular}').val('');

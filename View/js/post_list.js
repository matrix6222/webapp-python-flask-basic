load_post_list();

function load_post_list() {
	fetch('/api/get_post_list', {
		method: 'POST',
		headers: {
			'Accept': 'application/json',
			'Content-Type': 'application/json'}
	})
	.then((response) => response.json())
	.then((json) => {
		if (json['status'] === 'OK') {
			let data = json['data'];
			let container = document.getElementById('post-list');
			container.innerHTML = '';
			for (let x = 0; x < data.length; x++) {
				let row = data[x];
				let id = row['id'];
				let title = row['title'];
				let el = `<div class="row">
					${id} - ${title}
				</div>`;
				container.innerHTML += el;
			}
		}
	});
}
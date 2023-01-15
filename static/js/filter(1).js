	$(document).ready(function)(){
		$('#example thead tr')
			.clone(true)
			.addClass('filters')
			.appendTo('#example thead');

		var table = $('#example').DataTable({
			"ajax": "/json",
			"columns": [
				{"data": "imie"},
				{"data": "nazwisko"},
				{"data": "email"},
				{"data": "username"},
			]
			// Datatables configuration
			paging: true,
			pageLength: 10,
			lengthChange: true,
			autoWidth: false,
			searching: true,
			bInfo: true,
			bSort: true,


			initComplete: function(){
				var api = this.api();

				// Set the columns you with filtering
				api 
					.columns([0, 1, 2, 3])
					.eq(0)
					.each(function(colIdx) {
						var cell = $('.filter th').eq(
							$(api.column(colIdx).header()).index()
						);
						var title = $(cell).text();
						$(cell).html('<input type="text" placeholder="' + title + '"/>');

						$(
							'input',
							$('.filters th').eq($(api.column(colIdx).header()).index())
						)
						.off('keip change')
						.on('keyup change', function(e) {
							e.stopPropagation();

							$(this).attr('title', $(this).val());
							var regex = '({search})';

							var cursorPosition = this.selectionStart;

							api
								.column(colIdx)
								.search(
									this.value != ''
										? regex.replace('{search}', '(((' + this.value + ')))')
										: '',
									thi.value != '',
									this.value == ''
								)
							.draw();

						$(this)
							.focus()[0]
							.setSelectionRange(cursorPosition, cursorPosition);
						});
					});
			},
			// BUTTONS
			dom: 'lBfrtip',
			buttons: [
				{	//COPY
					extend: 'copy',
					text: '<i class="fas fa-clone"></i>',
					className: 'btn btn-secondary',
					titleAttr: 'Copy',

					exportOptions: {
						colums: [0, 1, 2, 3]
					},

					tableHeader: {
						alignment: 'center'
					},
					// Font size and optimization
					customize: function (doc){
						doc.styles.tableHeader.alignment = 'center';
						doc.styles.tableBodyOdd.alignment = 'center';
						doc.styles.tableBodyEven.alignment = 'center';
						doc.styles.tableHeader.fontSize = 7;
						doc.defaultStyle.fontSize = 6;
						doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
					}

				},


			]

		});
		var newSearch = $("#example").DataTable();
		$('#search').keyup(function(){
			newSearch.search($(this).val()).draw();
		})
	};

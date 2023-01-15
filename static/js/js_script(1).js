window.addEventListener('scroll', function(){
			const header = document.querySelector('header');
			header.classList.toggle("sticky", window.scrollY > 0);
			});

			function toggleMenu(){
			const MenuToggle=document.querySelector('.MenuToggle');
			const navigation = document.querySelector('.navigation');
			MenuToggle.classList.toggle('active');
			navigation.classList.toggle('active');
			}
			


		function numberofshoots() {
			var value = parseInt(document.getElementById('inputX').value, 10) + parseInt(document.getElementById('inputXx').value, 10) + parseInt(document.getElementById('inputdziewiec').value, 10) + parseInt(document.getElementById('inputosiem').value, 10) + parseInt(document.getElementById('inputsiedem').value, 10) + parseInt(document.getElementById('inputszesc').value, 10) + parseInt(document.getElementById('inputpiec').value, 10) + parseInt(document.getElementById('inputcztery').value, 10) + parseInt(document.getElementById('inputtrzy').value, 10) + parseInt(document.getElementById('inputdwa').value, 10) + parseInt(document.getElementById('inputjeden').value, 10);

			 document.getElementById('numberofshoots').value = value;
			}


		function finalValueDynamicShooting() {
			var value = parseFloat(document.getElementById('czas').value,10) + parseInt(document.getElementById('inputmiss').value)*parseInt(document.getElementById('missref').value) + parseInt(document.getElementById('inputprocedura').value)*parseInt(document.getElementById('proceduraref').value) + parseInt(document.getElementById('inputnoshoot').value)*parseInt(document.getElementById('noshootref').value);
			document.getElementById('inputwartosc_koncowa_miss').value = parseInt(document.getElementById('inputmiss').value, 10) * parseInt(document.getElementById('missref').value, 10);
			document.getElementById('inputwartosc_koncowa_procedura').value = parseInt(document.getElementById('inputprocedura').value, 10) * parseInt(document.getElementById('proceduraref').value, 10);
			document.getElementById('inputwartosc_koncowa_noshoot').value = parseInt(document.getElementById('inputnoshoot').value, 10) * parseInt(document.getElementById('noshootref').value, 10);
			document.getElementById('wynik_koncowy').value = value;
			}

		function increaseValueX() {
			  var value = parseInt(document.getElementById('inputX').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputX').value = value;
			  numberofshoots();
			}

			function decreaseValueX() {
			  var value = parseInt(document.getElementById('inputX').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputX').value = value;
			  numberofshoots();
			}

		function increaseValueXx() {
			  var value = parseInt(document.getElementById('inputXx').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputXx').value = value;
			  numberofshoots();
			}

			function decreaseValueXx() {
			  var value = parseInt(document.getElementById('inputXx').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputXx').value = value;
			  numberofshoots();
			}
		function increaseValuedziewiec() {
			  var value = parseInt(document.getElementById('inputdziewiec').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputdziewiec').value = value;
			  numberofshoots();
			}

			function decreaseValuedziewiec() {
			  var value = parseInt(document.getElementById('inputdziewiec').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputdziewiec').value = value;
			  numberofshoots();
			}
		function increaseValueosiem() {
			  var value = parseInt(document.getElementById('inputosiem').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputosiem').value = value;
			  numberofshoots();
			}

			function decreaseValueosiem() {
			  var value = parseInt(document.getElementById('inputosiem').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputosiem').value = value;
			  numberofshoots();
			}
		function increaseValuesiedem() {
			  var value = parseInt(document.getElementById('inputsiedem').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputsiedem').value = value;
			  numberofshoots();
			}

			function decreaseValuesiedem() {
			  var value = parseInt(document.getElementById('inputsiedem').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputsiedem').value = value;
			  numberofshoots();
			}
		function increaseValueszesc() {
			  var value = parseInt(document.getElementById('inputszesc').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputszesc').value = value;
			  numberofshoots();
			}

			function decreaseValueszesc() {
			  var value = parseInt(document.getElementById('inputszesc').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputszesc').value = value;
			  numberofshoots();
			}
		function increaseValuepiec() {
			  var value = parseInt(document.getElementById('inputpiec').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputpiec').value = value;
			  numberofshoots();
			}

			function decreaseValuepiec() {
			  var value = parseInt(document.getElementById('inputpiec').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputpiec').value = value;
			  numberofshoots();
			}
		function increaseValuecztery() {
			  var value = parseInt(document.getElementById('inputcztery').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputcztery').value = value;
			  numberofshoots();
			}

			function decreaseValuecztery() {
			  var value = parseInt(document.getElementById('inputcztery').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputcztery').value = value;
			  numberofshoots();
			}
		function increaseValuetrzy() {
			  var value = parseInt(document.getElementById('inputtrzy').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputtrzy').value = value;
			  numberofshoots();
			}

			function decreaseValuetrzy() {
			  var value = parseInt(document.getElementById('inputtrzy').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputtrzy').value = value;
			  numberofshoots();
			}
		function increaseValuedwa() {
			  var value = parseInt(document.getElementById('inputdwa').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputdwa').value = value;
			  numberofshoots();
			}

			function decreaseValuedwa() {
			  var value = parseInt(document.getElementById('inputdwa').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputdwa').value = value;
			  numberofshoots();
			}
		function increaseValuejeden() {
			  var value = parseInt(document.getElementById('inputjeden').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputjeden').value = value;
			  numberofshoots();
			}

			function decreaseValuejeden() {
			  var value = parseInt(document.getElementById('inputjeden').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputjeden').value = value;
			  numberofshoots();
			}
		function increaseValuekara_punktowa() {
			  var value = parseInt(document.getElementById('inputkara_punktowa').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputkara_punktowa').value = value;
			  numberofshoots();
			}

			function decreaseValuekara_punktowa() {
			  var value = parseInt(document.getElementById('inputkara_punktowa').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputkara_punktowa').value = value;
			  numberofshoots();
			}

		function increaseValueMiss() {
			  var value = parseInt(document.getElementById('inputmiss').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputmiss').value = value;
			  document.getElementById('inputwartosc_koncowa_miss').value = parseInt(document.getElementById('inputmiss').value, 10) * parseInt(document.getElementById('missref').value, 10);
			  finalValueDynamicShooting();
			}

			function decreaseValueMiss() {
			  var value = parseInt(document.getElementById('inputmiss').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputmiss').value = value;
			  document.getElementById('inputwartosc_koncowa_miss').value = parseInt(document.getElementById('inputmiss').value, 10) * parseInt(document.getElementById('missref').value, 10);
			  finalValueDynamicShooting();

			  
			}

		function increaseValueProcedura() {
			  var value = parseInt(document.getElementById('inputprocedura').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputprocedura').value = value;
			  document.getElementById('inputwartosc_koncowa_procedura').value = parseInt(document.getElementById('inputprocedura').value, 10) * parseInt(document.getElementById('proceduraref').value, 10);
			  finalValueDynamicShooting();
			}

			function decreaseValueProcedura() {
			  var value = parseInt(document.getElementById('inputprocedura').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputprocedura').value = value;
			  document.getElementById('inputwartosc_koncowa_procedura').value = parseInt(document.getElementById('inputprocedura').value, 10) * parseInt(document.getElementById('proceduraref').value, 10);
			  finalValueDynamicShooting();
			}

		function increaseValueNoShoot() {
			  var value = parseInt(document.getElementById('inputnoshoot').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value++;
			  document.getElementById('inputnoshoot').value = value;
			  document.getElementById('inputwartosc_koncowa_noshoot').value = parseInt(document.getElementById('inputnoshoot').value, 10) * parseInt(document.getElementById('noshootref').value, 10);
			  finalValueDynamicShooting();
			}

		function decreaseValueNoShoot() {
			  var value = parseInt(document.getElementById('inputnoshoot').value, 10);
			  value = isNaN(value) ? 0 : value;
			  value < 1 ? value = 1 : '';
			  value--;
			  document.getElementById('inputnoshoot').value = value;
			  document.getElementById('inputwartosc_koncowa_noshoot').value = parseInt(document.getElementById('inputnoshoot').value, 10) * parseInt(document.getElementById('noshootref').value, 10);
			  finalValueDynamicShooting();
			}

		function SelectorById(){
			const classes = [];

			for (const elem of document.querySelectorAll('[id $= "oplata"]')) {

			    classes.push(elem.id);
			}
			// console.log(classes);


			for (const elem of classes){
				// console.log('CLASSES', elem);
				// console.log('CLASSES val', document.getElementById(elem).checked);
				document.getElementById(elem).checked = true;
			}
		}



		function HideImie(){
			
			const classes = [];

			for (const elem of document.querySelectorAll('[id $= "imie"]')) {

			    classes.push(elem);
			}
			// console.log(classes);




			for (const elem of classes){

				if (elem.style.display == "none"){
					$(elem).show();

					console.log(elem.style.display);
				} else {
					$(elem).hide();
				}
				console.log(elem.classList);
			}

		}
	
'use strict'

// authentication
if (document.querySelector('.auth')) {
	// authentication tab
	const authHeader = document.querySelectorAll('.auth__header__item')
	authHeader.forEach((item) => {
		item.addEventListener('click', () => {
			const attr = item.getAttribute('data-auth')
			for (let header of authHeader) {
				header.classList.remove('active')
			}
			item.classList.add('active')

			document.querySelectorAll('.auth__body').forEach((body) => {
				body.classList.remove('active')
			})
			document.querySelector(`.auth__body--${attr}`).classList.add('active')
		})
	})

	// auth forget
	if (document.querySelector('.auth__forget')) {
		document.querySelector('.auth__forget').addEventListener('click', () => {
			for (let header of authHeader) {
				header.classList.remove('active')
			}
			document.querySelector('div[data-auth=register]').classList.add('active')

			document.querySelectorAll('.auth__body').forEach((body) => {
				body.classList.remove('active')
			})
			document.querySelector(`.auth__body--restore`).classList.add('active')
		})
	}

	if(document.querySelector('.auth__body--restore')) {
		document.querySelector('.auth__body--restore .btn').addEventListener('click', () => {
			document.querySelectorAll('.auth__body').forEach((body) => {
				body.classList.remove('active')
			})
			document.querySelector(`.auth__body--update`).classList.add('active')
		})
	}
}

// language switcher
document.querySelector('.header__globe').addEventListener('click', (e) => {
	e.stopPropagation()
	document.querySelector('.header__lang__list').classList.toggle('active')
})

document.querySelector('.header__lang__list').addEventListener('click', (e) => {
	e.stopPropagation()
})

document.querySelector('body, html').addEventListener('click', () => {
	document.querySelector('.header__lang__list').classList.remove('active')
})

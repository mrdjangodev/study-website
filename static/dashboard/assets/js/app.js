'use strict'

/* SELECT */
const selectBtn = document.querySelectorAll('.input__btn')
const selectList = document.querySelectorAll('.input__list')
const selectOption = document.querySelectorAll('.input__option')
if (selectBtn.length > 0) {
	selectBtn.forEach((btn) => {
		btn.addEventListener('click', (e) => {
			e.stopPropagation()

			if (!btn.nextElementSibling.classList.contains('active')) {
				for (let list of selectList) {
					list.classList.remove('active')
				}
			}

			btn.nextElementSibling.classList.toggle('active')
		})
	})
}

selectList.forEach((list) => {
	list.addEventListener('click', () => {
		list.classList.remove('active')
	})
})

for (let option of selectOption) {
	option.addEventListener('click', () => {
		const optionValue = option.innerText
		option.parentElement.parentElement.parentElement.previousElementSibling.previousElementSibling.setAttribute(
			'value',
			optionValue
		)
	})
}

document.querySelector('body').addEventListener('click', () => {
	document.querySelectorAll('.input__list').forEach((list) => {
		list.classList.remove('active')
	})
})

/* FAQ HELP */
document.querySelectorAll('.help__head').forEach((head) => {
	head.addEventListener('click', () => {
		head.parentElement.classList.toggle('active')
		let body = head.nextElementSibling
		if (body.style.maxHeight) {
			body.style.maxHeight = null
		} else {
			body.style.maxHeight = body.scrollHeight + 'px'
		}
	})
})

/* FAQ DASHBOARD */
const dashBtn = document.querySelector('.dash__btn')
const dashNav = document.querySelectorAll('.dash__nav__item')
if (dashBtn) {
	dashBtn.addEventListener('click', () => {
		dashBtn.classList.toggle('active')
		let body = dashBtn.nextElementSibling
		if (body.style.maxHeight) {
			body.style.maxHeight = null
		} else {
			body.style.maxHeight = body.scrollHeight + 'px'
		}
	})
}
if (dashNav) {
	for (let nav of dashNav) {
		nav.addEventListener('click', () => {
			if (window.innerWidth < 676) {
				nav.parentElement.style.maxHeight = null
			}
		})
	}
}

/* HEADER SETTINGS SWITCHER */
document.querySelector('.header__profile').addEventListener('click', (e) => {
	e.stopPropagation()
	document.querySelector('.header__list').classList.toggle('active')
	document.querySelector('.notes').classList.remove('active')
})

document.querySelector('body, html').addEventListener('click', () => {
	document.querySelector('.header__list').classList.remove('active')
})

/* RESULT FILTER SWITCHER */
if (document.querySelector('.result')) {
	document.querySelector('.result__current').addEventListener('click', (e) => {
		e.stopPropagation()
		document.querySelector('.result__list').classList.toggle('active')
	})

	document.querySelector('body, html').addEventListener('click', () => {
		document.querySelector('.result__list').classList.remove('active')
	})
}

/* EXIT MODAL SWITCHER */
document
	.querySelector('.header__list__item.btn-exit')
	.addEventListener('click', (e) => {
		e.stopPropagation()
		e.preventDefault()
		document.querySelector('.modal--exit').classList.add('active')
		document.querySelector('.header__list').classList.remove('active')
	})

document.querySelector('body, html').addEventListener('click', () => {
	document.querySelector('.modal--exit').classList.remove('active')
})

if (document.querySelector('.modal--error')) {
	document
		.querySelector('.modal--error')
		.querySelector('i.bx-x-circle')
		.addEventListener('click', () => {
			document.querySelector('.modal--error').classList.remove('active')
		})
}

/* HEADER SEARCH SWITCHER */
document
	.querySelector('.header__search__switch')
	.addEventListener('click', (e) => {
		e.stopPropagation()
		document.querySelector('.header__search').classList.toggle('active')
	})

document.querySelector('body').addEventListener('click', () => {
	document.querySelector('.header__search').classList.remove('active')
})
document.querySelector('.header__search').addEventListener('click', (e) => {
	e.stopPropagation()
})

/* HEADER NOTES SWITCHER */
document.querySelector('.header__ring').addEventListener('click', (e) => {
	e.stopPropagation()
	document.querySelector('.notes').classList.toggle('active')
})

document.querySelector('.notes').addEventListener('click', (e) => {
	e.stopPropagation()
})

document.querySelector('body').addEventListener('click', () => {
	document.querySelector('.notes').classList.remove('active')
})

/* HEADER RING COLOR CHANGE */
if (document.querySelector('.header__ring span').innerText !== '') {
	document.querySelector('.header__ring').classList.add('active')
} else {
	document.querySelector('.header__ring').classList.remove('active')
}

/* INPUT TYPE FILE */
if (document.querySelector('#dash__file')) {
	document.querySelector('#dash__file').onchange = function () {
		document.querySelector('#dash__filename').textContent = this.files[0].name
	}
}

/* INPUT CANCEL SIGN */
const inputNotSelect = document.querySelectorAll('.input:not(.select)')
if (inputNotSelect) {
	inputNotSelect.forEach((i) => {
		i.addEventListener('keyup', () => {
			if (i.value.length > 0) {
				i.nextElementSibling.classList.add('active')
			} else {
				i.nextElementSibling.classList.remove('active')
			}
		})
	})
	inputNotSelect.forEach((i) => {
		i.addEventListener('focus', () => {
			if (i.value.length > 0) {
				i.nextElementSibling.classList.add('active')
			} else {
				i.nextElementSibling.classList.remove('active')
			}
		})
	})
	document.querySelectorAll('.input__cancel').forEach((i) => {
		i.addEventListener('click', () => {
			i.previousElementSibling.value = ''
			i.classList.remove('active')
		})
	})
}

/* DASHBOARD NAVIGATION */
const navs = document.querySelectorAll('div[data-nav]')
const dashs = document.querySelectorAll('.dash__item')
navs.forEach((nav) => {
	nav.addEventListener('click', () => {
		for (let nav of navs) {
			nav.classList.remove('active')
		}
		nav.classList.add('active')

		for (let dash of dashs) {
			dash.classList.remove('active')
		}
		const data = nav.getAttribute('data-nav')
		document.querySelector(`.dash__item--${data}`).classList.add('active')
	})
})

/* SIDEBAR */
document.querySelector('.header__burger').addEventListener('click', () => {
	document.querySelector('.side').classList.add('active')
	document.querySelector('.cancel__bg').classList.add('active')
})

document.querySelector('.side__cancel').addEventListener('click', () => {
	document.querySelector('.side').classList.remove('active')
	document.querySelector('.cancel__bg').classList.remove('active')
})

/* MODULS */
const progress = document.querySelectorAll('.moduls__progress')

progress.forEach((pr) => {
	let data = pr.getAttribute('data-progress')
	if (parseInt(data) > 5) {
		pr.children[0].style.width = `${data}%`
		pr.children[0].innerText = `${data}%`
	}
})

/* TAB SWITCH */
const tabs = document.querySelectorAll('.tab__head span')

tabs.forEach((tab) => {
	tab.addEventListener('click', () => {
		for (let el of tabs) {
			el.classList.remove('active')
		}
		tab.classList.add('active')

		for (let body of document.querySelectorAll('.tab__body')) {
			body.classList.remove('active')
		}
		document
			.querySelector(`.${tab.getAttribute('data-tab')}`)
			.classList.add('active')
	})
})

/* PLAYER */
const players = Array.from(document.querySelectorAll('video')).map(
	(p) => new Plyr(p)
)

/* CHART */
const configs = []
for (let el of document.querySelectorAll('.data')) {
	const color = el.getAttribute('data-color')
	const lessons = el.getAttribute('data-lessons')
	const scores = [...el.getAttribute('data-scores').split(',')]

	const labels = []
	for (let i = 0; i < parseInt(lessons); ++i) {
		labels.push((i + 1).toString() + '-section')
	}
	const data = {
		labels: labels,
		datasets: [
			{
				data: scores,
				borderColor: color,
				backgroundColor: color,
				cubicInterpolationMode: 'monotone',
				tension: 0.4,
			},
		],
	}

	// config
	const config = {
		type: 'line',
		data,
		options: {
			responsive: true,
			interaction: {
				intersect: false,
			},
			scales: {
				y: {
					min: 0,
					max: 100,
					ticks: {
						stepSize: 25,
					},
				},
			},
			plugins: {
				legend: {
					display: false,
				},
			},
		},
	}

	configs.push(config)
}

// init
document.querySelectorAll('.chart').forEach((chart, i) => {
	const myChart = new Chart(chart, configs[i])
})

document.querySelectorAll('.faq__header').forEach((header) => {
	header.addEventListener('click', () => {
		header.parentElement.classList.toggle('active')
		let body = header.nextElementSibling
		if (body.style.maxHeight) {
			body.style.maxHeight = null
		} else {
			body.style.maxHeight = body.scrollHeight + 'px'
		}
	})
})

// document
// 	.querySelector('.header__lang__current')
// 	.addEventListener('click', (e) => {
// 		e.stopPropagation()
// 		document.querySelector('.header__lang__list').classList.toggle('active')
// 	})

// document.querySelector('.header__lang__list').addEventListener('click', (e) => {
// 	e.stopPropagation()
// })

// document.querySelector('body, html').addEventListener('click', () => {
// 	document.querySelector('.header__lang__list').classList.remove('active')
// })

const slider = document.querySelector('.video__head')
let isDown = false
let startX
let scrollLeft

if (slider) {
	slider.addEventListener('mousedown', (e) => {
		isDown = true
		slider.classList.add('active')
		startX = e.pageX - slider.offsetLeft
		scrollLeft = slider.scrollLeft
	})
	slider.addEventListener('mouseleave', () => {
		isDown = false
		slider.classList.remove('active')
	})
	slider.addEventListener('mouseup', () => {
		isDown = false
		slider.classList.remove('active')
	})
	slider.addEventListener('mousemove', (e) => {
		if (!isDown) return
		e.preventDefault()
		const x = e.pageX - slider.offsetLeft
		const walk = x - startX //scroll-fast
		slider.scrollLeft = scrollLeft - walk
	})
}

// const selectBtn = document.querySelector('.auth__select__btn')
// const selectList = document.querySelector('.auth__select__list')
// const selectOption = document.querySelectorAll('.auth__select__option')
// if (selectBtn) {
// 	selectBtn.addEventListener('click', (e) => {
// 		selectBtn.nextElementSibling.classList.toggle('active')
// 	})
// }

// selectList.addEventListener('click', () => {
// 	selectList.classList.remove('active')
// })

// for (let option of selectOption) {
// 	option.addEventListener('click', () => {
// 		const optionValue = option.innerText
// 		document
// 			.querySelector('.auth__input.select')
// 			.setAttribute('placeholder', optionValue)
// 	})
// }

$('.stat__inner').owlCarousel({
	responsive: {
		0: {
			items: 1,
		},
		992: {
			items: 2,
		},
	},
})

/* ======== TEST ======== */

if (document.querySelector('.tests')) {
	// progress bar and timer
	function startTimer(duration, display) {
		var timer = duration,
			minutes,
			seconds
		const intervalId = setInterval(function () {
			minutes = parseInt(timer / 60, 10)
			seconds = parseInt(timer % 60, 10)

			minutes = minutes < 10 ? '0' + minutes : minutes
			seconds = seconds < 10 ? '0' + seconds : seconds

			display.textContent = minutes + ':' + seconds
			document.querySelector('.test__progress span').style.width =
				(timer / duration) * 100 + '%'

			if (--timer < 0) {
				clearInterval(intervalId)
			}
		}, 1000)
	}

	window.onload = function () {
		const time = document.querySelector('.test__time')

		if (time) {
			startTimer(time.getAttribute('data-time'), time)
		}
	}

	// make green bg
	const labels = document.querySelectorAll('.test ul li label')
	labels.forEach((label) => {
		label.addEventListener('click', () => {
			for (let li of label.parentElement.parentElement.children) {
				li.classList.remove('active')
			}
			label.parentElement.classList.add('active')

			document
				.querySelector(
					`[data-test=${label.parentElement.parentElement.parentElement.classList[1]}]`
				)
				.classList.add('done')
		})
	})

	// test switch
	const nums = document.querySelectorAll('.test__nums li')
	nums.forEach((num) => {
		num.addEventListener('click', () => {
			const nth = num.getAttribute('data-test')

			// num bg-color
			for (let el of nums) {
				el.classList.remove('active')
			}
			num.classList.add('active')

			// switch tests
			for (let test of document.querySelectorAll('.test')) {
				test.classList.remove('active')
			}
			document.querySelector(`.${nth}`).classList.add('active')

			// prev, next, submit buttons
			if (nth === 'test-1') {
				for (let btn of document.querySelectorAll('.test__body .btn')) {
					btn.classList.remove('active')
				}
				document.querySelector('.test__body').classList.add('loaded')
				document.querySelector('.btn.next').classList.add('active')
			} else if (nth === 'test-' + nums.length.toString()) {
				for (let btn of document.querySelectorAll('.test__body .btn')) {
					btn.classList.remove('active')
				}
				document.querySelector('.test__body').classList.remove('loaded')
				document.querySelector('.btn.prev').classList.add('active')
				document.querySelector('.test__body button').classList.add('active')
			} else {
				for (let btn of document.querySelectorAll('.test__body .btn')) {
					btn.classList.remove('active')
				}
				document.querySelector('.test__body').classList.remove('loaded')
				document.querySelector('.btn.prev').classList.add('active')
				document.querySelector('.btn.next').classList.add('active')
			}
		})
	})

	// buttons prev and next
	document.querySelectorAll('.test__body a.btn').forEach((btn) => {
		btn.addEventListener('click', (e) => {
			e.preventDefault()
			const btnType = btn.classList[1]

			const activeIndex = [
				...document.querySelectorAll('.test__nums li'),
			].indexOf(document.querySelector('.test__nums li.active'))

			// switch tests

			// btns
			if (btnType === 'next') {
				for (let num of nums) {
					num.classList.remove('active')
				}
				nums[activeIndex + 1].classList.add('active')

				for (let test of document.querySelectorAll('.test')) {
					test.classList.remove('active')
				}
				document
					.querySelector(`.test-${activeIndex + 2}`)
					.classList.add('active')

				if (activeIndex === nums.length - 2) {
					for (let btn of document.querySelectorAll('.test__body .btn')) {
						btn.classList.remove('active')
					}
					document.querySelector('.test__body').classList.remove('loaded')
					document.querySelector('.btn.prev').classList.add('active')
					document.querySelector('.test__body button').classList.add('active')
				} else {
					for (let btn of document.querySelectorAll('.test__body .btn')) {
						btn.classList.remove('active')
					}
					document.querySelector('.test__body').classList.remove('loaded')
					document.querySelector('.btn.prev').classList.add('active')
					document.querySelector('.btn.next').classList.add('active')
				}
			}

			if (btnType === 'prev') {
				for (let num of nums) {
					num.classList.remove('active')
				}
				nums[activeIndex - 1].classList.add('active')

				for (let test of document.querySelectorAll('.test')) {
					test.classList.remove('active')
				}
				document.querySelector(`.test-${activeIndex}`).classList.add('active')

				if (activeIndex === 1) {
					for (let btn of document.querySelectorAll('.test__body .btn')) {
						btn.classList.remove('active')
					}
					document.querySelector('.test__body').classList.add('loaded')
					document.querySelector('.btn.next').classList.add('active')
				} else {
					for (let btn of document.querySelectorAll('.test__body .btn')) {
						btn.classList.remove('active')
					}
					document.querySelector('.test__body').classList.remove('loaded')
					document.querySelector('.btn.prev').classList.add('active')
					document.querySelector('.btn.next').classList.add('active')
				}
			}
		})
	})
}

/* ======== TEST ======== */

// var scrollToTopBtn = document.querySelector('.up')
// var phoneBtn = document.querySelector('.phone')
// var rootElement = document.documentElement

// function handleScroll() {
// 	if (rootElement.scrollTop > 800) {
// 		scrollToTopBtn.classList.add('active')
// 		phoneBtn.classList.add('active')
// 	} else {
// 		scrollToTopBtn.classList.remove('active')
// 		phoneBtn.classList.remove('active')
// 	}
// }

// function scrollToTop() {
// 	rootElement.scrollTo({
// 		top: 0,
// 		behavior: 'smooth',
// 	})
// }
// scrollToTopBtn.addEventListener('click', scrollToTop)
// document.addEventListener('scroll', handleScroll)

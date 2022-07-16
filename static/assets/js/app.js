'use strict'

const search = document.querySelector('.header__search')
document.querySelector('.header__search-btn').addEventListener('click', (e) => {
	e.stopPropagation()
	search.classList.toggle('active')
})

search.addEventListener('click', (e) => {
	e.stopPropagation()
})

document.querySelector('body').addEventListener('click', () => {
	search.classList.remove('active')
})

// AOS
AOS.init({
	once: true,
	duration: 700,
})

document.querySelectorAll('.faq__head').forEach((head) => {
	head.addEventListener('click', () => {
		for (let item of document.querySelectorAll('.faq__item')) {
			item.classList.remove('active')
			item.children[1].style.maxHeight = null
		}
		head.parentElement.classList.toggle('active')
		let body = head.nextElementSibling
		if (body.style.maxHeight) {
			body.style.maxHeight = null
		} else {
			body.style.maxHeight = body.scrollHeight + 'px'
		}
	})
})

// language switcher
const lang = document.querySelector('.lang')

lang.addEventListener('mouseover', () => {
	lang.classList.add('active')
})

lang.addEventListener('mouseout', () => {
	lang.classList.remove('active')
})

$('.news__inner').slick({
	slidesToShow: 3,
	slidesToScroll: 1,
	arrows: false,
	dots: true,
	infinite: false,
	responsive: [
		{
			breakpoint: 992,
			settings: {
				slidesToShow: 2,
			},
		},
		{
			breakpoint: 676,
			settings: {
				slidesToShow: 1,
			},
		},
	],
})

var scrollToTopBtn = document.querySelector('.up')
var rootElement = document.documentElement

function handleScroll() {
	if (rootElement.scrollTop > 800) {
		scrollToTopBtn.classList.add('active')
	} else {
		scrollToTopBtn.classList.remove('active')
	}
}

function scrollToTop() {
	rootElement.scrollTo({
		top: 0,
		behavior: 'smooth',
	})
}
scrollToTopBtn.addEventListener('click', scrollToTop)
document.addEventListener('scroll', handleScroll)

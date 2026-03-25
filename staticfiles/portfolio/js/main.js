// Smooth scroll for nav links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Animate skill bars on scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.transition = 'width 1s ease';
        }
    });
});
document.querySelectorAll('.skill-fill').forEach(bar => observer.observe(bar));

const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            fadeObserver.unobserve(entry.target); // animate only once
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll(
    '.research-card, .cert-card, .achieve-card, .extra-card'
).forEach(card => {
    card.classList.add('fade-in');
    fadeObserver.observe(card);
});
// ========================================
// Form Validation and Handling
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('towingForm');
    const phoneInput = document.getElementById('phone');

    // Phone number formatting
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length > 10) {
                value = value.slice(0, 10);
            }

            let formattedValue = '';
            if (value.length > 0) {
                formattedValue = value.slice(0, 3);
            }
            if (value.length > 3) {
                formattedValue += '-' + value.slice(3, 6);
            }
            if (value.length > 6) {
                formattedValue += '-' + value.slice(6, 10);
            }

            e.target.value = formattedValue;
        });
    }

    // Form submission handling
    if (form) {
        form.addEventListener('submit', function(e) {
            // Basic validation
            const name = document.getElementById('name').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const service = document.getElementById('service').value;

            if (!name || !phone || !service) {
                e.preventDefault();
                alert('Please fill in all required fields.');
                return false;
            }

            // Phone validation
            const phoneRegex = /^\d{3}-\d{3}-\d{4}$/;
            if (!phoneRegex.test(phone)) {
                e.preventDefault();
                alert('Please enter a valid phone number in format: 555-555-5555');
                return false;
            }

            // If using a custom form handler instead of Formspree, prevent default and handle with AJAX
            // For now, form will submit normally to the action URL
        });
    }

    // Smooth scroll for navigation links (additional to CSS smooth scroll)
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId !== '#' && targetId.length > 1) {
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    e.preventDefault();
                    const headerOffset = 80;
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Add active state to navigation on scroll
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('.main-nav a[href^="#"]');

    function highlightNavigation() {
        const scrollPosition = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navItems.forEach(item => {
                    item.classList.remove('active');
                    if (item.getAttribute('href') === `#${sectionId}`) {
                        item.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', highlightNavigation);

    // Track phone clicks for analytics (if you add analytics later)
    const phoneLinks = document.querySelectorAll('a[href^="tel:"]');
    phoneLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Add analytics tracking here if needed
            console.log('Phone link clicked');
            // Example: gtag('event', 'phone_click', { 'event_category': 'contact' });
        });
    });

    // Add animation on scroll for service cards
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe service cards and benefit cards for animation
    const animatedElements = document.querySelectorAll('.service-card, .benefit-card, .point, .faq-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Emergency CTA highlight on scroll
    const emergencyNotice = document.querySelector('.emergency-notice');
    if (emergencyNotice) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 800) {
                emergencyNotice.style.animation = 'pulse 2s infinite';
            }
        });
    }
});

// Add pulse animation to CSS dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes pulse {
        0%, 100% {
            box-shadow: 0 0 0 0 rgba(255, 107, 0, 0.7);
        }
        50% {
            box-shadow: 0 0 0 10px rgba(255, 107, 0, 0);
        }
    }

    .main-nav a.active {
        color: #ff6b00;
        border-bottom: 2px solid #ff6b00;
    }
`;
document.head.appendChild(style);
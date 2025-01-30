const steps = document.querySelectorAll('.form-step');
const nextButton = document.getElementById('nextButton');
const prevButton = document.getElementById('prevButton');
const submitButton = document.getElementById('submitButton');
const form = document.getElementById('multiPageForm');
let currentStep = 0;

function showStep(step) {
    steps.forEach((stepElement, index) => {
        stepElement.classList.toggle('active', index === step);
    });
    prevButton.disabled = step === 0;
    nextButton.style.display = step === steps.length - 1 ? 'none' : 'inline-block';
    submitButton.style.display = step === steps.length - 1 ? 'inline-block' : 'none';
    if (step === steps.length - 1) {
        document.getElementById('review-name').textContent = form.name.value;
        document.getElementById('review-email').textContent = form.email.value;
        document.getElementById('review-address').textContent = form.address.value;
        document.getElementById('review-city').textContent = form.city.value;
    }
}

nextButton.addEventListener('click', () => {
    if (currentStep < steps.length - 1) {
        currentStep++;
        showStep(currentStep);
    }
});

prevButton.addEventListener('click', () => {
    if (currentStep > 0) {
        currentStep--;
        showStep(currentStep);
    }
});

form.addEventListener('submit', (event) => {
    event.preventDefault();
    alert('Form submitted successfully!');
});

showStep(currentStep);

function showStep(step) {
    const steps = document.querySelectorAll('.form-step');
    steps.forEach((stepElement, index) => {
        stepElement.style.display = (index === step) ? 'block' : 'none';
    });
}

function nextStep(currentStep) {
    showStep(currentStep + 1);
}

function prevStep(currentStep) {
    showStep(currentStep - 1);
}

document.addEventListener('DOMContentLoaded', () => {
    showStep(0);
});

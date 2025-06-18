const form = document.getElementById('car-form');
        form.addEventListener('submit', async function(event) {
            event.preventDefault();
            
            // Collect form data
            const formData = {
                name: document.getElementById('name').value,
                company: document.getElementById('company').value,
                year: parseInt(document.getElementById('year').value),
                kms_driven: parseInt(document.getElementById('kms_driven').value),
                fuel_type: document.getElementById('fuel_type').value
            };

            // Send the data to the FastAPI backend
            const response = await fetch('http://localhost:8000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            const data = await response.json();

            // Display the result
            document.getElementById('result').innerText = `Predicted Price: ${data.prediction}`;
        });
document.getElementById('city-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const city = document.getElementById('city-input').value;
    
    fetch('/weather', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `city=${city}`,
    })
    .then(response => response.json())
    .then(data => {
      const weatherResult = document.getElementById('weather-result');
      if (data.error) {
        weatherResult.innerHTML = `<p>${data.error}</p>`;
      } else {
        const cityInfo = data.city_info.results[0];
        const weatherData = data.weather_data.current;
        weatherResult.innerHTML = `
          <h3>Weather in ${cityInfo.name}</h3>
          <p>Country: ${cityInfo.country}</p>
          <p>Latitude: ${cityInfo.latitude}</p>
          <p>Longitude: ${cityInfo.longitude}</p>
          <h4>Current Weather:</h4>
          <p>Temperature: ${weatherData.temperature_2m} °C</p>
          <p>Time: ${weatherData.time}</p>
        `;
      }
    })
    .catch(error => {
      console.error('Error fetching weather data:', error);
    });
  });
  
  document.getElementById('city-input').addEventListener('input', function() {
    const query = this.value;
    if (query.length > 2) {
      fetch(`/autocomplete?q=${query}`)
        .then(response => response.json())
        .then(data => {
          const suggestions = document.getElementById('suggestions');
          suggestions.innerHTML = '';
          data.forEach(city => {
            const div = document.createElement('div');
            div.textContent = city;
            div.addEventListener('click', function() {
              document.getElementById('city-input').value = city;
              suggestions.innerHTML = '';
            });
            suggestions.appendChild(div);
          });
        })
        .catch(error => {
          console.error('Error fetching city suggestions:', error);
        });
    }
  });
  
var ubicacion = navigator.geolocation;
var longitud = 0;
var latitud = 0;
ubicacion.getCurrentPosition(position=>{
     latitud= position.coords.latitude;
     longitud= position.coords.longitude;
     console.log(latitud,longitud)
     
    
    
})

//fetch( `https://api.weatherbit.io/v2.0/current?lat=-33.4931768&lon=-70.6097705&key=6935272bfe794a07b91887d8f6d82fc1&include=minutely`)
//.then(response =>response.json()).then(data => console.log(data.data[0].temp +"°C"))
fetch("https://api.openweathermap.org/data/2.5/weather?lat=-33.57627&lon=-70.6357953&appid=3242b1dab11daf94dbb5c2c45df0e07a").
then(response=>response.json()).then(data=>console.log(data.weather[0].description))

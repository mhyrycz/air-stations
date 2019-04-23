import React from 'react';

const WeatherOfStation = props => {
  const { temperature, aqi, humidity, airPressure } = props.stationData
  
  return (
    <div className="station-column">
      <div className="address">
        {props.label}
      </div>
      <div className="aqi">
        {aqi}
      </div>
      <div className="row">
        <div className="param">
          <div className="param2">
            Temperatura [℃]
          </div>
          <div className="param2">
            {temperature}
          </div>
        </div>
        <div className="param">
          <div className="param2">
            Ciśnienie [hPa]
          </div>
          <div className="param2">
            {airPressure}
          </div>
        </div>
        <div className="param">
          <div className="param2">
            Wilgotność [%]
          </div>
          <div className="param2">
            {humidity}
          </div>
        </div>
      </div>
    </div>
  )

}

export default WeatherOfStation;
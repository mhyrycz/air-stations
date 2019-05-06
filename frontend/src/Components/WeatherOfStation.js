import React from 'react';
import DonutChart from "react-svg-donut-chart";

const WeatherOfStation = props => {
  const { temperature, aqi, humidity, airPressure } = props.stationData

  const data = [
    { value: 60, stroke: "#2f7d6d" }
  ]
  
  return (
    <div className={props.className}>
      <div className="circle">
        <DonutChart height="700" data={data} />
      </div>
      <div className="address">
        {props.label}
      </div>
      <div className="aqi">
        <div className="aqi-value ">
          {aqi}
        </div>
      </div>
      <div className="row">
        <div className="param">
          <div className="param2">
            Temp.
          </div>
          <div className="param2">
            [℃]
          </div>
          <div className="param2">
            {temperature}
          </div>
        </div>
        <div className="param">
          <div className="param2">
            Ciśnienie
          </div>
          <div className="param2">
            [hPa]
          </div>
          <div className="param2">
            {airPressure}
          </div>
        </div>
        <div className="param">
          <div className="param2">
            Wilgotność
          </div>
          <div className="param2">
            [%]
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
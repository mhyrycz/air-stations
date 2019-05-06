import React from 'react';
import DonutChart from "react-svg-donut-chart";


class WeatherOfStation extends React.Component {
  constructor() {
    super();
    this.state = {
      height: 182
    }
  }

  componentDidMount() {
    this.updateDimensions();
    window.addEventListener("resize", this.updateDimensions.bind(this));
  }

  componentWillUnmount() {
    window.removeEventListener("resize", this.updateDimensions.bind(this));
  }

  updateDimensions() {
    const update_height = this.divElement.clientWidth;
    this.setState({ height: update_height });
  }

  
  render() {
    
    const { temperature, aqi, humidity, airPressure } = this.props.stationData

    const data = [
      { value: 60, stroke: "#2f7d6d", strokeWidth: 2 }
    ]

    return (
      <div className={this.props.className} ref={(divElement) => this.divElement = divElement} >
        <div className="circle">
          <DonutChart height={this.state.height} data={data} />
        </div>
        <div className="address">
          {this.props.label}
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
}

export default WeatherOfStation;
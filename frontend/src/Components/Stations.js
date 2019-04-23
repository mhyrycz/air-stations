import React, { Component } from 'react';
import WeatherOfStation from './WeatherOfStation'
// import DonutChart from "react-svg-donut-chart"
import { config } from '../config.js'

class Stations extends Component {
  constructor(props) {
    super(props);

    this.state = {
      firstStation: {
        address: "",
        air: { 
          aqi: 0,
          airPressure: 0,
          temperature: 0,
          humidity:0,
        }
      },
      secondStation: {
        address: "",
        air: {
          aqi: 0,
          airPressure: 0,
          temperature: 0,
          humidity: 0,
        }
      },
      thirdStation: {
        address: "",
        air: {
          aqi: 0,
          airPressure: 0,
          temperature: 0,
          humidity: 0,
        }
      }
    };
  }

  componentDidMount() {
    this.getData();
    this.timer = setInterval(() => this.getData(), 600000)
  }

  getData() {
    fetch(config.backend_url)
      .then(response => { return response.json() })
      .then(json => {
        this.setState({
          firstStation: {
            address: json[0]["address"],
            air: json[0]["air"]
          },
          secondStation: {
            address: json[1]["address"],
            air: json[1]["air"]
          },
          thirdStation: {
            address: json[2]["address"],
            air: json[2]["air"]
          },
        })
      }
    );
  }



  render() {
    const { firstStation, secondStation, thirdStation } = this.state
    return(
      <div className="stations">
        <WeatherOfStation label={firstStation["address"]} stationData={firstStation["air"]}/>
        <div className="vl"></div>
        <WeatherOfStation label={secondStation["address"]} stationData={secondStation["air"]}/>
        <div className="vl"></div>
        <WeatherOfStation label={thirdStation["address"]} stationData={thirdStation["air"]}/>
      </div>
    )
  }
}

export default Stations;
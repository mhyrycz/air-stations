import React from "react";
import WeatherOfStation from "./WeatherOfStation";
import { config } from "../config.js";

class Stations extends React.Component {
  state = {
    firstStation: {
      address: "",
      air: {
        aqi: {
          value: 0,
          color: "green"
        },
        airPressure: 0,
        temperature: 0,
        humidity: 0
      }
    },
    secondStation: {
      address: "",
      air: {
        aqi: {
          value: 0,
          color: "green"
        },
        airPressure: 0,
        temperature: 0,
        humidity: 0
      }
    },
    thirdStation: {
      address: "",
      air: {
        aqi: {
          value: 0,
          color: "green"
        },
        airPressure: 0,
        temperature: 0,
        humidity: 0
      }
    }
  };

  componentDidMount() {
    this.getData();
    this.timer = setInterval(() => this.getData(), 600000);
  }

  getData() {
    fetch(config.backend_url)
      .then(response => {
        return response.json();
      })
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
          }
        });
      });
  }

  render() {
    const { firstStation, secondStation, thirdStation } = this.state;
    return (
      <div className="stations">
        <WeatherOfStation
          className="station-column left"
          label={firstStation["address"]}
          stationData={firstStation["air"]}
        />
        <WeatherOfStation
          className="station-column middle"
          label={secondStation["address"]}
          stationData={secondStation["air"]}
        />
        <WeatherOfStation
          className="station-column right"
          label={thirdStation["address"]}
          stationData={thirdStation["air"]}
        />
      </div>
    );
  }
}

export default Stations;

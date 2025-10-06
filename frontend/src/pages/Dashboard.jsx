import React, { useState } from "react";
import API from "../api";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const [city, setCity] = useState("Nairobi");
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchWeather = async () => {
    setLoading(true);
    try {
      const res = await API.get(`/weather?city=${city}`);
      if (res.data.error) {
        alert(res.data.message || "Failed to get weather");
      } else {
        setWeather(res.data);
      }
    } catch (error) {
      alert("Unable to fetch weather data. Please check your server.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center min-h-screen bg-gradient-to-b from-yellow-100 to-yellow-200 p-6">
      <div className="bg-white shadow-xl rounded-2xl p-6 w-full max-w-md transition-transform hover:scale-[1.01]">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-bold text-gray-700">Weather Dashboard</h2>
          <Link to="/signin" className="text-sm text-blue-600 hover:underline">
            Logout
          </Link>
        </div>

        <input
          value={city}
          onChange={(e) => setCity(e.target.value)}
          placeholder="Enter city name..."
          className="border border-gray-300 p-2 w-full rounded mb-3 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        />
        <button
          onClick={fetchWeather}
          disabled={loading}
          className={`${
            loading ? "bg-gray-400" : "bg-yellow-500 hover:bg-yellow-600"
          } text-white w-full py-2 rounded-md transition`}
        >
          {loading ? "Loading..." : "Get Weather"}
        </button>

        {weather && weather.main && weather.weather && (
          <div className="mt-6 text-center border-t pt-4">
            <h3 className="text-xl font-semibold text-gray-800">{weather.name}</h3>
            <p className="capitalize text-gray-600">
              {weather.weather[0]?.description}
            </p>
            <p className="text-3xl font-bold text-yellow-600 mt-2">
              {weather.main?.temp} °C
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

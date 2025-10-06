import React, { useState } from "react";
import { Link } from "react-router-dom";
import API from "../api";

export default function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");

  const handleSignup = async () => {
    try {
      const res = await API.post("/signup", { email, password });
      setMsg(res.data.message);
    } catch (err) {
      setMsg(err.response?.data?.message || "Signup failed");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-b from-blue-100 to-blue-200">
      <div className="bg-white shadow-2xl rounded-2xl p-8 w-96 text-center">
        <h2 className="text-2xl font-semibold mb-4">Create Account</h2>

        <input
          className="border p-2 w-full rounded mb-3"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className="border p-2 w-full rounded mb-3"
          type="password"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={handleSignup}
          className="bg-blue-500 hover:bg-blue-600 text-white w-full py-2 rounded-md mb-3 transition"
        >
          Sign Up
        </button>

        <p className="text-sm text-gray-600">
          Already have an account?{" "}
          <Link to="/signin" className="text-blue-600 font-medium hover:underline">
            Sign in
          </Link>
        </p>

        {msg && <p className="text-sm text-green-600 mt-3">{msg}</p>}
      </div>
    </div>
  );
}

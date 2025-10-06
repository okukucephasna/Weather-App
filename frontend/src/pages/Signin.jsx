import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../api";

export default function Signin() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");
  const navigate = useNavigate();

  const handleSignin = async () => {
    try {
      const res = await API.post("/signin", { email, password });
      setMsg(res.data.message);
      if (res.status === 200) navigate("/dashboard");
    } catch (err) {
      setMsg(err.response?.data?.message || "Login failed");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-b from-green-100 to-green-200">
      <div className="bg-white shadow-2xl rounded-2xl p-8 w-96 text-center">
        <h2 className="text-2xl font-semibold mb-4">Sign In</h2>

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
          onClick={handleSignin}
          className="bg-green-500 hover:bg-green-600 text-white w-full py-2 rounded-md mb-3 transition"
        >
          Login
        </button>

        <p className="text-sm text-gray-600">
          Don’t have an account?{" "}
          <Link to="/" className="text-green-600 font-medium hover:underline">
            Create one
          </Link>
        </p>

        {msg && <p className="text-sm text-red-600 mt-3">{msg}</p>}
      </div>
    </div>
  );
}
